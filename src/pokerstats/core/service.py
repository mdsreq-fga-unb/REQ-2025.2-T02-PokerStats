from typing import List, Tuple, Dict
from .models import TransacaoDTO, HandHistoryDTO, TorneioConsolidado
from .readers.transactions import ler_transacoes_excel
from .readers.hand_history import processar_lote_hhs

class BodogService:
    def __init__(self):
        from ..database.config import SessionLocal
        from ..database.repository import TorneioRepository
        
        self.db = SessionLocal()
        self.repo = TorneioRepository(self.db)
        
        self._cache_dados = None

    def ler_transacoes(self, caminho_arquivo: str) -> List[TransacaoDTO]:
        return ler_transacoes_excel(caminho_arquivo)
    
    def verificar_duplicidade(self, transacoes: List[TransacaoDTO]) -> int:
        ids = [t.id_referencia for t in transacoes if t.id_referencia]
        return self.repo.contar_transacoes_existentes(ids)

    def processar_hhs(self, lista_caminhos: List[str]): 
        return processar_lote_hhs(lista_caminhos)

    def consolidar_dados(self, transacoes: List[TransacaoDTO], hhs: List[HandHistoryDTO]) -> Tuple[List[TorneioConsolidado], int]:
        consolidados = []
        JANELA_HORAS = 0.75
        TOLERANCIA_VALOR = 0.10
        candidatos = []

        for t in transacoes:
            for hh in hhs:
                diff_horas = abs((t.data_inicio - hh.data_hh).total_seconds() / 3600)
                diff_valor = abs(t.buy_in - hh.buy_in_estimado)
                
                if diff_horas <= JANELA_HORAS and diff_valor <= TOLERANCIA_VALOR:
                    candidatos.append({'diff_tempo': diff_horas, 'transacao': t, 'hh': hh})

        candidatos.sort(key=lambda x: x['diff_tempo'])
        transacoes_usadas = set()
        hhs_usados = set()

        for c in candidatos:
            t, hh = c['transacao'], c['hh']
            if id(t) not in transacoes_usadas and id(hh) not in hhs_usados:
                consolidados.append(TorneioConsolidado("VINCULADO", t, hh))
                transacoes_usadas.add(id(t))
                hhs_usados.add(id(hh))

        for t in transacoes:
            if id(t) not in transacoes_usadas:
                consolidados.append(TorneioConsolidado("PENDENTE_HH", t))

        qtd_descartados = len(hhs) - len(hhs_usados)
        return consolidados, qtd_descartados

    def salvar_no_banco(self, lista_consolidados: List[TorneioConsolidado]):
        novos, atualizados = self.repo.salvar_consolidacao(lista_consolidados)
        self._cache_dados = None
        return novos, atualizados

    def obter_historico_banco(self):
        """
        Retorna a lista completa para o cache da UI.
        Usa o cache interno do Service se disponível.
        """
        if self._cache_dados is None:
            self._cache_dados = self.repo.listar_todos()
        return self._cache_dados

    def recarregar_cache_banco(self):
        """Força a ida ao banco (usado no botão Atualizar)"""
        self._cache_dados = self.repo.listar_todos()
        return self._cache_dados

    def deletar_registro(self, db_id: int):
        sucesso = self.repo.deletar_transacao(db_id)
        if sucesso and self._cache_dados:
            self._cache_dados = [x for x in self._cache_dados if x.id != db_id]
        return sucesso

    def atualizar_registro(self, db_id: int, dados: dict):
        item_atualizado = self.repo.atualizar_transacao(db_id, dados)
        if item_atualizado and self._cache_dados:
             for i, item in enumerate(self._cache_dados):
                if item.id == db_id:
                    if item_atualizado is True:
                        self._cache_dados[i] = self.repo.buscar_por_id(db_id)
                    else:
                        self._cache_dados[i] = item_atualizado
                    break
        return True

    def gerar_relatorio_roi_itm(self) -> Dict:
        dados = self.obter_historico_banco()
        
        stats = {
            "Geral": {"investido": 0.0, "retorno": 0.0, "total": 0, "itm": 0},
            "MTT": {"investido": 0.0, "retorno": 0.0, "total": 0, "itm": 0},
            "Sit & Go": {"investido": 0.0, "retorno": 0.0, "total": 0, "itm": 0},
            "Outros": {"investido": 0.0, "retorno": 0.0, "total": 0, "itm": 0}
        }

        for t in dados:
            inv = t.buy_in or 0.0
            ret = t.premio or 0.0
            
            stats["Geral"]["investido"] += inv
            stats["Geral"]["retorno"] += ret
            stats["Geral"]["total"] += 1
            if ret > 0: stats["Geral"]["itm"] += 1
            
            nome = (t.nome_torneio or "").upper()
            
            if inv == 0 and ret > 0: categoria = "Outros"
            elif "SIT" in nome and "GO" in nome: categoria = "Sit & Go"
            elif "SNG" in nome: categoria = "Sit & Go"
            elif "MTT" in nome or "GUARANTEED" in nome or "GTD" in nome: categoria = "MTT"
            elif "CASH" in nome: categoria = "Outros"
            else: categoria = "MTT" 

            if categoria not in stats: stats[categoria] = {"investido": 0.0, "retorno": 0.0, "total": 0, "itm": 0}
            stats[categoria]["investido"] += inv
            stats[categoria]["retorno"] += ret
            stats[categoria]["total"] += 1
            if ret > 0: stats[categoria]["itm"] += 1

        relatorio_final = {}
        for cat, d in stats.items():
            investido = d["investido"]
            retorno = d["retorno"]
            lucro = retorno - investido
            roi = ((retorno - investido) / investido * 100) if investido > 0 else 0.0
            itm_pct = (d["itm"] / d["total"] * 100) if d["total"] > 0 else 0.0
            
            relatorio_final[cat] = {
                "investido": investido, "retorno": retorno, "lucro": lucro,
                "roi": roi, "total_count": d["total"], "itm_count": d["itm"], "itm_pct": itm_pct
            }
            
        return relatorio_final
    
    def deletar_em_lote(self, lista_ids: List[int]):
        sucesso = self.repo.deletar_em_lote(lista_ids)
        if sucesso and self._cache_dados:
            ids_set = set(lista_ids)
            self._cache_dados = [x for x in self._cache_dados if x.id not in ids_set]
        return sucesso

    def limpar_banco_completo(self):
        sucesso = self.repo.limpar_banco()
        if sucesso:
            self._cache_dados = [] 
        return sucesso
    
    def recarregar_cache_banco(self):
        self._cache_dados = self.repo.listar_todos()
        return self._cache_dados