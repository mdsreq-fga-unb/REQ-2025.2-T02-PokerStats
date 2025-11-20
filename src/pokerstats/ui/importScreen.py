import customtkinter as ctk
from tkinter import filedialog, messagebox
from src.pokerstats.core.service import BodogService

class BodogApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.service = BodogService()
        self.transacoes_carregadas = []
        self.hhs_carregados = []

        self.title("Bodog Manager - Importação em Lote")
        self.geometry("800x600")
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1) 

        self.frame_top = ctk.CTkFrame(self)
        self.frame_top.grid(row=0, column=0, padx=20, pady=20, sticky="ew")
        
        self.btn_transacoes = ctk.CTkButton(self.frame_top, text="1. Carregar Transações (XLSX)", command=self.carregar_transacoes)
        self.btn_transacoes.pack(side="left", padx=10, pady=10)

        self.btn_hhs = ctk.CTkButton(self.frame_top, text="2. Carregar Hand History (TXT)", fg_color="green", command=self.carregar_hhs)
        self.btn_hhs.pack(side="left", padx=10, pady=10)
        
        self.btn_consolidar = ctk.CTkButton(self.frame_top, text="3. Consolidar Dados", fg_color="orange", command=self.consolidar)
        self.btn_consolidar.pack(side="right", padx=10, pady=10)

        self.lbl_status = ctk.CTkLabel(self, text="Status: Aguardando arquivos...", font=("Arial", 12))
        self.lbl_status.grid(row=1, column=0, sticky="w", padx=25)

        self.log_box = ctk.CTkTextbox(self, font=("Consolas", 12))
        self.log_box.grid(row=2, column=0, padx=20, pady=(0, 20), sticky="nsew")
        
        self.log("Bem-vindo! Siga a ordem dos botões acima.")

    def log(self, texto):
        self.log_box.insert("end", texto + "\n")
        self.log_box.see("end")

    def carregar_transacoes(self):
        caminho = filedialog.askopenfilename(filetypes=[("Excel/CSV", "*.xlsx *.xls *.csv")])
        if not caminho: return

        self.log(f"--> Lendo transações de: {caminho}...")
        self.transacoes_carregadas = self.service.ler_transacoes(caminho)
        
        if self.transacoes_carregadas:
            qtd = len(self.transacoes_carregadas)
            self.log(f"Sucesso! {qtd} registros financeiros carregados.")
            self.lbl_status.configure(text=f"Transações: {qtd} | HHs: {len(self.hhs_carregados)}")
        else:
            self.log("Erro: Nenhuma transação válida encontrada ou arquivo vazio.")

    def carregar_hhs(self):
        caminhos = filedialog.askopenfilenames(
            title="Selecione os arquivos de Hand History",
            filetypes=[("Arquivos de Texto", "*.txt")]
        )
        
        if not caminhos: return

        qtd_selecionada = len(caminhos)
        self.log(f"--> Processando lote de {qtd_selecionada} arquivos...")
        
        novos_hhs, relatorio = self.service.processar_hhs(caminhos)
        
        self.hhs_carregados.extend(novos_hhs)
        
        self.log(f"Processamento concluído:")
        self.log(f"   Lidos com sucesso: {relatorio.sucessos}")
        self.log(f"   Falhas/Ignorados: {relatorio.falhas}")
        
        if relatorio.falhas > 0:
            self.log("   (Arquivos ignorados geralmente não são torneios ou estão vazios)")

        self.lbl_status.configure(text=f"Transações: {len(self.transacoes_carregadas)} | HHs: {len(self.hhs_carregados)}")

    def consolidar(self):
        if not self.transacoes_carregadas:
            messagebox.showwarning("Aviso", "Carregue o arquivo de Transações primeiro!")
            return

        self.log("\n--> Iniciando Consolidação (Matching)...")
        resultado = self.service.consolidar_dados(self.transacoes_carregadas, self.hhs_carregados)
        
        vinculados = [r for r in resultado if r.status == "VINCULADO"]
        pendentes = [r for r in resultado if r.status != "VINCULADO"]
        
        self.log("-" * 50)
        self.log(f"RESULTADO FINAL:")
        self.log(f" Torneios Vinculados (Nome + Financeiro): {len(vinculados)}")
        self.log(f" Pendentes (Falta par): {len(pendentes)}")
        self.log("-" * 50)
        
        if vinculados:
            self.log("Exemplos de Vinculados:")
            for i, item in enumerate(vinculados[:5]):
                r = item.resumo
                self.log(f"   • {r['Torneio']} | Lucro: ${r['Lucro']:.2f}")
            if len(vinculados) > 5:
                self.log("   ... e outros.")

if __name__ == "__main__":
    app = BodogApp()
    app.mainloop()