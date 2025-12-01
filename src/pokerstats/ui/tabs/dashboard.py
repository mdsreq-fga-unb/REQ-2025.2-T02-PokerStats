import customtkinter as ctk
from tkinter import filedialog, messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from ..utils import formatar_moeda, formatar_pct
from ..loading import executar_com_loading
from ..charts import (
    gerar_grafico_evolucao, 
    gerar_grafico_modalidades, 
    gerar_grafico_itm, 
    gerar_grafico_scatter
)
import os

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
        
        self.canvas_list = []

        self._setup_ui()
        
        self.after(100, self.atualizar_view)

    def ao_exibir_aba(self):
        self.atualizar_view()

    def _setup_ui(self):
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        self.scroll_page = ctk.CTkScrollableFrame(self, fg_color="transparent")
        self.scroll_page.grid(row=0, column=0, sticky="nsew")
        self.scroll_page.grid_columnconfigure(0, weight=1)

        frame_top = ctk.CTkFrame(self.scroll_page)
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

        self.frame_stats = ctk.CTkFrame(self.scroll_page)
        self.frame_stats.grid(row=2, column=0, padx=10, pady=5, sticky="ew")
        
        self.container_cards = ctk.CTkFrame(self.frame_stats, fg_color="transparent")
        self.container_cards.pack(fill="x", padx=5, pady=10)

        self.frame_charts_container = ctk.CTkFrame(self.scroll_page, fg_color="transparent")
        self.frame_charts_container.grid(row=3, column=0, padx=10, pady=10, sticky="ew")
        
        self.frame_charts_container.grid_columnconfigure(0, weight=1)
        self.frame_charts_container.grid_columnconfigure(1, weight=1)
        self.frame_charts_container.grid_rowconfigure(0, weight=1) 
        self.frame_charts_container.grid_rowconfigure(1, weight=1)
        
        self.chart_box_evolucao = ctk.CTkFrame(self.frame_charts_container, border_width=2, border_color="#404040", height=300)
        self.chart_box_evolucao.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
        
        self.chart_box_itm = ctk.CTkFrame(self.frame_charts_container, border_width=2, border_color="#404040", height=300)
        self.chart_box_itm.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")

        self.chart_box_modalidade = ctk.CTkFrame(self.frame_charts_container, border_width=2, border_color="#404040", height=300)
        self.chart_box_modalidade.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")

        self.chart_box_scatter = ctk.CTkFrame(self.frame_charts_container, border_width=2, border_color="#404040", height=300)
        self.chart_box_scatter.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")

        self.lbl_status = ctk.CTkLabel(self.scroll_page, text="Aguardando dados...", font=("Arial", 12))
        self.lbl_status.grid(row=1, column=0, sticky="w", padx=15, pady=(20, 20))


    def atualizar_view(self):
        relatorio = self.service.gerar_relatorio_roi_itm()
        
        stats_extra = None
        titulo_extra = "Selecione um Torneio"
        
        if self.torneio_selecionado and self.torneio_selecionado != "Selecione..." and self.torneio_selecionado != "Sem dados":
            stats_extra = self.service.calcular_stats_por_nome(self.torneio_selecionado)
            titulo_extra = self.torneio_selecionado
            if len(titulo_extra) > 20: titulo_extra = titulo_extra[:18] + "..."
        else:
            stats_extra = {"investido": 0.0, "retorno": 0.0, "lucro": 0.0, "roi": 0.0, "total_count": 0, "itm_count": 0, "itm_pct": 0.0}

        self._renderizar_cards_completos(relatorio, stats_extra, titulo_extra)
        
        dados_raw = self.service.obter_historico_banco()
        self._atualizar_graficos(dados_raw)
        self.update_idletasks()

    def _ao_selecionar_torneio(self, escolha):
        if escolha == "Selecione" or escolha == "Sem dados":
            self.torneio_selecionado = None
        else:
            self.torneio_selecionado = escolha
        self.atualizar_view()

    def _atualizar_graficos(self, dados):
        for c in self.canvas_list: 
            try: c.get_tk_widget().destroy()
            except: pass
        self.canvas_list = []

        fig1 = gerar_grafico_evolucao(dados)
        self._embed_chart(fig1, self.chart_box_evolucao)

        fig2 = gerar_grafico_itm(dados)
        self._embed_chart(fig2, self.chart_box_itm)

        fig3 = gerar_grafico_modalidades(dados)
        self._embed_chart(fig3, self.chart_box_modalidade)

        fig4 = gerar_grafico_scatter(dados)
        self._embed_chart(fig4, self.chart_box_scatter)

    def _embed_chart(self, fig, parent):
        fig.tight_layout()
        canvas = FigureCanvasTkAgg(fig, master=parent)
        canvas.draw()
        widget = canvas.get_tk_widget()
        widget.pack(fill="both", expand=True, padx=2, pady=2)
        self.canvas_list.append(canvas)

    def _renderizar_cards_completos(self, relatorio, stats_extra, titulo_extra):
        for w in self.container_cards.winfo_children(): w.destroy()
        
        cols = 5
        for i in range(cols): self.container_cards.grid_columnconfigure(i, weight=1)

        nomes = self.service.obter_nomes_torneios()
        valores_combo = ["Selecione"] + nomes if nomes else ["Selecione"]
        
        self.combo_torneios = ctk.CTkComboBox(
            self.container_cards, 
            values=valores_combo,
            command=self._ao_selecionar_torneio,
            height=24,
            width=140,
            font=("Arial", 11)
        )
        if self.torneio_selecionado and self.torneio_selecionado in valores_combo:
            self.combo_torneios.set(self.torneio_selecionado)
        else:
            self.combo_torneios.set("Selecione")
            
        self.combo_torneios.grid(row=0, column=4, padx=15, pady=(0, 5), sticky="ew")

        ordem = ["Geral", "MTT", "Sit & Go", "Outros"]
        idx = 0
        
        for key in ordem:
            if key in relatorio:
                self._criar_card(idx, key, relatorio[key], padx=5)
            idx += 1
        
        self._criar_card(idx, titulo_extra, stats_extra, destaque_titulo=True, padx=5)

    def _criar_card(self, col, titulo, dados, destaque_titulo=False, padx=5):
        frame = ctk.CTkFrame(self.container_cards, border_width=2, border_color="#404040")
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
            caminhos_processados = []
            if res['duplicados'] > 0:
                if not messagebox.askyesno("Duplicidade", f"{res['duplicados']} registros existem. Atualizar?"): return
            if res['dados']:
                self.buffer_transacoes.extend(res['dados'])
                self.arquivos_importados.update(res['caminhos'])
                caminhos_processados = res['caminhos']
            if caminhos_processados:
                self._notificar_adicao(caminhos_processados, "Transação")
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
            dados = self.service.processar_hhs(novos)
            return {"dados": dados, "caminhos": novos}  
        def fim(res, err):
            if err: messagebox.showerror("Erro", str(err)); return
            if not res: return
            dados, _ = res['dados']  
            caminhos_processados = []
            if dados:
                self.buffer_hhs.extend(dados)
                self.arquivos_importados.update(res['caminhos'])
                caminhos_processados = res['caminhos']  
            if caminhos_processados:  
                self._notificar_adicao(caminhos_processados, "Hand History")
            self._atualizar_ui_fila()
        executar_com_loading(self.app, tarefa, fim)

    def _notificar_adicao(self, caminhos_processados: list, tipo_dado: str):
        qtd_sucesso = len(caminhos_processados)
        if qtd_sucesso == 0:
            self.lbl_status.configure(text=f"Nenhum arquivo de {tipo_dado} válido foi adicionado.")
            return

        primeiro_arquivo = os.path.basename(caminhos_processados[0])
        
        if qtd_sucesso == 1:
            texto_status = f"✅ {tipo_dado}: '{primeiro_arquivo}' adicionado à fila."
        else:
            texto_status = f"✅ {tipo_dado}: {qtd_sucesso} arquivos adicionados ('{primeiro_arquivo} e mais {qtd_sucesso}')."
            
        self.lbl_status.configure(text=texto_status, text_color="#2ecc71")
        self.after(5000, lambda: self.lbl_status.configure(text="Aguardando dados...", text_color="gray"))
        
        self._atualizar_ui_fila()

    def _atualizar_ui_fila(self):
        self.lbl_count_tr.configure(text=f"{len(self.buffer_transacoes)} registros em fila")
        self.lbl_count_hh.configure(text=f"{len(self.buffer_hhs)} arquivos em fila")
        state = "normal" if (self.buffer_transacoes or self.buffer_hhs) else "disabled"
        self.btn_consolidar.configure(state=state)
        self.btn_limpar.configure(state=state)

    def consolidar(self):
        if not self.buffer_transacoes and not self.buffer_hhs: return
        def tarefa():
            res, desc = self.service.consolidar_dados(self.buffer_transacoes, self.buffer_hhs)
            n, a = self.service.salvar_no_banco(res)
            return n, a, desc
        def fim(res, err):
            if err: messagebox.showerror("Erro", str(err)); return
            n, a, desc = res
            mensagem = f"\n{' '*70}\n"
            mensagem += f"  Registros Novos:      {n}\n\n"
            mensagem += f"  Registros Atualizados: {a}\n\n"
            mensagem += f"  Registros Descartados: {desc}\n\n"
            messagebox.showinfo(" Processamento Concluído", mensagem)
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