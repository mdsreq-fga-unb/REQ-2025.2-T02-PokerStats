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
        self.dados_cache = []
        
        aplicar_estilo_treeview()
        self._setup_ui()
        self.ja_carregou = False

    def ao_exibir_aba(self):
        if not self.ja_carregou:
            self.recarregar_dados()

    def _setup_ui(self):
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=0) 
        self.grid_rowconfigure(1, weight=1) 
        self.grid_rowconfigure(2, weight=0) 

        frame_top = ctk.CTkFrame(self, fg_color="transparent")
        frame_top.grid(row=0, column=0, sticky="ew", padx=10, pady=5)
        
        ctk.CTkLabel(frame_top, text="Registros Consolidados", font=("Arial", 16, "bold")).pack(side="left")
        ctk.CTkButton(frame_top, text="Atualizar", width=100, command=self.recarregar_dados).pack(side="right")

        frame_table = ctk.CTkFrame(self, fg_color="transparent")
        frame_table.grid(row=1, column=0, padx=10, pady=5, sticky="nsew")
        
        frame_table.grid_columnconfigure(0, weight=1)
        frame_table.grid_rowconfigure(0, weight=1)

        cols = ("id", "data", "nome", "buyin", "premio", "lucro")
        self.tree = ttk.Treeview(frame_table, columns=cols, show="headings", selectmode="browse")
        
        self.tree.heading("id", text="ID")
        self.tree.heading("data", text="Data")
        self.tree.heading("nome", text="Torneio")
        self.tree.heading("buyin", text="Buy-in")
        self.tree.heading("premio", text="Prêmio")
        self.tree.heading("lucro", text="Lucro")

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
        frame_footer.grid(row=2, column=0, sticky="ew", padx=10, pady=10)
        
        frame_footer.grid_propagate(False) 

        ctk.CTkLabel(frame_footer, text="Selecione uma linha para ações:", text_color="gray").pack(side="left", padx=10, pady=10)
        
        ctk.CTkButton(frame_footer, text="🗑️ Excluir", fg_color="#e74c3c", width=100, command=self._acao_excluir).pack(side="right", padx=5, pady=10)
        ctk.CTkButton(frame_footer, text="✏️ Editar", fg_color="#f1c40f", text_color="black", width=100, command=self._acao_editar).pack(side="right", padx=5, pady=10)

        self.menu_contexto = Menu(self, tearoff=0)
        self.menu_contexto.add_command(label="Editar", command=self._acao_editar)
        self.menu_contexto.add_separator()
        self.menu_contexto.add_command(label="Excluir", command=self._acao_excluir)

    def recarregar_dados(self):
        def tarefa(): return self.service.obter_historico_banco()
        def fim(dados, erro):
            if erro: messagebox.showerror("Erro", str(erro))
            else: self.dados_cache = dados; self.ja_carregou = True; self._popular_tabela()
        executar_com_loading(self.app, tarefa, fim)

    def _popular_tabela(self):
        for item in self.tree.get_children(): self.tree.delete(item)
        for item in self.dados_cache:
            lucro = item.resultado.lucro if item.resultado else 0.0
            tag_cor = "lucro_pos" if lucro > 0 else ("lucro_neg" if lucro < 0 else "normal")
            valores = (item.id, item.data_inicio.strftime("%d/%m/%Y %H:%M"), item.nome_torneio, f"${item.buy_in:.2f}", f"${item.premio:.2f}", formatar_moeda(lucro))
            self.tree.insert("", "end", values=valores, tags=(tag_cor,))
        self.tree.tag_configure("lucro_pos", foreground="#2ecc71")
        self.tree.tag_configure("lucro_neg", foreground="#e74c3c")

    def _get_id_selecionado(self):
        selected_item = self.tree.selection()
        if not selected_item: return None
        item_values = self.tree.item(selected_item[0], 'values')
        return int(item_values[0])

    def _on_double_click(self, event): self._acao_editar()
    def _on_right_click(self, event):
        row_id = self.tree.identify_row(event.y)
        if row_id: self.tree.selection_set(row_id); self.menu_contexto.post(event.x_root, event.y_root)

    def _acao_editar(self):
        db_id = self._get_id_selecionado()
        if not db_id: messagebox.showwarning("Aviso", "Selecione um registro."); return
        self._abrir_popup_edicao(db_id)

    def _acao_excluir(self):
        db_id = self._get_id_selecionado()
        if not db_id: messagebox.showwarning("Aviso", "Selecione um registro."); return
        if messagebox.askyesno("Confirmar", "Apagar este registro?"):
            def tarefa(): return self.service.deletar_registro(db_id)
            def fim(res, err):
                if err: messagebox.showerror("Erro", str(err))
                else: self.recarregar_dados(); 
                if self.on_data_change: self.on_data_change()
            executar_com_loading(self.app, tarefa, fim)

    def _abrir_popup_edicao(self, db_id):
        item = next((x for x in self.dados_cache if x.id == db_id), None)
        if not item: return
        top = ctk.CTkToplevel(self); top.title(f"Editar Registro #{db_id}"); top.geometry("400x380")
        top.transient(self.app); top.update_idletasks() 
        
        ctk.CTkLabel(top, text="Nome").pack(pady=(15,5)); e_nome = ctk.CTkEntry(top, width=300); e_nome.insert(0, item.nome_torneio); e_nome.pack()
        ctk.CTkLabel(top, text="Buy-in ($)").pack(pady=5); e_buy = ctk.CTkEntry(top); e_buy.insert(0, str(item.buy_in)); e_buy.pack()
        ctk.CTkLabel(top, text="Prêmio ($)").pack(pady=5); e_prem = ctk.CTkEntry(top); e_prem.insert(0, str(item.premio)); e_prem.pack()

        def salvar():
            try:
                dados = {"nome": e_nome.get(), "buy_in": float(e_buy.get().replace(",", ".")), "premio": float(e_prem.get().replace(",", "."))}
                def tarefa(): return self.service.atualizar_registro(db_id, dados)
                def fim(res, err):
                    top.destroy()
                    if err: messagebox.showerror("Erro", str(err))
                    else: 
                        messagebox.showinfo("Sucesso", "Atualizado!")
                        self.recarregar_dados()
                        if self.on_data_change: self.on_data_change()
                executar_com_loading(top, tarefa, fim)
            except Exception as e: messagebox.showerror("Erro", str(e))
        ctk.CTkButton(top, text="Salvar", fg_color="green", command=salvar).pack(pady=20)
        
        try: top.grab_set(); top.focus_force()
        except: pass