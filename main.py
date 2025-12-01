import customtkinter as ctk
from src.pokerstats.core.service import BodogService
from src.pokerstats.ui.tabs.dashboard import DashboardTab
from src.pokerstats.ui.tabs.management import ManagementTab
from src.pokerstats.ui.loading import executar_com_loading

class BodogApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.service = BodogService()
        self.title("Poker Stats")
        self.geometry("1100x800")
        
        self.after(0, self._maximizar)

        self.tabview = ctk.CTkTabview(self, command=self._ao_mudar_aba)
        self.tabview.pack(fill="both", expand=True, padx=10, pady=10)

        self.tab_import = self.tabview.add("Dashboard & Importação")
        self.tab_data = self.tabview.add("Gerenciar Registros")

        self.dash_view = DashboardTab(self.tab_import, self.service, self.notificar_mudancas, self)
        self.dash_view.pack(fill="both", expand=True)

        self.mgmt_view = ManagementTab(self.tab_data, self.service, self.notificar_mudancas, self)
        self.mgmt_view.pack(fill="both", expand=True)

        self.after(200, self._check_maximized_and_start)

    def _maximizar(self):
        try: self.attributes('-zoomed', True)
        except: self.state('zoomed')

    def _check_maximized_and_start(self):
        """
        Verifica se a janela atingiu um tamanho suficiente (maximizada) e só então inicia o loading.
        """
        self.update_idletasks()
        
        if self.winfo_width() > 1200:
            self.carregar_dash_inicial()
        else:
            self.after(100, self._check_maximized_and_start)

    def carregar_dash_inicial(self):
        """Hard Refresh: Vai ao banco e popula o cache"""
        def tarefa():
            self.service.recarregar_cache_banco()
        
        def fim(res, err):
            if not err:
                self.notificar_mudancas()
                
        executar_com_loading(self, tarefa, fim)

    def _ao_mudar_aba(self):
        aba_atual = self.tabview.get()
        if aba_atual == "Gerenciar Registros":
            self.mgmt_view.ao_exibir_aba()
        elif aba_atual == "Dashboard & Importação":
            self.dash_view.atualizar_view()

    def notificar_mudancas(self):
        """Redesenha a interface (sem loading) com os dados novos da memória"""
        self.dash_view.atualizar_view()
        if self.tabview.get() == "Gerenciar Registros":
            self.mgmt_view.atualizar_tabela_visual()
        else:
            self.mgmt_view.ja_carregou = False

if __name__ == "__main__":
    app = BodogApp()
    app.mainloop()