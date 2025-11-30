import customtkinter as ctk
from tkinter import filedialog, messagebox
from src.pokerstats.core.service import BodogService 

class BodogApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.service = BodogService()
        self.transacoes_carregadas = []
        self.hhs_carregados = []
        self.arquivo_transacao_atual = None

        self.title("Bodog Manager - Dashboard & Importação")
        self.geometry("1100x800")
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=0)
        self.grid_rowconfigure(2, weight=0)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=0)

        self.frame_top = ctk.CTkFrame(self)
        self.frame_top.grid(row=0, column=0, padx=20, pady=10, sticky="ew")
        
        self.btn_transacao = ctk.CTkButton(self.frame_top, text="1. Carregar Transação", command=self.carregar_transacao)
        self.btn_transacao.pack(side="left", padx=10, pady=10)

        self.btn_hhs = ctk.CTkButton(self.frame_top, text="2. Adicionar HHs", fg_color="green", command=self.carregar_hhs, state="disabled")
        self.btn_hhs.pack(side="left", padx=10, pady=10)
        
        self.btn_consolidar = ctk.CTkButton(self.frame_top, text="3. Consolidar", fg_color="orange", command=self.consolidar, state="disabled")
        self.btn_consolidar.pack(side="left", padx=10, pady=10)

        self.btn_cancelar = ctk.CTkButton(self.frame_top, text="Reiniciar", fg_color="#c0392b", width=80, command=self.reiniciar_fluxo, state="disabled")
        self.btn_cancelar.pack(side="right", padx=10, pady=10)

        self.frame_dashboard = ctk.CTkFrame(self)
        self.frame_dashboard.grid(row=1, column=0, padx=20, pady=5, sticky="ew")
        
        ctk.CTkLabel(self.frame_dashboard, text="DASHBOARD DE PERFORMANCE", font=("Arial", 14, "bold"), text_color="gray").pack(pady=(10, 5))
        
        self.container_stats = ctk.CTkFrame(self.frame_dashboard, fg_color="transparent")
        self.container_stats.pack(fill="x", padx=10, pady=10)
        
        self._construir_dashboard_vazio()

        # --- 3. Status e Tabela ---
        self.lbl_status = ctk.CTkLabel(self, text="Aguardando dados...", font=("Arial", 12))
        self.lbl_status.grid(row=2, column=0, sticky="w", padx=25, pady=5)

        self.tabela_frame = ctk.CTkScrollableFrame(self, label_text="Histórico de Torneios")
        self.tabela_frame.grid(row=3, column=0, padx=20, pady=5, sticky="nsew")
        self.tabela_frame.grid_columnconfigure((0,1,2,3), weight=1)

        # --- 4. Log ---
        self.log_box = ctk.CTkTextbox(self, height=80, font=("Consolas", 11))
        self.log_box.grid(row=4, column=0, padx=20, pady=10, sticky="ew")
        
        self._atualizar_dashboard()
        self.log("Sistema pronto.")

    def log(self, texto):
        self.log_box.insert("end", texto + "\n")
        self.log_box.see("end")

    def _formatar_moeda(self, valor):
        valor = float(valor)
        sinal = "- " if valor < 0 else ""
        texto = f"{abs(valor):,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        return f"{sinal}$ {texto}"

    def _formatar_pct(self, valor):
        return f"{valor:.2f}%"

    def _construir_dashboard_vazio(self):
        for widget in self.container_stats.winfo_children():
            widget.destroy()
        ctk.CTkLabel(self.container_stats, text="Nenhum dado registrado.", text_color="gray").pack()

    def _atualizar_dashboard(self):
        relatorio = self.service.gerar_relatorio_roi_itm()
        
        for widget in self.container_stats.winfo_children():
            widget.destroy()

        cols = len(relatorio)
        for i in range(cols):
            self.container_stats.grid_columnconfigure(i, weight=1)

        idx = 0
        for modalidade, dados in relatorio.items():
            self._criar_card_stat(idx, modalidade, dados)
            idx += 1

    def _criar_card_stat(self, col_idx, titulo, dados):
        roi = dados['roi']
        lucro = dados['lucro']
        itm_pct = dados['itm_pct']
        itm_count = dados['itm_count']
        total_count = dados['total_count']
        
        cor_valor = "#2ecc71" if lucro > 0 else ("#e74c3c" if lucro < 0 else "gray")
        
        frame = ctk.CTkFrame(self.container_stats)
        frame.grid(row=0, column=col_idx, padx=10, sticky="ew")
        
        ctk.CTkLabel(frame, text=titulo.upper(), font=("Arial", 12, "bold")).pack(pady=(5,0))
        
        lbl_roi = ctk.CTkLabel(frame, text=self._formatar_pct(roi), font=("Arial", 24, "bold"), text_color=cor_valor)
        lbl_roi.pack()
        ctk.CTkLabel(frame, text="ROI", font=("Arial", 10), text_color="gray").pack()
        
        txt_lucro = self._formatar_moeda(lucro)
        ctk.CTkLabel(frame, text=f"Lucro: {txt_lucro}", font=("Arial", 12), text_color=cor_valor).pack(pady=(5,0))
        
        txt_itm = f"{itm_pct:.2f}% ({itm_count}/{total_count})"
        ctk.CTkLabel(frame, text=f"ITM: {txt_itm}", font=("Arial", 11, "bold")).pack(pady=(2,0))

        txt_inv = self._formatar_moeda(dados['investido'])
        ctk.CTkLabel(frame, text=f"Investido: {txt_inv}", font=("Arial", 11)).pack(pady=(2,10))

    def reiniciar_fluxo(self):
        self.transacoes_carregadas = []
        self.hhs_carregados = []
        self.arquivo_transacao_atual = None
        self.btn_transacao.configure(state="normal")
        self.btn_hhs.configure(state="disabled")
        self.btn_consolidar.configure(state="disabled")
        self.btn_cancelar.configure(state="disabled")
        for w in self.tabela_frame.winfo_children(): w.destroy()
        self.lbl_status.configure(text="Reiniciado.")
        self._atualizar_dashboard()

    def carregar_transacao(self):
        caminho = filedialog.askopenfilename(parent=self, filetypes=[("Excel/CSV", "*.xlsx *.xls *.csv")])
        if not caminho: return
        try:
            transacoes = self.service.ler_transacoes(caminho)
            if not transacoes: return
            
            duplicados = self.service.verificar_duplicidade(transacoes)
            if duplicados > 0:
                if not messagebox.askyesno("Duplicidade", f"{duplicados} registros já existem. Atualizar?"): return
            
            self.transacoes_carregadas = transacoes
            self.arquivo_transacao_atual = caminho
            
            self.btn_transacao.configure(state="disabled")
            self.btn_hhs.configure(state="normal")
            self.btn_consolidar.configure(state="normal")
            self.btn_cancelar.configure(state="normal")
            self.lbl_status.configure(text=f"Arquivo: {caminho.split('/')[-1]}")
            self.log(f"Carregados {len(transacoes)} registros.")
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    def carregar_hhs(self):
        caminhos = filedialog.askopenfilenames(parent=self, filetypes=[("Texto", "*.txt")])
        if not caminhos: return
        try:
            novos, relatorio = self.service.processar_hhs(caminhos)
            self.hhs_carregados.extend(novos)
            self.log(f"HHs: {relatorio.sucessos} ok, {relatorio.falhas} ignorados.")
            self.lbl_status.configure(text=f"Transações: {len(self.transacoes_carregadas)} | HHs: {len(self.hhs_carregados)}")
            
            if self.transacoes_carregadas:
                preview, _ = self.service.consolidar_dados(self.transacoes_carregadas, self.hhs_carregados)
                self._renderizar_tabela(preview)
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    def consolidar(self):
        try:
            resultado, descartados = self.service.consolidar_dados(self.transacoes_carregadas, self.hhs_carregados)
            novos, atualizados = self.service.salvar_no_banco(resultado)
            messagebox.showinfo("Sucesso", f"Salvo!\nNovos: {novos}\nAtualizados: {atualizados}\nDescartados: {descartados}")
            self.reiniciar_fluxo()
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    def _renderizar_tabela(self, lista):
        for w in self.tabela_frame.winfo_children(): w.destroy()
        headers = ["Data", "Torneio", "Status", "Lucro"]
        for i, h in enumerate(headers):
            ctk.CTkLabel(self.tabela_frame, text=h, font=("Arial",12,"bold")).grid(row=0, column=i, padx=5, sticky="w")
        
        vinculados = [x for x in lista if x.status == "VINCULADO"]
        for idx, item in enumerate(vinculados[:50]):
            r = item.resumo
            cor = "#2ecc71" if r['Lucro'] > 0 else ("#e74c3c" if r['Lucro'] < 0 else "white")
            ctk.CTkLabel(self.tabela_frame, text=r['Data'].strftime("%d/%m %H:%M")).grid(row=idx+1, column=0, padx=5, sticky="w")
            ctk.CTkLabel(self.tabela_frame, text=r['Torneio'][:35]).grid(row=idx+1, column=1, padx=5, sticky="w")
            ctk.CTkLabel(self.tabela_frame, text="OK", text_color="#3498db").grid(row=idx+1, column=2, padx=5, sticky="w")
            ctk.CTkLabel(self.tabela_frame, text=self._formatar_moeda(r['Lucro']), text_color=cor).grid(row=idx+1, column=3, padx=5, sticky="w")

if __name__ == "__main__":
    app = BodogApp()
    app.mainloop()