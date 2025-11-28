from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional

@dataclass
class TransacaoDTO:
    id_referencia: str
    data_inicio: datetime
    buy_in: float
    premio: float 
    
    @property
    def lucro(self):
        return self.premio - self.buy_in

@dataclass
class HandHistoryDTO:
    id_hh: str
    nome_arquivo: str
    nome_torneio: str
    data_hh: datetime
    buy_in_estimado: float

@dataclass
class RelatorioProcessamento:
    sucessos: int
    falhas: int
    erros_detalhados: List[str]

@dataclass
class TorneioConsolidado:
    status: str 
    dados_financeiros: Optional[TransacaoDTO] = None
    dados_hh: Optional[HandHistoryDTO] = None

    @property
    def resumo(self):
        nome = self.dados_hh.nome_torneio if self.dados_hh else "Desconhecido"
        buy_in = self.dados_financeiros.buy_in if self.dados_financeiros else (self.dados_hh.buy_in_estimado if self.dados_hh else 0.0)
        premio = self.dados_financeiros.premio if self.dados_financeiros else 0.0
        
        lucro = premio - buy_in
        roi = ((premio - buy_in) / buy_in * 100) if buy_in > 0 else 0.0
        
        return {
            "Status": self.status,
            "ID": self.dados_financeiros.id_referencia if self.dados_financeiros else self.dados_hh.id_hh,
            "Torneio": nome,
            "Data": self.dados_financeiros.data_inicio if self.dados_financeiros else self.dados_hh.data_hh,
            "BuyIn": buy_in,
            "Premio": premio,
            "Lucro": lucro,
            "ROI": roi
        }