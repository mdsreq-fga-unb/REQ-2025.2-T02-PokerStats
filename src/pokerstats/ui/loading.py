import customtkinter as ctk
import threading

class AsyncLoading:
    def __init__(self, master_window, task_func, callback_func=None, close_early=False):
        self.master = master_window
        self.task = task_func
        self.callback = callback_func
        self.close_early = close_early
        self.result = None
        self.error = None
        
        self.popup = ctk.CTkToplevel(self.master)
        self.popup.title("")
        self.popup.geometry("300x150")
        self.popup.resizable(False, False)
        self.popup.overrideredirect(True)
        self.popup.attributes("-topmost", True)
        
        self.center_popup()

        frame = ctk.CTkFrame(self.popup, border_width=2, border_color="#3498db")
        frame.pack(fill="both", expand=True)
        
        ctk.CTkLabel(frame, text="Processando...", font=("Arial", 16, "bold")).pack(pady=(35, 15))
        ctk.CTkLabel(frame, text="Aguarde um momento", font=("Arial", 12), text_color="gray").pack(pady=(0, 10))
        
        self.progress = ctk.CTkProgressBar(frame, width=220, mode="indeterminate")
        self.progress.pack(pady=10)
        self.progress.start()
        
        self.popup.update_idletasks() 
        self.popup.deiconify()
        
        self._safe_grab()
        
        thread = threading.Thread(target=self._run_thread, daemon=True)
        thread.start()

    def center_popup(self):
        try:
            self.master.update_idletasks()
            x = self.master.winfo_rootx() + (self.master.winfo_width() // 2) - 150
            y = self.master.winfo_rooty() + (self.master.winfo_height() // 2) - 75
            self.popup.geometry(f"+{x}+{y}")
        except:
            pass

    def _safe_grab(self):
        try:
            self.popup.grab_set()
        except Exception:
            self.master.after(50, self._safe_grab)

    def _run_thread(self):
        try:
            if self.task:
                self.result = self.task()
        except Exception as e:
            self.error = e
        
        self.master.after(0, self._finish)

    def _close_window(self):
        try:
            self.popup.grab_release()
            self.popup.destroy()
            self.master.update_idletasks() 
        except:
            pass

    def _finish(self):
        if self.close_early:
            self._close_window()
            if self.callback:
                try:
                    self.callback(self.result, self.error)
                except Exception as e:
                    print(f"Erro Callback: {e}")
        else:
            if self.callback:
                try:
                    self.callback(self.result, self.error)
                except Exception as e:
                    print(f"Erro Callback: {e}")
            
            try:
                self.master.update_idletasks()
            except:
                pass
            
            self._close_window()

def executar_com_loading(master, tarefa, sucesso, close_early=False):
    """
    close_early=True: Fecha o loading ANTES do callback (Ideal para Messagebox)
    close_early=False: Fecha o loading DEPOIS do callback (Ideal para renderizar Tabela)
    """
    AsyncLoading(master, tarefa, sucesso, close_early)