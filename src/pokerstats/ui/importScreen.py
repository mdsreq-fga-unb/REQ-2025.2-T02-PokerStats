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

        self.title("Bodog Manager - Fluxo Guiado")
        self.geometry("1000x700")
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=0)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=0)

        self.frame_top = ctk.CTkFrame(self)
        self.frame_top.grid(row=0, column=0, padx=20, pady=10, sticky="ew")
        
        self.btn_transacao = ctk.CTkButton(
            self.frame_top, 
            text="1. Carregar Transação (Único)", 
            command=self.carregar_transacao
        )
        self.btn_transacao.pack(side="left", padx=10, pady=10)

        self.btn_hhs = ctk.CTkButton(
            self.frame_top, 
            text="2. Adicionar HHs Relacionados", 
            fg_color="green", 
            command=self.carregar_hhs,
            state="disabled"
        )
        self.btn_hhs.pack(side="left", padx=10, pady=10)
        
        self.btn_consolidar = ctk.CTkButton(
            self.frame_top, 
            text="3. Processar e Finalizar", 
            fg_color="orange", 
            command=self.consolidar,
            state="disabled"
        )
        self.btn_consolidar.pack(side="left", padx=10, pady=10)

        self.btn_cancelar = ctk.CTkButton(
            self.frame_top, 
            text="Cancelar / Reiniciar", 
            fg_color="#c0392b",
            width=80,
            command=self.reiniciar_fluxo,
            state="disabled"
        )
        self.btn_cancelar.pack(side="right", padx=10, pady=10)

        self.lbl_status = ctk.CTkLabel(self, text="Aguardando arquivo de Transação...", font=("Arial", 12, "bold"))
        self.lbl_status.grid(row=1, column=0, sticky="w", padx=25, pady=(0, 5))

        self.tabela_frame = ctk.CTkScrollableFrame(self, label_text="Prévia da Consolidação")
        self.tabela_frame.grid(row=2, column=0, padx=20, pady=5, sticky="nsew")
        
        self.tabela_frame.grid_columnconfigure(0, weight=1)
        self.tabela_frame.grid_columnconfigure(1, weight=3)
        self.tabela_frame.grid_columnconfigure(2, weight=1)
        self.tabela_frame.grid_columnconfigure(3, weight=1)

        self.log_box = ctk.CTkTextbox(self, height=100, font=("Consolas", 11))
        self.log_box.grid(row=3, column=0, padx=20, pady=10, sticky="ew")
        
        self.log("Sistema pronto. Inicie carregando um arquivo de transação.")

    def log(self, texto):
        self.log_box.insert("end", texto + "\n")
        self.log_box.see("end")

    def reiniciar_fluxo(self):
        self.transacoes_carregadas = []
        self.hhs_carregados = []
        self.arquivo_transacao_atual = None
        
        self.btn_transacao.configure(state="normal")
        self.btn_hhs.configure(state="disabled")
        self.btn_consolidar.configure(state="disabled")
        self.btn_cancelar.configure(state="disabled")
        
        for widget in self.tabela_frame.winfo_children():
            widget.destroy()
            
        self.lbl_status.configure(text="Fluxo reiniciado. Aguardando Transação...")
        self.log("-" * 30)
        self.log("Fluxo reiniciado.")

    def carregar_transacao(self):
        caminho = filedialog.askopenfilename(
            parent=self,
            title="Selecione UM arquivo de Transação",
            filetypes=[("Excel/CSV", "*.xlsx *.xls *.csv")]
        )
        if not caminho: return

        self.log(f"Lendo transação: {caminho}...")
        try:
            transacoes_temp = self.service.ler_transacoes(caminho)
            
            if not transacoes_temp:
                self.log("Aviso: Nenhuma transação válida encontrada.")
                return

            qtd_total = len(transacoes_temp)
            
            qtd_existente = self.service.verificar_duplicidade(transacoes_temp)
            
            if qtd_existente > 0:
                msg = f"Atenção: {qtd_existente} das {qtd_total} transações deste arquivo JÁ EXISTEM no banco.\n\n" \
                      f"Se continuar, os dados existentes serão ATUALIZADOS.\n" \
                      f"Deseja prosseguir mesmo assim?"
                
                resposta = messagebox.askyesno("Dados Existentes", msg, parent=self)
                if not resposta:
                    self.log("Importação cancelada pelo usuário.")
                    return
                else:
                    self.log(f"Usuário optou por sobrescrever/atualizar {qtd_existente} registros.")

            self.transacoes_carregadas = transacoes_temp
            self.arquivo_transacao_atual = caminho
            
            self.log(f"Sucesso: {qtd_total} registros carregados.")
            
            self.btn_transacao.configure(state="disabled")
            self.btn_hhs.configure(state="normal")
            self.btn_consolidar.configure(state="normal")
            self.btn_cancelar.configure(state="normal")
            
            self.lbl_status.configure(text=f"Arquivo Ativo: {caminho.split('/')[-1]} ({qtd_total} linhas)")
            self.log("Agora adicione os HHs correspondentes ou clique em Finalizar.")
            
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    def carregar_hhs(self):
        caminhos = filedialog.askopenfilenames(
            parent=self,
            title=f"HHs para {self.arquivo_transacao_atual.split('/')[-1] if self.arquivo_transacao_atual else '...'}",
            filetypes=[("Arquivos de Texto", "*.txt")]
        )
        if not caminhos: return

        self.log(f"Processando {len(caminhos)} HHs...")
        try:
            novos_hhs, relatorio = self.service.processar_hhs(caminhos)
            self.hhs_carregados.extend(novos_hhs)
            
            self.log(f"HHs Aceitos: {relatorio.sucessos} | Ignorados: {relatorio.falhas}")
            self.lbl_status.configure(text=f"Ativo: {len(self.transacoes_carregadas)} Transações | HHs Carregados: {len(self.hhs_carregados)}")
            
            if self.transacoes_carregadas and self.hhs_carregados:
                preview, descartados = self.service.consolidar_dados(self.transacoes_carregadas, self.hhs_carregados)
                self._renderizar_tabela(preview)
                if descartados > 0:
                    self.log(f"Prévia: {descartados} HHs não encontraram par e serão descartados.")

        except Exception as e:
            messagebox.showerror("Erro", str(e))

    def consolidar(self):
        if not self.transacoes_carregadas:
            return

        self.log("Finalizando processo...")
        try:
            resultado, descartados = self.service.consolidar_dados(self.transacoes_carregadas, self.hhs_carregados)
            novos, atualizados = self.service.salvar_no_banco(resultado)
            
            msg_final = f"Importação Concluída!\n\n" \
                        f"Mapeados/Salvos: {novos + atualizados}\n" \
                        f"HHs Descartados: {descartados}"
            
            messagebox.showinfo("Sucesso", msg_final)
            self.log(f"Salvo no Banco: {novos} novos, {atualizados} atualizados.")
            self.log(f"Hand Histories Descartados (Sem Transação): {descartados}")
            
            self.reiniciar_fluxo()

        except Exception as e:
            self.log(f"ERRO: {str(e)}")
            messagebox.showerror("Erro Crítico", str(e))

    def _formatar_moeda(self, valor):
        valor = float(valor)
        
        sinal = "- " if valor < 0 else ""
        
        valor_abs = abs(valor)
        
        texto_us = f"{valor_abs:,.2f}"
        
        texto_br = texto_us.replace(",", "X").replace(".", ",").replace("X", ".")
        
        return f"{sinal}$ {texto_br}"

    def _renderizar_tabela(self, lista_consolidados):
        for widget in self.tabela_frame.winfo_children():
            widget.destroy()

        headers = ["Data", "Torneio", "Status", "Lucro"]
        for i, h in enumerate(headers):
            lbl = ctk.CTkLabel(self.tabela_frame, text=h, font=("Arial", 12, "bold"))
            lbl.grid(row=0, column=i, padx=5, pady=5, sticky="w")

        vinculados = [x for x in lista_consolidados if x.status == "VINCULADO"]
        
        limit = 50
        for idx, item in enumerate(vinculados[:limit]):
            r = item.resumo
            row_num = idx + 1
            
            cor_lucro = "white"
            if r['Lucro'] > 0: cor_lucro = "#2ecc71"
            elif r['Lucro'] < 0: cor_lucro = "#e74c3c"

            data_str = r['Data'].strftime("%d/%m %H:%M") if r['Data'] else "--"
            nome_limpo = r['Torneio'][:40] + "..." if len(r['Torneio']) > 40 else r['Torneio']
            
            texto_lucro = self._formatar_moeda(r['Lucro'])

            ctk.CTkLabel(self.tabela_frame, text=data_str).grid(row=row_num, column=0, padx=5, sticky="w")
            ctk.CTkLabel(self.tabela_frame, text=nome_limpo).grid(row=row_num, column=1, padx=5, sticky="w")
            ctk.CTkLabel(self.tabela_frame, text="OK", text_color="#3498db").grid(row=row_num, column=2, padx=5, sticky="w")
            
            ctk.CTkLabel(
                self.tabela_frame, 
                text=texto_lucro, 
                text_color=cor_lucro,
                font=("Consolas", 12, "bold") 
            ).grid(row=row_num, column=3, padx=5, sticky="w")
        
        if not vinculados:
            ctk.CTkLabel(self.tabela_frame, text="Nenhum dado consolidado para exibir.", text_color="gray").grid(row=1, column=0, columnspan=4, pady=20)
        
        if len(vinculados) > limit:
            ctk.CTkLabel(self.tabela_frame, text=f"... e mais {len(vinculados)-limit} registros").grid(row=limit+1, column=1)

if __name__ == "__main__":
    app = BodogApp()
    app.mainloop()