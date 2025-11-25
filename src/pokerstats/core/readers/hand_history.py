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
            erros.append(f"Formato inválido: {os.path.basename(caminho)}")
    
    relatorio = RelatorioProcessamento(sucessos=sucessos, falhas=len(erros), erros_detalhados=erros)
    return hhs_validos, relatorio

def _ler_unico_hh(caminho_arquivo: str) -> Optional[HandHistoryDTO]:
    nome_arquivo = os.path.basename(caminho_arquivo)
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8', errors='ignore') as f:
            conteudo = f.read(4096) 
        
        match_id = re.search(r'Tourney No\.(\d+)', conteudo) or re.search(r'Tourney No\.(\d+)', nome_arquivo)
        if not match_id: return None
        id_hh = match_id.group(1)

        match_data = re.search(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})', conteudo)
        data_obj = pd.to_datetime(match_data.group(1)) if match_data else datetime.now()

        buy_in_est = 0.0
        match_buyin_txt = re.search(r'Buy-In[:\s]+\$([\d\.]+)\s*[+\-]\s*\$([\d\.]+)', conteudo, re.IGNORECASE)
        
        if match_buyin_txt:
            v1 = float(match_buyin_txt.group(1))
            v2 = float(match_buyin_txt.group(2))
            buy_in_est = v1 + v2
        
        partes = nome_arquivo.split('-')
        nome_torneio = "Torneio Bodog" 
        
        idx_tipo = -1
        idx_buyin_nome = -1

        for i, parte in enumerate(partes):
            p_limpa = parte.strip().upper()
            
            if idx_tipo == -1:
                if "MTT" in p_limpa:
                    idx_tipo = i
                elif "SIT" in p_limpa and "GO" in p_limpa:
                    idx_tipo = i
                elif "SNG" in p_limpa:
                    idx_tipo = i
            
            if idx_buyin_nome == -1:
                if re.search(r'\$(\d+(?:\.\d+)?)[-+]?\$(\d+(?:\.\d+)?)', parte):
                    idx_buyin_nome = i
                    if buy_in_est == 0.0:
                        match_v = re.search(r'\$(\d+(?:\.\d+)?)[-+]?\$(\d+(?:\.\d+)?)', parte)
                        if match_v:
                            buy_in_est = float(match_v.group(1)) + float(match_v.group(2))

        if idx_tipo != -1:
            if idx_buyin_nome != -1 and idx_buyin_nome > idx_tipo:
                pedacos_nome = partes[idx_tipo+1 : idx_buyin_nome]
                nome_torneio = " - ".join([p.strip() for p in pedacos_nome])
            elif len(partes) > idx_tipo + 1:
                nome_torneio = partes[idx_tipo+1].strip()
                if "Sit" in partes[idx_tipo] and "Go" in partes[idx_tipo] and nome_torneio == "":
                     nome_torneio = "Sit & Go"

        if not nome_torneio or nome_torneio.replace(" ", "") == "":
             nome_torneio = "Torneio Desconhecido"

        return HandHistoryDTO(
            id_hh=id_hh,
            nome_arquivo=nome_arquivo,
            nome_torneio=nome_torneio,
            data_hh=data_obj,
            buy_in_estimado=buy_in_est
        )
    except:
        return None