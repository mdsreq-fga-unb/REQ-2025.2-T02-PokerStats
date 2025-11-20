from typing import List
from .models import TransacaoDTO, HandHistoryDTO, TorneioConsolidado, RelatorioProcessamento
from .readers.transactions import ler_transacoes_excel
from .readers.hand_history import processar_lote_hhs
from ..database.config import SessionLocal
from ..database.repository import TorneioRepository

class BodogService:
    def __init__(self):
        self.db = SessionLocal()
        self.repo = TorneioRepository(self.db)

    def ler_transacoes(self, caminho_arquivo: str) -> List[TransacaoDTO]:
        return ler_transacoes_excel(caminho_arquivo)

    def processar_hhs(self, lista_caminhos: List[str]): 
        return processar_lote_hhs(lista_caminhos)

    def consolidar_dados(self, transacoes: List[TransacaoDTO], hhs: List[HandHistoryDTO]) -> List[TorneioConsolidado]:
        consolidados = []
        hhs_pool = hhs.copy()
        
        JANELA_HORAS = 4
        TOLERANCIA_VALOR = 0.10

        for t in transacoes:
            match = None
            
            for hh in hhs_pool:
                diff_horas = abs((t.data_inicio - hh.data_hh).total_seconds() / 3600)
                diff_valor = abs(t.buy_in - hh.buy_in_estimado)
                
                if diff_horas <= JANELA_HORAS and diff_valor <= TOLERANCIA_VALOR:
                    match = hh
                    break
            
            if match:
                consolidados.append(TorneioConsolidado("VINCULADO", t, match))
                hhs_pool.remove(match)
            else:
                consolidados.append(TorneioConsolidado("PENDENTE_HH", t))

        for hh_restante in hhs_pool:
            consolidados.append(TorneioConsolidado("PENDENTE_FINANCEIRO", None, hh_restante))
            
        return consolidados
    
    def salvar_no_banco(self, lista_consolidados: List[TorneioConsolidado]):
            return self.repo.salvar_consolidacao(lista_consolidados)
        
    def obter_historico_banco(self):
        return self.repo.listar_todos()    