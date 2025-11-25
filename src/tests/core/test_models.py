from datetime import datetime
from pokerstats.core.models import TransacaoDTO, HandHistoryDTO, TorneioConsolidado

def test_calculo_lucro_roi_transacao():
    t = TransacaoDTO(
        id_referencia="T1",
        data_inicio=datetime(2025, 10, 15, 10, 0, 0),
        buy_in=11.0,
        premio=22.0
    )
    
    consolidado = TorneioConsolidado(status="PENDENTE", dados_financeiros=t)
    resumo = consolidado.resumo
    
    assert resumo['Lucro'] == 11.0
    assert resumo['ROI'] == 100.0

def test_calculo_roi_negativo():
    t = TransacaoDTO(
        id_referencia="T2",
        data_inicio=datetime(2025, 10, 15, 10, 0, 0),
        buy_in=10.0,
        premio=0.0
    )
    
    consolidado = TorneioConsolidado(status="PENDENTE", dados_financeiros=t)
    resumo = consolidado.resumo
    
    assert resumo['Lucro'] == -10.0
    assert resumo['ROI'] == -100.0

def test_calculo_hh_sem_transacao():
    hh = HandHistoryDTO(
        id_hh="123",
        nome_arquivo="teste.txt",
        nome_torneio="MTT",
        data_hh=datetime(2025, 10, 15, 10, 0, 0),
        buy_in_estimado=55.0
    )
    
    consolidado = TorneioConsolidado(status="PENDENTE_FINANCEIRO", dados_hh=hh)
    resumo = consolidado.resumo
    
    assert resumo['BuyIn'] == 55.0
    assert resumo['Lucro'] == -55.0