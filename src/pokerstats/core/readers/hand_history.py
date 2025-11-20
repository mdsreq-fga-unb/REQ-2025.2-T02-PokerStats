import re
import os
import pandas as pd
from datetime import datetime
from typing import List, Tuple, Optional
from ..models import HandHistoryDTO, RelatorioProcessamento

def processar_lote_hhs(lista_caminhos: List[str]) -> Tuple[List[HandHistoryDTO], RelatorioProcessamento]:
    hhs_validos = []
    erros = []
    sucessos = 0
    
    for caminho in lista_caminhos:
        if not os.path.exists(caminho):
            erros.append(f"Arquivo não encontrado: {caminho}")
            continue
            
        hh = _ler_unico_hh(caminho)
        if hh:
            hhs_validos.append(hh)
            sucessos += 1
        else:
            erros.append(f"Falha ao ler: {os.path.basename(caminho)}")
    
    relatorio = RelatorioProcessamento(sucessos=sucessos, falhas=len(erros), erros_detalhados=erros)
    return hhs_validos, relatorio

def _ler_unico_hh(caminho_arquivo: str) -> Optional[HandHistoryDTO]:
    nome_arquivo = os.path.basename(caminho_arquivo)
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8', errors='ignore') as f:
            conteudo = f.read(2048)
        
        match_id = re.search(r'Tourney No\.(\d+)', conteudo) or re.search(r'Tourney No\.(\d+)', nome_arquivo)
        if not match_id: return None

        match_data = re.search(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})', conteudo)
        data_obj = pd.to_datetime(match_data.group(1)) if match_data else datetime.now()

        match_valor = re.search(r'\$(\d+(?:\.\d+)?)-\$(\d+(?:\.\d+)?)', nome_arquivo)
        valor = 0.0
        if match_valor:
            valor = float(match_valor.group(1)) + float(match_valor.group(2))

        partes = nome_arquivo.split('-')
        nome = "Desconhecido"
        candidate = ""
        for p in partes:
            if "Garantidos" in p or "(" in p:
                candidate = p.strip()
                break
        
        if not candidate and len(partes) > 3:
            if "MTT" not in partes[3]: candidate = partes[3].strip()
            elif len(partes) > 4: candidate = partes[4].strip()
        
        if candidate: nome = candidate

        return HandHistoryDTO(match_id.group(1), nome_arquivo, nome, data_obj, valor)
    except:
        return None