import os
from datetime import datetime
from pokerstats.core.readers.hand_history import _ler_unico_hh

def test_leitura_hh_mtt_padrao(tmp_path):
    conteudo = """Bodog.com Hand #123: HOLDEM Tournament #77754743 TBL#1 - Level 1 - 2025-11-13 15:33:55
Tourney No.77754743
Buy-In: $10.00 + $1.00"""
    
    arquivo = tmp_path / "HH20251113-153355 - 77754743 - MTT - Crazy 8s - $10-$1.txt"
    arquivo.write_text(conteudo, encoding="utf-8")
    
    dto = _ler_unico_hh(str(arquivo))
    
    assert dto is not None
    assert dto.id_hh == "77754743"
    assert dto.buy_in_estimado == 11.0
    assert dto.nome_torneio == "Crazy 8s"
    assert dto.data_hh == datetime(2025, 11, 13, 15, 33, 55)

def test_leitura_hh_sit_go_double_up(tmp_path):
    conteudo = """Bodog.com Hand #456: HOLDEM Tournament #64732590 - Level 1 - 2025-10-15 03:40:00
Tourney No.64732590
Buy-In: $50.00 + $5.00"""
    
    arquivo = tmp_path / "HH20251015 - 64732590 - SNG - Sit & Go Double Up - $50-$5.txt"
    arquivo.write_text(conteudo, encoding="utf-8")
    
    dto = _ler_unico_hh(str(arquivo))
    
    assert dto is not None
    assert dto.buy_in_estimado == 55.0
    assert "Double Up" in dto.nome_torneio 

def test_leitura_arquivo_renomeado_com_buyin_interno(tmp_path):
    conteudo = """Bodog.com Hand #999: HOLDEM Tournament #88888888
Tourney No.88888888
Level 1 - 2025-12-01 10:00:00
Buy-In: $5.00 + $0.50"""
    
    arquivo = tmp_path / "meu_arquivo_louco.txt"
    arquivo.write_text(conteudo, encoding="utf-8")
    
    dto = _ler_unico_hh(str(arquivo))
    
    assert dto is not None
    assert dto.id_hh == "88888888"
    assert dto.buy_in_estimado == 5.50
    assert dto.data_hh == datetime(2025, 12, 1, 10, 0, 0)