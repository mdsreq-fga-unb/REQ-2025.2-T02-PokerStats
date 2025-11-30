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
        
        self.buffer_transacoes = [] 
        self.buffer_hhs = []        
        self.arquivos_importados = set()
        
        self.dados_dashboard_cache = None
        self.torneio_selecionado = None

        self._setup_ui()
        
        # Atualiza view inicial
        self.after(100, self.atualizar_view)

    def ao_exibir_aba(self):
        self.atualizar_view()

    def _setup_ui(self):
        self.grid_columnconfigure(0, weight=1)
        # 0: Botões, 1: Cards (Inclui Combo), 2: Status, 3: Preview
        self.grid_rowconfigure(3, weight=1)

        # --- 1. Painel de Controle ---
        frame_top = ctk.CTkFrame(self)
        frame_top.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        
        frame_tr = ctk.CTkFrame(frame_top, fg_color="transparent")
        frame_tr.pack(side="left", padx=10, pady=10)
        self.btn_transacao = ctk.CTkButton(frame_tr, text="Adicionar Transacoes (+)", command=self.add_transacoes)
        self.btn_transacao.pack(pady=2)
        self.lbl_count_tr = ctk.CTkLabel(frame_tr, text="0 registros em fila", font=("Arial", 11), text_color="gray")
        self.lbl_count_tr.pack()

        frame_hh = ctk.CTkFrame(frame_top, fg_color="transparent")
        frame_hh.pack(side="left", padx=10, pady=10)
        self.btn_hhs = ctk.CTkButton(frame_hh, text="Adicionar Hand History (+)", fg_color="green", command=self.add_hhs)
        self.btn_hhs.pack(pady=2)
        self.lbl_count_hh = ctk.CTkLabel(frame_hh, text="0 arquivos em fila", font=("Arial", 11), text_color="gray")
        self.lbl_count_hh.pack()

        frame_actions = ctk.CTkFrame(frame_top, fg_color="transparent")
        frame_actions.pack(side="right", padx=10, pady=10)
        self.btn_consolidar = ctk.CTkButton(frame_actions, text="Processar Dados", fg_color="orange", command=self.consolidar, state="disabled")
        self.btn_consolidar.pack(pady=5)
        self.btn_limpar = ctk.CTkButton(frame_actions, text="Cancelar", fg_color="#c0392b", width=80, command=self.limpar_fila, state="disabled")
        self.btn_limpar.pack()

        # --- 2. Área de Dashboard (Combo + Cards juntos) ---
        # Removemos o frame_filter separado. Tudo fica dentro do frame_stats/container_cards
        self.frame_stats = ctk.CTkFrame(self)
        self.frame_stats.grid(row=1, column=0, padx=10, pady=5, sticky="ew")
        
        # Container principal do Grid de Cards
        self.container_cards = ctk.CTkFrame(self.frame_stats, fg_color="transparent")
        self.container_cards.pack(fill="x", padx=5, pady=10)

        # --- 3. Status ---
        self.lbl_status = ctk.CTkLabel(self, text="Aguardando dados...", font=("Arial", 12))
        self.lbl_status.grid(row=2, column=0, sticky="w", padx=15)

        # --- 4. Preview ---
        self.tabela_preview = ctk.CTkScrollableFrame(self, label_text="Previa do que sera salvo")
        self.tabela_preview.grid(row=3, column=0, padx=10, pady=5, sticky="nsew")
        self.tabela_preview.grid_columnconfigure((0,1,2,3), weight=1)

    # --- Lógica de View ---

    def atualizar_view(self):
        relatorio = self.service.gerar_relatorio_roi_itm()
        
        stats_extra = None
        titulo_extra = "SELECAO"
        
        if self.torneio_selecionado and self.torneio_selecionado != "Selecione..." and self.torneio_selecionado != "Sem dados":
            stats_extra = self.service.calcular_stats_por_nome(self.torneio_selecionado)
            titulo_extra = self.torneio_selecionado
            if len(titulo_extra) > 20: titulo_extra = titulo_extra[:18] + "..."
        else:
            stats_extra = {"investido": 0.0, "retorno": 0.0, "lucro": 0.0, "roi": 0.0, "total_count": 0, "itm_count": 0, "itm_pct": 0.0}

        self._renderizar_cards_completos(relatorio, stats_extra, titulo_extra)
        self.update_idletasks()

    def _ao_selecionar_torneio(self, escolha):
        if escolha == "Selecione..." or escolha == "Sem dados":
            self.torneio_selecionado = None
        else:
            self.torneio_selecionado = escolha
        self.atualizar_view()

    def _renderizar_cards_completos(self, relatorio, stats_extra, titulo_extra):
        # Limpa tudo para redesenhar alinhado
        for w in self.container_cards.winfo_children(): w.destroy()
        
        # Configura 5 colunas IGUAIS com ESPAÇAMENTO
        cols = 5
        for i in range(cols): 
            self.container_cards.grid_columnconfigure(i, weight=1)

        # --- A. Renderiza o ComboBox (Linha 0, Coluna 4 - Acima do 5º Card) ---
        nomes = self.service.obter_nomes_torneios()
        valores_combo = nomes if nomes else ["Sem dados"]
        
        self.combo_torneios = ctk.CTkComboBox(
            self.container_cards, 
            values=valores_combo,
            command=self._ao_selecionar_torneio,
            height=24,
            width=140, # Largura reduzida para casar com o card
            font=("Arial", 11)
        )
        # Define valor atual
        if self.torneio_selecionado and self.torneio_selecionado in valores_combo:
            self.combo_torneios.set(self.torneio_selecionado)
        else:
            self.combo_torneios.set("Selecione...")
            
        # Posiciona exatamente na coluna 4
        self.combo_torneios.grid(row=0, column=4, padx=15, pady=(0, 5), sticky="ew")

        # --- B. Renderiza os Cards (Linha 1) ---
        ordem = ["Geral", "MTT", "Sit & Go", "Outros"]
        idx = 0
        
        # Cards Fixos
        for key in ordem:
            if key in relatorio:
                # padx=15 garante a separação bem definida
                self._criar_card(idx, key, relatorio[key], padx=15)
            idx += 1
        
        # Card Dinâmico (5º Elemento)
        self._criar_card(idx, titulo_extra, stats_extra, destaque_titulo=True, padx=15)

    def _criar_card(self, col, titulo, dados, destaque_titulo=False, padx=10):
        frame = ctk.CTkFrame(self.container_cards)
        # Cards ficam na linha 1 (abaixo do combo que está na linha 0, coluna 4)
        frame.grid(row=1, column=col, padx=padx, sticky="ew")
        
        cor_val = "#2ecc71" if dados['lucro'] > 0 else ("#e74c3c" if dados['lucro'] < 0 else "gray")
        cor_tit = "#3498db" if destaque_titulo else "gray"
        
        ctk.CTkLabel(frame, text=titulo.upper(), font=("Arial", 11, "bold"), text_color=cor_tit).pack(pady=(8,0))
        
        ctk.CTkLabel(frame, text=formatar_pct(dados['roi']), font=("Arial", 22, "bold"), text_color=cor_val).pack()
        ctk.CTkLabel(frame, text="ROI", font=("Arial", 9), text_color="gray").pack()
        
        ctk.CTkLabel(frame, text=f"Lucro: {formatar_moeda(dados['lucro'])}", font=("Arial", 12), text_color=cor_val).pack(pady=(4,0))
        
        txt_itm = f"{dados['itm_pct']:.1f}% ({dados['itm_count']}/{dados['total_count']})"
        ctk.CTkLabel(frame, text=f"ITM: {txt_itm}", font=("Arial", 11, "bold")).pack()
        
        ctk.CTkLabel(frame, text=f"Inv: {formatar_moeda(dados['investido'])}", font=("Arial", 10)).pack(pady=(2,10))

    # --- MÉTODOS DE IMPORTAÇÃO (MANTIDOS IGUAIS) ---
    def add_transacoes(self):
        caminhos = filedialog.askopenfilenames(parent=self, title="Transacoes", filetypes=[("Excel/CSV", "*.xlsx *.xls *.csv")])
        if not caminhos: return
        def tarefa():
            novos = [c for c in caminhos if c not in self.arquivos_importados]
            if not novos: return None
            dados, erros = self.service.ler_lote_transacoes(novos)
            duplicados = self.service.verificar_duplicidade(dados) if dados else 0
            return {"dados": dados, "erros": erros, "caminhos": novos, "duplicados": duplicados}
        def fim(res, err):
            if err: messagebox.showerror("Erro", str(err)); return
            if not res: return
            if res['duplicados'] > 0:
                if not messagebox.askyesno("Duplicidade", f"{res['duplicados']} registros existem. Atualizar?"): return
            if res['dados']:
                self.buffer_transacoes.extend(res['dados'])
                self.arquivos_importados.update(res['caminhos'])
            self._atualizar_ui_fila()
        executar_com_loading(self.app, tarefa, fim)

    def add_hhs(self):
        if not self.buffer_transacoes and not self.service.obter_historico_banco():
            messagebox.showwarning("Aviso", "Adicione transacoes primeiro."); return
        caminhos = filedialog.askopenfilenames(parent=self, title="Hand History", filetypes=[("Texto", "*.txt")])
        if not caminhos: return
        def tarefa():
            novos = [c for c in caminhos if c not in self.arquivos_importados]
            if not novos: return None
            return self.service.processar_hhs(novos)
        def fim(res, err):
            if err: messagebox.showerror("Erro", str(err)); return
            if not res: return
            dados, _ = res
            if dados:
                self.buffer_hhs.extend(dados)
                self.arquivos_importados.update(caminhos)
            self._atualizar_ui_fila()
        executar_com_loading(self.app, tarefa, fim)

    def _atualizar_ui_fila(self):
        self.lbl_count_tr.configure(text=f"{len(self.buffer_transacoes)} registros em fila")
        self.lbl_count_hh.configure(text=f"{len(self.buffer_hhs)} arquivos em fila")
        state = "normal" if (self.buffer_transacoes or self.buffer_hhs) else "disabled"
        self.btn_consolidar.configure(state=state)
        self.btn_limpar.configure(state=state)
        if self.buffer_transacoes or self.buffer_hhs:
            self.configure(cursor="watch"); self.update()
            prev, _ = self.service.consolidar_dados(self.buffer_transacoes, self.buffer_hhs)
            self._renderizar_preview(prev)
            self.configure(cursor="")
        else: self._renderizar_preview([])

    def consolidar(self):
        if not self.buffer_transacoes and not self.buffer_hhs: return
        def tarefa():
            res, desc = self.service.consolidar_dados(self.buffer_transacoes, self.buffer_hhs)
            n, a = self.service.salvar_no_banco(res)
            return n, a, desc
        def fim(res, err):
            if err: messagebox.showerror("Erro", str(err)); return
            n, a, desc = res
            messagebox.showinfo("Sucesso", f"Novos: {n}\nAtualizados: {a}\nDescartados: {desc}")
            self.limpar_fila()
            self.atualizar_view()
            if self.on_data_change: self.on_data_change()
        executar_com_loading(self.app, tarefa, fim)

    def limpar_fila(self):
        self.buffer_transacoes = []
        self.buffer_hhs = []
        self.arquivos_importados.clear()
        self._atualizar_ui_fila()

    def reiniciar_fluxo(self):
        self.limpar_fila()
        self.atualizar_view()

    def _renderizar_preview(self, lista):
        for w in self.tabela_preview.winfo_children(): w.destroy()
        cols = ["Data", "Torneio", "Status", "Lucro"]
        for i, c in enumerate(cols): ctk.CTkLabel(self.tabela_preview, text=c, font=("Arial",12,"bold")).grid(row=0, column=i, sticky="w", padx=5)
        to_show = [x for x in lista if x.status == "VINCULADO"] + [x for x in lista if x.status != "VINCULADO"]
        for idx, item in enumerate(to_show[:50]):
            r = item.resumo
            ctk.CTkLabel(self.tabela_preview, text=r['Data'].strftime("%d/%m")).grid(row=idx+1, column=0, padx=5, sticky="w")
            ctk.CTkLabel(self.tabela_preview, text=r['Torneio'][:25]).grid(row=idx+1, column=1, padx=5, sticky="w")
            cor = "blue" if r['Status'] == "VINCULADO" else "gray"
            ctk.CTkLabel(self.tabela_preview, text=r['Status'], text_color=cor, font=("Arial", 10)).grid(row=idx+1, column=2, padx=5, sticky="w")
            ctk.CTkLabel(self.tabela_preview, text=formatar_moeda(r['Lucro'])).grid(row=idx+1, column=3, padx=5, sticky="w")