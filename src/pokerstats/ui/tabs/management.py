import customtkinter as ctk
from tkinter import ttk, Menu, messagebox
from ..utils import formatar_moeda
from ..loading import executar_com_loading
from ..styles import aplicar_estilo_treeview

class ManagementTab(ctk.CTkFrame):
    def __init__(self, master, service, update_callback, app_instance):
        super().__init__(master)
        self.service = service
        self.on_data_change = update_callback
        self.app = app_instance
        
        self.dados_banco = [] 
        self.dados_exibidos = []
        
        self.coluna_sort = "ID"
        self.sort_reverse = False 
        self.ja_carregou = False
        
        aplicar_estilo_treeview()
        self._setup_ui()

    def ao_exibir_aba(self):
        self._aplicar_tema_treeview()
        self.recarregar_dados()

    def _setup_ui(self):
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1) 
        frame_header = ctk.CTkFrame(self, fg_color="transparent")
        frame_header.grid(row=0, column=0, sticky="ew", padx=10, pady=(10, 0))
        
        ctk.CTkLabel(frame_header, text="Gerenciar Registros", font=("Arial", 18, "bold")).pack(side="left")
        
        ctk.CTkButton(frame_header, text="⚠️ Apagar Todos os Registros", fg_color="#c0392b", hover_color="#962d22", 
                      width=150, command=self._acao_apagar_tudo).pack(side="right")

        frame_tools = ctk.CTkFrame(self)
        frame_tools.grid(row=1, column=0, sticky="ew", padx=10, pady=10)
        
        ctk.CTkLabel(frame_tools, text="🔍 Buscar:").pack(side="left", padx=10)
        
        self.entry_busca = ctk.CTkEntry(frame_tools, width=250, placeholder_text="Digite para filtrar...")
        self.entry_busca.pack(side="left", padx=5)
        self.entry_busca.bind("<KeyRelease>", self._filtrar_dados) 
        
        self.combo_coluna = ctk.CTkComboBox(frame_tools, values=["Todos", "Torneio", "ID", "Data"], width=100)
        self.combo_coluna.set("Todos")
        self.combo_coluna.pack(side="left", padx=5)
        
        ctk.CTkButton(frame_tools, text=" Recarregar", width=100, command=self.recarregar_dados).pack(side="right", padx=10)

        frame_table = ctk.CTkFrame(self, fg_color="transparent")
        frame_table.grid(row=2, column=0, padx=10, pady=5, sticky="nsew")
        frame_table.grid_columnconfigure(0, weight=1)
        frame_table.grid_rowconfigure(0, weight=1)

        cols = ("id", "data", "nome", "buyin", "premio", "lucro")
        self.tree = ttk.Treeview(frame_table, columns=cols, show="headings", selectmode="extended")
        
        self.tree.heading("id", text="ID", command=lambda: self._ordenar_coluna("ID"))
        self.tree.heading("data", text="Data", command=lambda: self._ordenar_coluna("Data"))
        self.tree.heading("nome", text="Torneio", command=lambda: self._ordenar_coluna("Torneio"))
        self.tree.heading("buyin", text="Buy-in", command=lambda: self._ordenar_coluna("Buy-in"))
        self.tree.heading("premio", text="Prêmio", command=lambda: self._ordenar_coluna("Prêmio"))
        self.tree.heading("lucro", text="Lucro", command=lambda: self._ordenar_coluna("Lucro"))

        self.tree.column("id", width=50, anchor="center")
        self.tree.column("data", width=120, anchor="center")
        self.tree.column("nome", width=300, anchor="w")
        self.tree.column("buyin", width=100, anchor="e")
        self.tree.column("premio", width=100, anchor="e")
        self.tree.column("lucro", width=120, anchor="e")

        scrollbar = ttk.Scrollbar(frame_table, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        
        self.tree.grid(row=0, column=0, sticky="nsew")
        scrollbar.grid(row=0, column=1, sticky="ns")

        self.tree.bind("<Double-1>", self._on_double_click)
        self.tree.bind("<Button-3>", self._on_right_click)

        frame_footer = ctk.CTkFrame(self, height=50)
        frame_footer.grid(row=3, column=0, sticky="ew", padx=10, pady=10)
        frame_footer.grid_propagate(False)

        ctk.CTkLabel(frame_footer, text="Selecione linhas com Ctrl ou Shift", text_color="gray").pack(side="left", padx=10)
        
        ctk.CTkButton(frame_footer, text="🗑️ Excluir Selecionados", fg_color="#e74c3c", width=150, command=self._acao_excluir_selecionados).pack(side="right", padx=5)
        ctk.CTkButton(frame_footer, text="✏️ Editar (Único)", fg_color="#f1c40f", text_color="black", width=150, command=self._acao_editar).pack(side="right", padx=5)

        self.menu_contexto = Menu(self, tearoff=0)
        self.menu_contexto.add_command(label="Editar", command=self._acao_editar)
        self.menu_contexto.add_separator()
        self.menu_contexto.add_command(label="Excluir Selecionados", command=self._acao_excluir_selecionados)

    def recarregar_dados(self):
        def tarefa():
            return self.service.obter_historico_banco()
        
        def fim(dados, erro):
            if erro:
                messagebox.showerror("Erro", str(erro))
            else:
                self.dados_banco = dados
                self.ja_carregou = True
                self._filtrar_dados() 
        
        executar_com_loading(self.app, tarefa, fim)

    def atualizar_tabela_visual(self):
        """Chamado pelo Main para refresh leve (sem ir ao banco se já tiver cache)"""
        if self.ja_carregou:
            self._filtrar_dados()
        else:
            self.recarregar_dados()

    def _filtrar_dados(self, event=None):
        termo = self.entry_busca.get().lower()
        coluna_filtro = self.combo_coluna.get()
        
        if not termo:
            self.dados_exibidos = self.dados_banco.copy()
        else:
            filtrados = []
            for item in self.dados_banco:
                match = False
                
                texto_id = str(item.id)
                texto_nome = (item.nome_torneio or "").lower()
                texto_data = item.data_inicio.strftime("%d/%m/%Y")
                
                if coluna_filtro == "Todos":
                    if termo in texto_nome or termo in texto_id or termo in texto_data: match = True
                elif coluna_filtro == "Torneio" and termo in texto_nome: match = True
                elif coluna_filtro == "ID" and termo in texto_id: match = True
                elif coluna_filtro == "Data" and termo in texto_data: match = True
                
                if match: filtrados.append(item)
            
            self.dados_exibidos = filtrados
        
        self._aplicar_ordenacao()
        self._popular_tabela()

    def _ordenar_coluna(self, coluna):
        if self.coluna_sort == coluna:
            self.sort_reverse = not self.sort_reverse
        else:
            self.coluna_sort = coluna
            self.sort_reverse = True if coluna in ["Data", "Lucro", "Prêmio", "Buy-in"] else False
            
        self._aplicar_ordenacao()
        self._popular_tabela()

    def _aplicar_ordenacao(self):
        mapa = {
            "ID": lambda x: x.id, "Data": lambda x: x.data_inicio,
            "Torneio": lambda x: (x.nome_torneio or "").lower(),
            "Buy-in": lambda x: x.buy_in, "Prêmio": lambda x: x.premio,
            "Lucro": lambda x: x.resultado.lucro if x.resultado else 0.0
        }
        chave = mapa.get(self.coluna_sort)
        if chave:
            self.dados_exibidos.sort(key=chave, reverse=self.sort_reverse)
            
            for col in self.tree["columns"]:
                base_text = {
                    "id": "ID", "data": "Data", "nome": "Torneio", 
                    "buyin": "Buy-in", "premio": "Prêmio", "lucro": "Lucro"
                }.get(col, col)
                
                if self.coluna_sort == base_text:
                    seta = "▼" if self.sort_reverse else "▲"
                    self.tree.heading(col, text=f"{base_text} {seta}")
                else:
                    self.tree.heading(col, text=base_text)

    def _popular_tabela(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        for item in self.dados_exibidos:
            lucro = item.resultado.lucro if item.resultado else 0.0
            tag_cor = "lucro_pos" if lucro > 0 else ("lucro_neg" if lucro < 0 else "normal")
            
            valores = (
                item.id,
                item.data_inicio.strftime("%d/%m/%Y %H:%M"),
                item.nome_torneio,
                f"${item.buy_in:.2f}",
                f"${item.premio:.2f}",
                formatar_moeda(lucro)
            )
            self.tree.insert("", "end", values=valores, tags=(tag_cor,))

        self.tree.tag_configure("lucro_pos", foreground="#2ecc71")
        self.tree.tag_configure("lucro_neg", foreground="#e74c3c")

    def _get_ids_selecionados(self):
        selected_items = self.tree.selection()
        ids = []
        for item in selected_items:
            val = self.tree.item(item, 'values')
            ids.append(int(val[0]))
        return ids

    def _on_double_click(self, event):
        self._acao_editar()

    def _on_right_click(self, event):
        row_id = self.tree.identify_row(event.y)
        if row_id:
            if row_id not in self.tree.selection():
                self.tree.selection_set(row_id)
            self.menu_contexto.post(event.x_root, event.y_root)

    def _acao_editar(self):
        ids = self._get_ids_selecionados()
        if len(ids) == 0:
            messagebox.showwarning("Aviso", "Selecione um registro.")
        elif len(ids) > 1:
            messagebox.showwarning("Aviso", "Selecione apenas UM registro para editar.")
        else:
            self._abrir_popup_edicao(ids[0])

    def _acao_excluir_selecionados(self):
        ids = self._get_ids_selecionados()
        if not ids:
            messagebox.showwarning("Aviso", "Nenhum registro selecionado.")
            return

        qtd = len(ids)
        msg = f"Tem certeza que deseja apagar {qtd} registro(s)?"
        if qtd > 1:
            msg += "\n\n⚠️ Esta ação não pode ser desfeita!"

        if messagebox.askyesno("Confirmar Exclusão", msg):
            if qtd > 5:
                if not messagebox.askyesno("Confirmar Novamente", f"Realmente apagar {qtd} itens permanentemente?"):
                    return

            def tarefa():
                return self.service.deletar_em_lote(ids)
            
            def fim(res, err):
                if err: messagebox.showerror("Erro", str(err))
                else:
                    self.dados_banco = [x for x in self.dados_banco if x.id not in ids]
                    self._filtrar_dados() 
                    if self.on_data_change: self.on_data_change()

            executar_com_loading(self.app, tarefa, fim)

    def _acao_apagar_tudo(self):
        if not self.dados_banco:
            messagebox.showinfo("Vazio", "O banco já está vazio.")
            return

        if messagebox.askyesno("PERIGO ⚠️", "Tem certeza que deseja APAGAR TODO O BANCO DE DADOS?\n\nIsso excluirá todo o histórico importado."):
            if messagebox.askyesno("Confirmação Final", "Apagar TODOS os registros?"):
                
                def tarefa():
                    return self.service.limpar_banco_completo()
                
                def fim(res, err):
                    if err: messagebox.showerror("Erro", str(err))
                    else:
                        self.dados_banco = []
                        self._filtrar_dados()
                        if self.on_data_change: self.on_data_change()
                        messagebox.showinfo("Limpo", "Todos os registros apagados com sucesso.")

                executar_com_loading(self.app, tarefa, fim)

    def _abrir_popup_edicao(self, db_id):
        item = next((x for x in self.dados_banco if x.id == db_id), None)
        if not item: return

        top = ctk.CTkToplevel(self); top.title(f"Editar #{db_id}"); top.geometry("400x380")
        top.transient(self.app); top.update_idletasks()
        
        ctk.CTkLabel(top, text="Nome").pack(pady=(15,5)); e_nome = ctk.CTkEntry(top, width=300); e_nome.insert(0, item.nome_torneio); e_nome.pack()
        ctk.CTkLabel(top, text="Buy-in").pack(pady=5); e_buy = ctk.CTkEntry(top); e_buy.insert(0, str(item.buy_in)); e_buy.pack()
        ctk.CTkLabel(top, text="Prêmio").pack(pady=5); e_prem = ctk.CTkEntry(top); e_prem.insert(0, str(item.premio)); e_prem.pack()

        def salvar():
            try:
                dados = {"nome": e_nome.get(), "buy_in": float(e_buy.get().replace(",", ".")), "premio": float(e_prem.get().replace(",", "."))}
                def tarefa(): return self.service.atualizar_registro(db_id, dados)
                def fim(res, err):
                    top.destroy()
                    if err: messagebox.showerror("Erro", str(err))
                    else:
                        messagebox.showinfo("Sucesso", "Atualizado!")
                        self._filtrar_dados()
                        if self.on_data_change: self.on_data_change()
                executar_com_loading(top, tarefa, fim)
            except Exception as e: messagebox.showerror("Erro", str(e))
        ctk.CTkButton(top, text="Salvar", command=salvar).pack(pady=20)
        try: 
            top.grab_set(); 
            top.focus_force(); 
        except: 
            pass
        
    def _aplicar_tema_treeview(self):
        tema = ctk.get_appearance_mode()
        estilo = ttk.Style()

        estilo.theme_use("default")

        if tema == "Dark":
            estilo.configure(
                "Treeview",
                background="#2a2d2e",
                foreground="#ffffff",
                fieldbackground="#2a2d2e",
                bordercolor="#2a2d2e",
                rowheight=26
            )
            estilo.map(
                "Treeview",
                background=[("selected", "#3a3f47")]
            )
            estilo.configure(
                "Treeview.Heading",
                background="#2f3234",
                foreground="#ffffff"
            )
        else:
            estilo.configure(
                "Treeview",
                background="#ffffff",
                foreground="#000000",
                fieldbackground="#ffffff",
                bordercolor="#d9d9d9",
                rowheight=26
            )
            estilo.map(
                "Treeview",
                background=[("selected", "#cce6ff")]
            )
            estilo.configure(
                "Treeview.Heading",
                background="#f0f0f0",
                foreground="#000000"
            )