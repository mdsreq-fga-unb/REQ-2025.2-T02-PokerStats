import customtkinter as ctk
from tkinter import messagebox
import math
from ..utils import formatar_moeda
from ..loading import executar_com_loading

class ManagementTab(ctk.CTkFrame):
    def __init__(self, master, service, update_callback, app_instance):
        super().__init__(master)
        self.service = service
        self.on_data_change = update_callback
        self.app = app_instance
        
        self.coluna_sort = "ID"
        self.sort_reverse = False
        
        self.pagina_atual = 1
        self.itens_por_pagina = 50
        self.total_paginas = 1
        self.todos_dados_cache = []

        self._setup_ui()

    def _setup_ui(self):
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=0)

        frame_top = ctk.CTkFrame(self, fg_color="transparent")
        frame_top.grid(row=0, column=0, sticky="ew", padx=10, pady=5)
        ctk.CTkButton(frame_top, text="🔄 Atualizar", width=100, command=self.iniciar_carregamento).pack(side="right")

        self.tabela_full = ctk.CTkScrollableFrame(self, label_text="Gerenciar Registros")
        self.tabela_full.grid(row=1, column=0, padx=10, pady=5, sticky="nsew")
        
        self.tabela_full.grid_columnconfigure(0, weight=0, minsize=50)
        self.tabela_full.grid_columnconfigure(1, weight=0, minsize=100)
        self.tabela_full.grid_columnconfigure(2, weight=1)
        self.tabela_full.grid_columnconfigure(3, weight=0, minsize=100)
        self.tabela_full.grid_columnconfigure(4, weight=0, minsize=100)
        self.tabela_full.grid_columnconfigure(5, weight=0, minsize=120)
        self.tabela_full.grid_columnconfigure(6, weight=0, minsize=80)

        self.frame_footer = ctk.CTkFrame(self, fg_color="transparent")
        self.frame_footer.grid(row=2, column=0, sticky="ew", padx=10, pady=5)
        
        self.btn_ant = ctk.CTkButton(self.frame_footer, text="< Anterior", width=80, command=self.pagina_anterior)
        self.btn_ant.pack(side="left")
        self.lbl_paginacao = ctk.CTkLabel(self.frame_footer, text="Clique na aba para carregar.", font=("Arial", 12, "bold"))
        self.lbl_paginacao.pack(side="left", padx=20, expand=True)
        self.btn_prox = ctk.CTkButton(self.frame_footer, text="Próxima >", width=80, command=self.pagina_proxima)
        self.btn_prox.pack(side="right")

    def ao_exibir_aba(self):
        if not self.todos_dados_cache:
            self.iniciar_carregamento()

    def iniciar_carregamento(self):
        def tarefa():
            return self.service.obter_historico_banco()
        
        def fim(resultado, erro):
            if erro:
                messagebox.showerror("Erro", str(erro))
            else:
                self.todos_dados_cache = resultado
                self.pagina_atual = 1
                self.renderizar_pagina_real(self._ordenar_dados(resultado))

        executar_com_loading(self.app, tarefa, fim, close_early=False)

    def recarregar_dados(self):
        self.todos_dados_cache = self.service.obter_historico_banco()
        if self.todos_dados_cache:
             self.renderizar_pagina_real(self._ordenar_dados(self.todos_dados_cache.copy()))

    def _deletar(self, db_id):
        if messagebox.askyesno("Confirmar", "Apagar?"):
            def tarefa(): return self.service.deletar_registro(db_id)
            
            def fim(res, err):
                if err: messagebox.showerror("Erro", str(err))
                else: 
                    self.iniciar_carregamento()
                    if self.on_data_change: self.on_data_change()
            
            executar_com_loading(self.app, tarefa, fim, close_early=True)

    def _popup_editar(self, db_id):
        item = next((x for x in self.todos_dados_cache if x.id == db_id), None)
        if not item: return
        top = ctk.CTkToplevel(self)
        top.geometry("400x380")
        top.after(100, lambda: (top.grab_set(), top.focus_force()))
        
        ctk.CTkLabel(top, text="Nome").pack(); e_nome = ctk.CTkEntry(top, width=300); e_nome.insert(0, item.nome_torneio); e_nome.pack()
        ctk.CTkLabel(top, text="Buy-in").pack(); e_buy = ctk.CTkEntry(top); e_buy.insert(0, str(item.buy_in)); e_buy.pack()
        ctk.CTkLabel(top, text="Prêmio").pack(); e_prem = ctk.CTkEntry(top); e_prem.insert(0, str(item.premio)); e_prem.pack()

        def salvar():
            try:
                dados = {"nome": e_nome.get(), "buy_in": float(e_buy.get().replace(",", ".")), "premio": float(e_prem.get().replace(",", "."))}
                def tarefa(): return self.service.atualizar_registro(db_id, dados)
                
                def fim(res, err):
                    if err: 
                        messagebox.showerror("Erro", str(err))
                    else:
                        top.destroy()
                        messagebox.showinfo("Sucesso", "Atualizado!")
                        self.iniciar_carregamento()
                        if self.on_data_change: self.on_data_change()

                executar_com_loading(top, tarefa, fim, close_early=True)
            except Exception as e: messagebox.showerror("Erro", str(e))
        
        ctk.CTkButton(top, text="Salvar", command=salvar).pack(pady=20)

    
    def renderizar_pagina_com_loading(self):
        def tarefa_fake(): return self._ordenar_dados(self.todos_dados_cache.copy())
        def fim(dados_ordenados, erro): self.renderizar_pagina_real(dados_ordenados)
        executar_com_loading(self.app, tarefa_fake, fim, close_early=False)

    def pagina_anterior(self):
        if self.pagina_atual > 1: self.pagina_atual -= 1; self.renderizar_pagina_com_loading()
    def pagina_proxima(self):
        if self.pagina_atual < self.total_paginas: self.pagina_atual += 1; self.renderizar_pagina_com_loading()
    
    def _ao_clicar_cabecalho(self, coluna):
        if self.coluna_sort == coluna: self.sort_reverse = not self.sort_reverse
        else: self.coluna_sort = coluna; self.sort_reverse = True if coluna in ["Data", "Lucro", "Prêmio"] else False
        self.renderizar_pagina_com_loading()

    def _ordenar_dados(self, dados):
        mapa = {"ID": lambda x: x.id, "Data": lambda x: x.data_inicio, "Torneio": lambda x: (x.nome_torneio or "").lower(), "Buy-in": lambda x: x.buy_in, "Prêmio": lambda x: x.premio, "Lucro": lambda x: x.resultado.lucro if x.resultado else 0.0}
        chave = mapa.get(self.coluna_sort)
        if chave: dados.sort(key=chave, reverse=self.sort_reverse)
        return dados

    def renderizar_pagina_real(self, dados_ordenados):
        self.total_paginas = math.ceil(len(dados_ordenados) / self.itens_por_pagina) or 1
        if self.pagina_atual > self.total_paginas: self.pagina_atual = self.total_paginas
        inicio = (self.pagina_atual - 1) * self.itens_por_pagina
        dados_pagina = dados_ordenados[inicio : inicio + self.itens_por_pagina]

        self.lbl_paginacao.configure(text=f"Página {self.pagina_atual} de {self.total_paginas} (Total: {len(dados_ordenados)})")
        self.btn_ant.configure(state="normal" if self.pagina_atual > 1 else "disabled")
        self.btn_prox.configure(state="normal" if self.pagina_atual < self.total_paginas else "disabled")

        for w in self.tabela_full.winfo_children(): w.destroy()

        headers = ["ID", "Data", "Torneio", "Buy-in", "Prêmio", "Lucro", "Ações"]
        for i, h in enumerate(headers):
            txt = f"{h} {'▼' if self.sort_reverse else '▲'}" if h == self.coluna_sort else h
            cmd = lambda c=h: self._ao_clicar_cabecalho(c)
            if h != "Ações": ctk.CTkButton(self.tabela_full, text=txt, font=("Arial",12,"bold"), fg_color="transparent", hover_color="#404040", command=cmd).grid(row=0, column=i, sticky="ew")
            else: ctk.CTkLabel(self.tabela_full, text=h, font=("Arial",12,"bold")).grid(row=0, column=i, sticky="ew")

        for idx, item in enumerate(dados_pagina):
            row = idx + 1
            lucro = item.resultado.lucro if item.resultado else 0.0
            cor = "#2ecc71" if lucro > 0 else ("#e74c3c" if lucro < 0 else "white")
            ctk.CTkLabel(self.tabela_full, text=str(item.id)).grid(row=row, column=0, padx=2, pady=2)
            ctk.CTkLabel(self.tabela_full, text=item.data_inicio.strftime("%d/%m/%Y")).grid(row=row, column=1, padx=2, pady=2)
            ctk.CTkLabel(self.tabela_full, text=item.nome_torneio[:40]+"...", anchor="w").grid(row=row, column=2, padx=5, sticky="ew")
            ctk.CTkLabel(self.tabela_full, text=f"${item.buy_in:.2f}", font=("Consolas",12)).grid(row=row, column=3, padx=5, sticky="e")
            ctk.CTkLabel(self.tabela_full, text=f"${item.premio:.2f}", font=("Consolas",12)).grid(row=row, column=4, padx=5, sticky="e")
            ctk.CTkLabel(self.tabela_full, text=formatar_moeda(lucro), text_color=cor, font=("Consolas",12,"bold")).grid(row=row, column=5, padx=5, sticky="e")
            f_acoes = ctk.CTkFrame(self.tabela_full, fg_color="transparent")
            f_acoes.grid(row=row, column=6, padx=2)
            ctk.CTkButton(f_acoes, text="✏️", width=30, fg_color="#f1c40f", text_color="black", command=lambda id=item.id: self._popup_editar(id)).pack(side="left", padx=2)
            ctk.CTkButton(f_acoes, text="🗑️", width=30, fg_color="#e74c3c", command=lambda id=item.id: self._deletar(id)).pack(side="left", padx=2)