from typing import List, Tuple
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
        
        JANELA_HORAS = 0.33
        TOLERANCIA_VALOR = 0.10

        candidatos = []

        for t in transacoes:
            for hh in hhs:
                diff_horas = abs((t.data_inicio - hh.data_hh).total_seconds() / 3600)
                diff_valor = abs(t.buy_in - hh.buy_in_estimado)
                
                if diff_horas <= JANELA_HORAS and diff_valor <= TOLERANCIA_VALOR:
                    candidatos.append({
                        'diff_tempo': diff_horas,
                        'transacao': t,
                        'hh': hh
                    })

        candidatos.sort(key=lambda x: x['diff_tempo'])

        transacoes_usadas = set()
        hhs_usados = set()

        for c in candidatos:
            t = c['transacao']
            hh = c['hh']
            
            id_t = id(t)
            id_h = id(hh)

            if id_t not in transacoes_usadas and id_h not in hhs_usados:
                consolidados.append(TorneioConsolidado("VINCULADO", t, hh))
                transacoes_usadas.add(id_t)
                hhs_usados.add(id_h)

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
        
        total_lucro = total_premio - total_buyin
        
        return {
            "total_buyin": total_buyin,
            "total_premio": total_premio,
            "total_lucro": total_lucro
        }