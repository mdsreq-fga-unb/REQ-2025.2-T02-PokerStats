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

        self._setup_ui()
        self.after(100, self.atualizar_view)

    def ao_exibir_aba(self):
        self.atualizar_view()

    def _setup_ui(self):
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(3, weight=1)

        frame_top = ctk.CTkFrame(self)
        frame_top.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        
        frame_tr = ctk.CTkFrame(frame_top, fg_color="transparent")
        frame_tr.pack(side="left", padx=10, pady=10)
        
        self.btn_transacao = ctk.CTkButton(frame_tr, text=" Adicionar Transações (+)", command=self.add_transacoes)
        self.btn_transacao.pack(pady=2)
        self.lbl_count_tr = ctk.CTkLabel(frame_tr, text="0 registros em fila", font=("Arial", 11), text_color="gray")
        self.lbl_count_tr.pack()

        frame_hh = ctk.CTkFrame(frame_top, fg_color="transparent")
        frame_hh.pack(side="left", padx=10, pady=10)
        
        self.btn_hhs = ctk.CTkButton(frame_hh, text=" Adicionar Hand History (+)", fg_color="green", command=self.add_hhs)
        self.btn_hhs.pack(pady=2)
        self.lbl_count_hh = ctk.CTkLabel(frame_hh, text="0 arquivos em fila", font=("Arial", 11), text_color="gray")
        self.lbl_count_hh.pack()

        frame_actions = ctk.CTkFrame(frame_top, fg_color="transparent")
        frame_actions.pack(side="right", padx=10, pady=10)
        
        self.btn_consolidar = ctk.CTkButton(frame_actions, text=" Processar Dados", fg_color="orange", command=self.consolidar, state="disabled")
        self.btn_consolidar.pack(pady=5)
        
        self.btn_limpar = ctk.CTkButton(frame_actions, text="Cancelar", fg_color="#c0392b", width=80, command=self.limpar_fila, state="disabled")
        self.btn_limpar.pack()

        self.frame_stats = ctk.CTkFrame(self)
        self.frame_stats.grid(row=1, column=0, padx=10, pady=5, sticky="ew")
        self.container_cards = ctk.CTkFrame(self.frame_stats, fg_color="transparent")
        self.container_cards.pack(fill="x", padx=5, pady=5)

        self.tabela_preview = ctk.CTkScrollableFrame(self, label_text="Prévia do que será salvo (Match em Memória)")
        self.tabela_preview.grid(row=3, column=0, padx=10, pady=5, sticky="nsew")
        self.tabela_preview.grid_columnconfigure((0,1,2,3), weight=1)

    def add_transacoes(self):
        caminhos = filedialog.askopenfilenames(
            parent=self, 
            title="Adicionar Arquivos de Transação",
            filetypes=[("Excel/CSV", "*.xlsx *.xls *.csv")]
        )
        if not caminhos: return

        def tarefa():
            novos_caminhos = [c for c in caminhos if c not in self.arquivos_importados]
            if not novos_caminhos: return [], 0
            
            dados, erros = self.service.ler_lote_transacoes(novos_caminhos)
            return dados, erros, novos_caminhos

        def fim(resultado, erro):
            if erro: messagebox.showerror("Erro", str(erro)); return
            
            novos_dados, qtd_erros, caminhos_processados = resultado
            
            if novos_dados:
                self.buffer_transacoes.extend(novos_dados)
                self.arquivos_importados.update(caminhos_processados)
                self._atualizar_ui_fila()
            
            msg = f"{len(novos_dados)} registros adicionados à fila."
            if qtd_erros > 0: msg += f"\n({qtd_erros} arquivos falharam ou vazios)"
            
            print(msg) 

        executar_com_loading(self.app, tarefa, fim)

    def add_hhs(self):
        tem_transacoes_fila = len(self.buffer_transacoes) > 0
        
        historico_banco = self.service.obter_historico_banco()
        tem_transacoes_banco = len(historico_banco) > 0

        if not tem_transacoes_fila and not tem_transacoes_banco:
            messagebox.showwarning(
                "Ação Bloqueada", 
                "Você precisa adicionar arquivos de TRANSAÇÕES antes de adicionar Hand Histories.\n\n"
                "O sistema precisa dos dados financeiros para vincular corretamente os jogos."
            )
            return

        caminhos = filedialog.askopenfilenames(
            parent=self, 
            title="Adicionar Arquivos de Hand History",
            filetypes=[("Texto", "*.txt")]
        )
        if not caminhos: return

        def tarefa():
            novos_caminhos = [c for c in caminhos if c not in self.arquivos_importados]
            if not novos_caminhos: return [], None
            
            return self.service.processar_hhs(novos_caminhos)

        def fim(resultado, erro):
            if erro: messagebox.showerror("Erro", str(erro)); return
            
            if not resultado: return

            dados, relatorio = resultado
            
            if dados:
                self.buffer_hhs.extend(dados)
                self.arquivos_importados.update(caminhos)
                self._atualizar_ui_fila()

        executar_com_loading(self.app, tarefa, fim)

    def _atualizar_ui_fila(self):
        qtd_tr = len(self.buffer_transacoes)
        qtd_hh = len(self.buffer_hhs)
        
        self.lbl_count_tr.configure(text=f"{qtd_tr} registros em fila")
        self.lbl_count_hh.configure(text=f"{qtd_hh} arquivos em fila")
        
        tem_dados = qtd_tr > 0 or qtd_hh > 0
        state = "normal" if tem_dados else "disabled"
        
        self.btn_consolidar.configure(state=state)
        self.btn_limpar.configure(state=state)
        
        if tem_dados:
            self._rodar_preview()

    def limpar_fila(self):
        self.buffer_transacoes = []
        self.buffer_hhs = []
        self.arquivos_importados.clear()
        self._atualizar_ui_fila()
        
        for w in self.tabela_preview.winfo_children(): w.destroy()

    def _rodar_preview(self):
        def tarefa():
            return self.service.consolidar_dados(self.buffer_transacoes, self.buffer_hhs)
        
        def fim(resultado, erro):
            if not erro: 
                prev, _ = resultado
                self._renderizar_preview(prev)
        
        executar_com_loading(self.app, tarefa, fim)

    def consolidar(self):
        if not self.buffer_transacoes and not self.buffer_hhs: return

        def tarefa():
            res, desc = self.service.consolidar_dados(self.buffer_transacoes, self.buffer_hhs)
            n, a = self.service.salvar_no_banco(res)
            return n, a, desc

        def fim(resultado, erro):
            if erro: messagebox.showerror("Erro", str(erro)); return
            
            n, a, desc = resultado
            messagebox.showinfo("Sucesso", f"Importação Finalizada!\n\nNovos: {n}\nAtualizados/Vinculados: {a}\nHHs Descartados: {desc}")
            
            self.limpar_fila()
            
            self.atualizar_view()
            
            if self.on_data_change: self.on_data_change()

        executar_com_loading(self.app, tarefa, fim)


    def atualizar_view(self):
        relatorio = self.service.gerar_relatorio_roi_itm()
        self._renderizar_cards(relatorio)

    def _renderizar_cards(self, relatorio):
        for w in self.container_cards.winfo_children(): w.destroy()
        if not relatorio:
            ctk.CTkLabel(self.container_cards, text="Sem dados no banco.", text_color="gray").pack()
            return
        
        cols = len(relatorio)
        for i in range(cols): self.container_cards.grid_columnconfigure(i, weight=1)
        idx = 0
        for mod, dados in relatorio.items():
            self._criar_card(idx, mod, dados)
            idx += 1

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

    def _renderizar_preview(self, lista):
        for w in self.tabela_preview.winfo_children(): w.destroy()
        cols = ["Data", "Torneio", "Status", "Lucro"]
        for i, c in enumerate(cols): ctk.CTkLabel(self.tabela_preview, text=c, font=("Arial",12,"bold")).grid(row=0, column=i, sticky="w", padx=5)
        
        for idx, item in enumerate(lista[:50]):
            r = item.resumo
            ctk.CTkLabel(self.tabela_preview, text=r['Data'].strftime("%d/%m")).grid(row=idx+1, column=0, padx=5, sticky="w")
            ctk.CTkLabel(self.tabela_preview, text=r['Torneio'][:25]).grid(row=idx+1, column=1, padx=5, sticky="w")
            
            status_cor = "blue" if r['Status'] == "VINCULADO" else "gray"
            ctk.CTkLabel(self.tabela_preview, text=r['Status'], text_color=status_cor, font=("Arial", 10)).grid(row=idx+1, column=2, padx=5, sticky="w")
            
            ctk.CTkLabel(self.tabela_preview, text=formatar_moeda(r['Lucro'])).grid(row=idx+1, column=3, padx=5, sticky="w")