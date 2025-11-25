from datetime import datetime
from pokerstats.database.repository import TorneioRepository
from pokerstats.core.models import TorneioConsolidado, TransacaoDTO, HandHistoryDTO
from pokerstats.database.schemas import TransacaoDB

def test_salvar_novo_registro(db_session):
    repo = TorneioRepository(db_session)
    
    t = TransacaoDTO("REF1", datetime.now(), 10.0, 20.0)
    hh = HandHistoryDTO("HH1", "a.txt", "Torneio Teste", datetime.now(), 10.0)
    
    item = TorneioConsolidado("VINCULADO", t, hh)
    
    novos, atualizados = repo.salvar_consolidacao([item])
    
    assert novos == 1
    assert atualizados == 0
    
    salvo = db_session.query(TransacaoDB).first()
    assert salvo.id_transacao == "REF1"
    assert salvo.id_hh == "HH1"
    assert salvo.resultado.lucro == 10.0

def test_atualizacao_idempotente(db_session):
    repo = TorneioRepository(db_session)
    
    t = TransacaoDTO("REF1", datetime.now(), 10.0, 0.0)
    item = TorneioConsolidado("PENDENTE_HH", t, None)
    
    repo.salvar_consolidacao([item])
    
    hh = HandHistoryDTO("HH99", "a.txt", "Torneio Completo", datetime.now(), 10.0)
    item_atualizado = TorneioConsolidado("VINCULADO", t, hh)
    
    novos, atualizados = repo.salvar_consolidacao([item_atualizado])
    
    assert novos == 0
    assert atualizados == 1
    
    salvo = db_session.query(TransacaoDB).filter_by(id_transacao="REF1").first()
    assert salvo.id_hh == "HH99" 
    assert salvo.nome_torneio == "Torneio Completo"

def test_prevencao_duplicidade_lote(db_session):
    repo = TorneioRepository(db_session)
    
    t = TransacaoDTO("REF_DUPLA", datetime.now(), 10.0, 0.0)
    item = TorneioConsolidado("PENDENTE_HH", t, None)
    
    novos, atualizados = repo.salvar_consolidacao([item, item])
    
    assert novos == 1 
    assert atualizados == 0