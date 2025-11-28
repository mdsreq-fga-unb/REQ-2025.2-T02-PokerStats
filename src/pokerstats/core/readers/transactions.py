import pandas as pd
from typing import List
from ..models import TransacaoDTO 

def ler_transacoes_excel(caminho_arquivo: str) -> List[TransacaoDTO]:
    lista_transacoes = []
    try:
        if caminho_arquivo.endswith('.csv'):
            df_temp = pd.read_csv(caminho_arquivo, header=None, nrows=20)
        else:
            df_temp = pd.read_excel(caminho_arquivo, header=None, nrows=20)

        idx_cabecalho = -1
        for i, row in df_temp.iterrows():
            linha = " ".join(row.astype(str).values)
            if "Reference" in linha and "Description" in linha:
                idx_cabecalho = i
                break
        
        if idx_cabecalho == -1: return []

        if caminho_arquivo.endswith('.csv'):
            df = pd.read_csv(caminho_arquivo, header=idx_cabecalho)
        else:
            df = pd.read_excel(caminho_arquivo, header=idx_cabecalho)

        df.columns = [str(c).replace('\n', ' ').strip() for c in df.columns]

        col_ref = next((c for c in df.columns if 'Reference' in c), None)
        col_amount = next((c for c in df.columns if 'Cash Amount' in c or 'Amount' in c), None)
        col_date = next((c for c in df.columns if 'Date' in c), None)
        col_desc = next((c for c in df.columns if 'Description' in c), None)

        if not all([col_ref, col_amount, col_date, col_desc]): return []

        df = df[df[col_desc].astype(str).str.contains("Tournament", case=False, na=False)]
        df[col_date] = pd.to_datetime(df[col_date])

        for ref, dados in df.groupby(col_ref):
            buyin_rows = dados[dados[col_amount] < 0]
            if buyin_rows.empty: continue
            
            valor_buyin = abs(dados[dados[col_amount] < 0][col_amount].sum())
            valor_premio = dados[dados[col_amount] > 0][col_amount].sum()
            data_inicial = buyin_rows[col_date].min()

            lista_transacoes.append(TransacaoDTO(
                id_referencia=str(ref),
                data_inicio=data_inicial,
                buy_in=float(valor_buyin),
                premio=float(valor_premio)
            ))
    except Exception as e:
        print(f"Erro leitura transações: {e}")
        
    return lista_transacoes