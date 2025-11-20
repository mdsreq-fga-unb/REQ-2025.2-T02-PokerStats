from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional, Tuple
import pandas as pd
import re
import os

# --- DTOs (Estruturas de Dados) ---
@dataclass
class TransacaoDTO:
    id_referencia: str
    data_inicio: datetime
    buy_in: float
    premio: float # Soma de cashouts
    
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
    status: str # VINCULADO, PENDENTE_HH, PENDENTE_FINANCEIRO
    dados_financeiros: Optional[TransacaoDTO] = None
    dados_hh: Optional[HandHistoryDTO] = None

    @property
    def resumo(self):
        nome = self.dados_hh.nome_torneio if self.dados_hh else "Desconhecido"
        # Prioridade para o valor financeiro real, senão usa o estimado do TXT
        buy_in = self.dados_financeiros.buy_in if self.dados_financeiros else (self.dados_hh.buy_in_estimado if self.dados_hh else 0.0)
        premio = self.dados_financeiros.premio if self.dados_financeiros else 0.0
        
        roi = 0.0
        if buy_in > 0:
            roi = ((premio - buy_in) / buy_in) * 100
        
        return {
            "Status": self.status,
            "ID": self.dados_financeiros.id_referencia if self.dados_financeiros else self.dados_hh.id_hh,
            "Torneio": nome,
            "Data": self.dados_financeiros.data_inicio if self.dados_financeiros else self.dados_hh.data_hh,
            "BuyIn": buy_in,
            "Premio": premio,
            "Lucro": premio - buy_in,
            "ROI": roi
        }

class BodogCore:
    
    # --- 1. Leitura Financeira ---
    def ler_transacoes(self, caminho_arquivo: str) -> List[TransacaoDTO]:
        lista_transacoes = []
        try:
            # Detecção de cabeçalho
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

            # Leitura oficial
            if caminho_arquivo.endswith('.csv'):
                df = pd.read_csv(caminho_arquivo, header=idx_cabecalho)
            else:
                df = pd.read_excel(caminho_arquivo, header=idx_cabecalho)

            # Limpeza de colunas
            df.columns = [str(c).replace('\n', ' ').strip() for c in df.columns]

            col_ref = next((c for c in df.columns if 'Reference' in c), None)
            col_amount = next((c for c in df.columns if 'Cash Amount' in c or 'Amount' in c), None)
            col_date = next((c for c in df.columns if 'Date' in c), None)
            col_desc = next((c for c in df.columns if 'Description' in c), None)

            if not all([col_ref, col_amount, col_date, col_desc]): return []

            df = df[df[col_desc].astype(str).str.contains("Tournament", case=False, na=False)]
            df[col_date] = pd.to_datetime(df[col_date])

            # Agrupamento (Transações Múltiplas)
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

    # --- 2. Leitura de Hand History (Lote) ---
    def processar_lote_hhs(self, lista_caminhos: List[str]) -> Tuple[List[HandHistoryDTO], RelatorioProcessamento]:
        hhs_validos = []
        erros = []
        sucessos = 0
        
        for caminho in lista_caminhos:
            if not os.path.exists(caminho):
                erros.append(f"Arquivo não encontrado: {caminho}")
                continue
                
            hh = self._ler_unico_hh(caminho)
            if hh:
                hhs_validos.append(hh)
                sucessos += 1
            else:
                erros.append(f"Falha ao ler: {os.path.basename(caminho)}")
        
        relatorio = RelatorioProcessamento(sucessos=sucessos, falhas=len(erros), erros_detalhados=erros)
        return hhs_validos, relatorio

    def _ler_unico_hh(self, caminho_arquivo: str) -> Optional[HandHistoryDTO]:
        # Método interno auxiliar
        nome_arquivo = os.path.basename(caminho_arquivo)
        try:
            with open(caminho_arquivo, 'r', encoding='utf-8', errors='ignore') as f:
                conteudo = f.read(2048)
            
            # ID
            match_id = re.search(r'Tourney No\.(\d+)', conteudo) or re.search(r'Tourney No\.(\d+)', nome_arquivo)
            if not match_id: return None

            # Data
            match_data = re.search(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})', conteudo)
            data_obj = pd.to_datetime(match_data.group(1)) if match_data else datetime.now()
            

            # Valor (Regex corrigido: $10-$1)
            match_valor = re.search(r'\$(\d+(?:\.\d+)?)-\$(\d+(?:\.\d+)?)', nome_arquivo)
            valor = 0.0
            if match_valor:
                valor = float(match_valor.group(1)) + float(match_valor.group(2))

            # Nome
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

    # --- 3. Consolidação (Core Logic) ---
    def consolidar_dados(self, transacoes: List[TransacaoDTO], hhs: List[HandHistoryDTO]) -> List[TorneioConsolidado]:
        consolidados = []
        hhs_pool = hhs.copy() # Cópia para ir removendo os que derem match
        
        # Janelas de tolerância
        JANELA_HORAS = 4
        TOLERANCIA_VALOR = 0.10 # 10 centavos

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
                hhs_pool.remove(match) # Garante que um HH não seja usado duas vezes
            else:
                consolidados.append(TorneioConsolidado("PENDENTE_HH", t))

        # Adiciona o que sobrou de HH (torneios que não têm transação financeira correspondente)
        for hh_restante in hhs_pool:
            consolidados.append(TorneioConsolidado("PENDENTE_FINANCEIRO", None, hh_restante))
            
        return consolidados

# --- Exemplo de Uso do Novo Core ---
if __name__ == "__main__":
    core = BodogCore()
    
    # 1. Transações
    print("--- Lendo Transações ---")
    transacoes = core.ler_transacoes("transacaoNovembro.xlsx")
    print(f"Transações encontradas: {len(transacoes)}")

    # 2. Lista de Arquivos HH (Simulando seleção de vários arquivos)
    # Aqui você passaria todos os caminhos que o usuário selecionou na interface
    print("\n--- Lendo Lote de HHs ---")
    meus_arquivos = [
        "HH20251113-113000 - 576 - MTT - $6.888 Garantidos (Crazy 8s) - $10-$1 - TorneioHOLDEM - NL -Tourney No.77754743.txt" # Exemplo de erro
    ]
    
    hhs_lidos, relatorio = core.processar_lote_hhs(meus_arquivos)
    print(f"HHs Sucesso: {relatorio.sucessos} | Falhas: {relatorio.falhas}")

    # 3. Consolidação
    print("\n--- Consolidando ---")
    resultado = core.consolidar_dados(transacoes, hhs_lidos)
    lista_hhs = []
    
    if os.path.exists(meus_arquivos):
        hh = core.ler_hh(meus_arquivos)
        if hh: lista_hhs.append(hh)

    # 3. Executar e mostrar tabela
    print(f"Processando {len(transacoes)} transações e {len(lista_hhs)} arquivos de HH...\n")
    core.mapear(transacoes, lista_hhs)
    
    
    # Exibindo apenas os vinculados para teste
    print(f"{'STATUS':<20} | {'TORNEIO':<30} | {'LUCRO':<10}")
    print("-" * 65)
    for item in resultado:
        r = item.resumo
        # Mostra vinculados ou o ID específico se estivermos testando
        if r['Status'] == "VINCULADO": 
            print(f"{r['Status']:<20} | {r['Torneio']:<30} | ${r['Lucro']:.2f}")