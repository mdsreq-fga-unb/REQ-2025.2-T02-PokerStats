import customtkinter as ctk
from tkinter import filedialog, messagebox
from ..utils import formatar_moeda, formatar_pct
from ..loading import executar_com_loading

class DashboardTab(ctk.CTkFrame):
    def __init__(self, master, service, update_callback, app_instance):
        super().__init__(master)
        self.service = service
        self.on_data_change = update_callback
        self.app = app_instance
        self.transacoes_carregadas = []
        self.hhs_carregados = []
        self.arquivo_transacao_atual = None
        self._setup_ui()
        # Não carrega nada no init. O main vai mandar desenhar.

    def ao_exibir_aba(self):
        self.atualizar_view()

    def atualizar_view(self):
        # --- REMOVIDO LOADING ---
        # O cálculo de ROI na memória é instantâneo.
        relatorio = self.service.gerar_relatorio_roi_itm()
        self._renderizar_cards(relatorio)

    def _renderizar_cards(self, relatorio):
        for w in self.container_cards.winfo_children(): w.destroy()
        if not relatorio:
            ctk.CTkLabel(self.container_cards, text="Sem dados.", text_color="gray").pack()
            return
        
        cols = len(relatorio)
        for i in range(cols): self.container_cards.grid_columnconfigure(i, weight=1)
        idx = 0
        for mod, dados in relatorio.items():
            self._criar_card(idx, mod, dados)
            idx += 1

    # ... (MANTENHA O RESTO DO ARQUIVO IGUAL: _setup_ui, _criar_card, carregar_*, consolidar) ...
    # ... Apenas certifique-se que 'consolidar' chama self.on_data_change() no final ...
    
    # Vou replicar o _setup_ui e _criar_card resumidos para contexto, mas o foco é o atualizar_view acima.
    def _setup_ui(self):
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(3, weight=1)
        frame_top = ctk.CTkFrame(self); frame_top.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        self.btn_transacao = ctk.CTkButton(frame_top, text="1. Carregar Transação", command=self.carregar_transacao); self.btn_transacao.pack(side="left", padx=5)
        self.btn_hhs = ctk.CTkButton(frame_top, text="2. Adicionar HHs", fg_color="green", command=self.carregar_hhs, state="disabled"); self.btn_hhs.pack(side="left", padx=5)
        self.btn_consolidar = ctk.CTkButton(frame_top, text="3. Consolidar", fg_color="orange", command=self.consolidar, state="disabled"); self.btn_consolidar.pack(side="left", padx=5)
        self.btn_cancelar = ctk.CTkButton(frame_top, text="Reiniciar", fg_color="#c0392b", width=80, command=self.reiniciar_fluxo, state="disabled"); self.btn_cancelar.pack(side="right", padx=5)
        self.frame_stats = ctk.CTkFrame(self); self.frame_stats.grid(row=1, column=0, padx=10, pady=5, sticky="ew")
        self.container_cards = ctk.CTkFrame(self.frame_stats, fg_color="transparent"); self.container_cards.pack(fill="x", padx=5, pady=5)
        self.lbl_status = ctk.CTkLabel(self, text="Aguardando dados...", font=("Arial", 12)); self.lbl_status.grid(row=2, column=0, sticky="w", padx=15)
        self.tabela_preview = ctk.CTkScrollableFrame(self, label_text="Prévia da Consolidação"); self.tabela_preview.grid(row=3, column=0, padx=10, pady=5, sticky="nsew")
        self.tabela_preview.grid_columnconfigure((0,1,2,3), weight=1)

    def _criar_card(self, col, titulo, dados):
        frame = ctk.CTkFrame(self.container_cards); frame.grid(row=0, column=col, padx=5, sticky="ew")
        cor = "#2ecc71" if dados['lucro'] > 0 else ("#e74c3c" if dados['lucro'] < 0 else "gray")
        ctk.CTkLabel(frame, text=titulo.upper(), font=("Arial",12,"bold")).pack(pady=(5,0))
        ctk.CTkLabel(frame, text=formatar_pct(dados['roi']), font=("Arial",20,"bold"), text_color=cor).pack()
        ctk.CTkLabel(frame, text="ROI", font=("Arial",9), text_color="gray").pack()
        ctk.CTkLabel(frame, text=f"Lucro: {formatar_moeda(dados['lucro'])}", font=("Arial",11), text_color=cor).pack(pady=2)
        txt_itm = f"{dados['itm_pct']:.1f}% ({dados['itm_count']}/{dados['total_count']})"
        ctk.CTkLabel(frame, text=f"ITM: {txt_itm}", font=("Arial",10,"bold")).pack()
        ctk.CTkLabel(frame, text=f"Inv: {formatar_moeda(dados['investido'])}", font=("Arial",10)).pack(pady=(2,10))

    def carregar_transacao(self):
        caminho = filedialog.askopenfilename(parent=self, filetypes=[("Excel/CSV", "*.xlsx *.xls *.csv")])
        if not caminho: return
        def tarefa():
            transacoes = self.service.ler_transacoes(caminho)
            duplicados = 0
            if transacoes: duplicados = self.service.verificar_duplicidade(transacoes)
            return transacoes, duplicados
        def fim(resultado, erro):
            if erro: messagebox.showerror("Erro", str(erro)); return
            transacoes, duplicados = resultado
            if not transacoes: messagebox.showwarning("Aviso", "Nenhum dado encontrado."); return
            if duplicados > 0:
                if not messagebox.askyesno("Duplicidade", f"{duplicados} registros existem. Atualizar?"): return
            self.transacoes_carregadas = transacoes
            self.arquivo_transacao_atual = caminho
            self.btn_transacao.configure(state="disabled"); self.btn_hhs.configure(state="normal"); self.btn_consolidar.configure(state="normal"); self.btn_cancelar.configure(state="normal")
            self.lbl_status.configure(text=f"Arquivo: {caminho.split('/')[-1]}")
        executar_com_loading(self.app, tarefa, fim)

    def carregar_hhs(self):
        caminhos = filedialog.askopenfilenames(parent=self, filetypes=[("Texto", "*.txt")])
        if not caminhos: return
        def tarefa(): return self.service.processar_hhs(caminhos)
        def fim(resultado, erro):
            if erro: messagebox.showerror("Erro", str(erro)); return
            novos, relatorio = resultado
            self.hhs_carregados.extend(novos)
            self.lbl_status.configure(text=f"Transações: {len(self.transacoes_carregadas)} | HHs: {len(self.hhs_carregados)}")
            if self.transacoes_carregadas: self._rodar_preview()
        executar_com_loading(self.app, tarefa, fim)

    def _rodar_preview(self):
        def tarefa(): return self.service.consolidar_dados(self.transacoes_carregadas, self.hhs_carregados)
        def fim(resultado, erro):
            if not erro: prev, _ = resultado; self._renderizar_preview(prev)
        executar_com_loading(self.app, tarefa, fim)

    def consolidar(self):
        def tarefa():
            res, desc = self.service.consolidar_dados(self.transacoes_carregadas, self.hhs_carregados)
            n, a = self.service.salvar_no_banco(res)
            return n, a, desc
        def fim(resultado, erro):
            if erro: messagebox.showerror("Erro", str(erro)); return
            n, a, desc = resultado
            messagebox.showinfo("Sucesso", f"Novos: {n}\nAtualizados: {a}\nDescartados: {desc}")
            self.reiniciar_fluxo()
            if self.on_data_change: self.on_data_change()
        executar_com_loading(self.app, tarefa, fim)

    def reiniciar_fluxo(self):
        self.transacoes_carregadas = []
        self.hhs_carregados = []
        self.arquivo_transacao_atual = None
        self.btn_transacao.configure(state="normal"); self.btn_hhs.configure(state="disabled"); self.btn_consolidar.configure(state="disabled"); self.btn_cancelar.configure(state="disabled")
        for w in self.tabela_preview.winfo_children(): w.destroy()
        self.lbl_status.configure(text="Reiniciado.")
        self.atualizar_view()

    def _renderizar_preview(self, lista):
        for w in self.tabela_preview.winfo_children(): w.destroy()
        cols = ["Data", "Torneio", "Status", "Lucro"]
        for i, c in enumerate(cols): ctk.CTkLabel(self.tabela_preview, text=c, font=("Arial",12,"bold")).grid(row=0, column=i, sticky="w", padx=5)
        vinculados = [x for x in lista if x.status == "VINCULADO"]
        for idx, item in enumerate(vinculados[:30]):
            r = item.resumo
            ctk.CTkLabel(self.tabela_preview, text=r['Data'].strftime("%d/%m")).grid(row=idx+1, column=0, padx=5, sticky="w")
            ctk.CTkLabel(self.tabela_preview, text=r['Torneio'][:25]).grid(row=idx+1, column=1, padx=5, sticky="w")
            ctk.CTkLabel(self.tabela_preview, text="OK", text_color="blue").grid(row=idx+1, column=2, padx=5, sticky="w")
            ctk.CTkLabel(self.tabela_preview, text=formatar_moeda(r['Lucro'])).grid(row=idx+1, column=3, padx=5, sticky="w")