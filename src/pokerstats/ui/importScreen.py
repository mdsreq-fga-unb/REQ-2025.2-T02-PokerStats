import customtkinter as ctk
from tkinter import filedialog, messagebox
from src.pokerstats.core.service import BodogService 

class BodogApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.service = BodogService()
        self.transacoes_carregadas = []
        self.hhs_carregados = []

        self.title("Bodog Manager - Importação e Consolidação")
        self.geometry("1000x700") 
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=0) # Status
        self.grid_rowconfigure(2, weight=1) # Tabela (Expande)
        self.grid_rowconfigure(3, weight=0) # Log (Fixo embaixo)

        self.frame_top = ctk.CTkFrame(self)
        self.frame_top.grid(row=0, column=0, padx=20, pady=10, sticky="ew")
        
        self.btn_transacoes = ctk.CTkButton(self.frame_top, text="1. Transações (XLSX)", command=self.carregar_transacoes)
        self.btn_transacoes.pack(side="left", padx=10, pady=10)

        self.btn_hhs = ctk.CTkButton(self.frame_top, text="2. Hand History (TXT)", fg_color="green", command=self.carregar_hhs)
        self.btn_hhs.pack(side="left", padx=10, pady=10)
        
        self.btn_consolidar = ctk.CTkButton(self.frame_top, text="3. Consolidar e Salvar", fg_color="orange", command=self.consolidar)
        self.btn_consolidar.pack(side="right", padx=10, pady=10)

        self.lbl_status = ctk.CTkLabel(self, text="Status: Aguardando arquivos...", font=("Arial", 12, "bold"))
        self.lbl_status.grid(row=1, column=0, sticky="w", padx=25, pady=(0, 5))

        self.tabela_frame = ctk.CTkScrollableFrame(self, label_text="Resultado da Consolidação")
        self.tabela_frame.grid(row=2, column=0, padx=20, pady=5, sticky="nsew")
        
        self.tabela_frame.grid_columnconfigure(0, weight=1) # Data
        self.tabela_frame.grid_columnconfigure(1, weight=3) # Nome Torneio
        self.tabela_frame.grid_columnconfigure(2, weight=1) # Status
        self.tabela_frame.grid_columnconfigure(3, weight=1) # Lucro

        self.log_box = ctk.CTkTextbox(self, height=100, font=("Consolas", 11))
        self.log_box.grid(row=3, column=0, padx=20, pady=10, sticky="ew")
        
        self.log("Sistema pronto.")

    def log(self, texto):
        self.log_box.insert("end", texto + "\n")
        self.log_box.see("end")

    def carregar_transacoes(self):
        caminho = filedialog.askopenfilename(title="Selecione Transações", filetypes=[("Excel/CSV", "*.xlsx *.xls *.csv")])
        if not caminho: return

        self.log(f"Lendo: {caminho}...")
        try:
            self.transacoes_carregadas = self.service.ler_transacoes(caminho)
            if self.transacoes_carregadas:
                self.log(f"Sucesso: {len(self.transacoes_carregadas)} transações carregadas.")
                self._atualizar_status()
            else:
                self.log("Aviso: Nenhuma transação de torneio encontrada.")
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    def carregar_hhs(self):
        caminhos = filedialog.askopenfilenames(title="Selecione Hand Histories", filetypes=[("Arquivos de Texto", "*.txt")])
        if not caminhos: return

        self.log(f"Processando {len(caminhos)} arquivos...")
        try:
            novos_hhs, relatorio = self.service.processar_hhs(caminhos)
            self.hhs_carregados.extend(novos_hhs)
            self.log(f"HHs Lidos: {relatorio.sucessos} | Falhas: {relatorio.falhas}")
            self._atualizar_status()
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    def consolidar(self):
        if not self.transacoes_carregadas and not self.hhs_carregados:
            messagebox.showwarning("Aviso", "Sem dados para processar.")
            return

        self.log("Consolidando...")
        try:
            resultado = self.service.consolidar_dados(self.transacoes_carregadas, self.hhs_carregados)
            
            novos, atualizados = self.service.salvar_no_banco(resultado)
            self.log(f"Salvo no Banco: {novos} novos, {atualizados} atualizados.")
            
            self._renderizar_tabela(resultado)
            
            messagebox.showinfo("Concluído", f"Processamento finalizado!\nNovos: {novos}\nAtualizados: {atualizados}")

        except Exception as e:
            self.log(f"ERRO: {str(e)}")
            messagebox.showerror("Erro Crítico", str(e))

    def _renderizar_tabela(self, lista_consolidados):
        for widget in self.tabela_frame.winfo_children():
            widget.destroy()

        headers = ["Data", "Torneio", "Status", "Buy-in", "Prêmio", "Lucro"]
        for i, h in enumerate(headers):
            lbl = ctk.CTkLabel(self.tabela_frame, text=h, font=("Arial", 12, "bold"))
            lbl.grid(row=0, column=i, padx=5, pady=5, sticky="w")

        for idx, item in enumerate(lista_consolidados):
            r = item.resumo
            row_num = idx + 1
            
            cor_lucro = "white"
            if r['Lucro'] > 0: cor_lucro = "#2ecc71" # Verde
            elif r['Lucro'] < 0: cor_lucro = "#e74c3c" # Vermelho

            cor_status = "gray"
            if r['Status'] == "VINCULADO": cor_status = "#3498db" # Azul
            
            data_str = r['Data'].strftime("%d/%m %H:%M") if r['Data'] else "--"
            nome_limpo = r['Torneio'][:35] + "..." if len(r['Torneio']) > 35 else r['Torneio']
            
            ctk.CTkLabel(self.tabela_frame, text=data_str).grid(row=row_num, column=0, padx=5, sticky="w")
            ctk.CTkLabel(self.tabela_frame, text=nome_limpo).grid(row=row_num, column=1, padx=5, sticky="w")
            ctk.CTkLabel(self.tabela_frame, text=r['Status'], text_color=cor_status).grid(row=row_num, column=2, padx=5, sticky="w")
            ctk.CTkLabel(self.tabela_frame, text=f"${r['BuyIn']:.2f}").grid(row=row_num, column=3, padx=5, sticky="w")
            ctk.CTkLabel(self.tabela_frame, text=f"${r['Premio']:.2f}").grid(row=row_num, column=4, padx=5, sticky="w")
            ctk.CTkLabel(self.tabela_frame, text=f"${r['Lucro']:.2f}", text_color=cor_lucro, font=("Arial", 12, "bold")).grid(row=row_num, column=5, padx=5, sticky="w")

    def _atualizar_status(self):
        self.lbl_status.configure(text=f"Memória: {len(self.transacoes_carregadas)} Transações | {len(self.hhs_carregados)} Hand Histories")

if __name__ == "__main__":
    app = BodogApp()
    app.mainloop()