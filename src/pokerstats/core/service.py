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
        return self.repo.salvar_consolidacao(lista_consolidados)
    
    def obter_historico_banco(self):
        return self.repo.listar_todos()

    def obter_resumo_financeiro(self):
        somas = self.repo.obter_somas_totais()
        total_buyin = somas[0] if somas[0] else 0.0
        total_premio = somas[1] if somas[1] else 0.0
        return {"total_buyin": total_buyin, "total_premio": total_premio, "total_lucro": total_premio - total_buyin}

    def gerar_relatorio_roi_itm(self) -> Dict:
        """
        Processa dados para ROI e ITM (In The Money).
        """
        todos_torneios = self.repo.listar_todos()
        
        stats = {
            "Geral": {"investido": 0.0, "retorno": 0.0, "total": 0, "itm": 0},
            "MTT": {"investido": 0.0, "retorno": 0.0, "total": 0, "itm": 0},
            "Sit & Go": {"investido": 0.0, "retorno": 0.0, "total": 0, "itm": 0},
            "Outros": {"investido": 0.0, "retorno": 0.0, "total": 0, "itm": 0}
        }

        for t in todos_torneios:
            inv = t.buy_in or 0.0
            ret = t.premio or 0.0
            
            stats["Geral"]["investido"] += inv
            stats["Geral"]["retorno"] += ret
            stats["Geral"]["total"] += 1
            if ret > 0: 
                stats["Geral"]["itm"] += 1
            
            nome = (t.nome_torneio or "").upper()
            
            if inv == 0 and ret > 0:
                categoria = "Outros"
            elif "SIT" in nome and "GO" in nome:
                categoria = "Sit & Go"
            elif "SNG" in nome:
                categoria = "Sit & Go"
            elif "MTT" in nome or "GUARANTEED" in nome or "GTD" in nome:
                categoria = "MTT"
            elif "CASH" in nome:
                categoria = "Outros"
            else:
                categoria = "MTT" 

            if categoria not in stats:
                stats[categoria] = {"investido": 0.0, "retorno": 0.0, "total": 0, "itm": 0}
                
            stats[categoria]["investido"] += inv
            stats[categoria]["retorno"] += ret
            stats[categoria]["total"] += 1
            if ret > 0:
                stats[categoria]["itm"] += 1

        relatorio_final = {}
        for cat, dados in stats.items():
            investido = dados["investido"]
            retorno = dados["retorno"]
            total = dados["total"]
            itm_count = dados["itm"]
            
            lucro = retorno - investido
            
            if investido > 0:
                roi_pct = ((retorno - investido) / investido) * 100
            else:
                roi_pct = 0.0 
            
            if total > 0:
                itm_pct = (itm_count / total) * 100
            else:
                itm_pct = 0.0

            relatorio_final[cat] = {
                "investido": investido,
                "retorno": retorno,
                "lucro": lucro,
                "roi": roi_pct,
                "total_count": total,
                "itm_count": itm_count,
                "itm_pct": itm_pct
            }
            
        return relatorio_final