from datetime import datetime
from pokerstats.core.service import BodogService
from pokerstats.core.models import TransacaoDTO, HandHistoryDTO

def test_match_perfeito():
    service = BodogService()
    
    t1 = TransacaoDTO("T1", datetime(2025, 10, 20, 14, 0, 0), 11.0, 0.0)
    hh1 = HandHistoryDTO("H1", "arq1.txt", "MTT", datetime(2025, 10, 20, 14, 2, 0), 11.0)
    
    res, descartados = service.consolidar_dados([t1], [hh1])
    
    assert len(res) == 1
    assert res[0].status == "VINCULADO"
    assert res[0].dados_financeiros == t1
    assert res[0].dados_hh == hh1
    assert descartados == 0

def test_match_recusado_valor_diferente():
    service = BodogService()
    
    t1 = TransacaoDTO("T1", datetime(2025, 10, 20, 14, 0, 0), 55.0, 0.0)
    hh1 = HandHistoryDTO("H1", "arq1.txt", "MTT", datetime(2025, 10, 20, 14, 1, 0), 11.0)
    
    res, descartados = service.consolidar_dados([t1], [hh1])
    
    assert len(res) == 1
    assert res[0].status == "PENDENTE_HH"
    assert descartados == 1 

def test_match_global_melhor_candidato():
    service = BodogService()
    
    t_alvo = TransacaoDTO("T_ALVO", datetime(2025, 10, 20, 14, 0, 0), 11.0, 0.0)
    
    hh_longe = HandHistoryDTO("H_LONGE", "arq1.txt", "MTT", datetime(2025, 10, 20, 14, 25, 0), 11.0)
    hh_perto = HandHistoryDTO("H_PERTO", "arq2.txt", "MTT", datetime(2025, 10, 20, 14, 1, 0), 11.0)
    
    res, descartados = service.consolidar_dados([t_alvo], [hh_longe, hh_perto])
    
    vinculado = next(r for r in res if r.status == "VINCULADO")
    
    assert vinculado.dados_hh.id_hh == "H_PERTO"
    assert descartados == 1