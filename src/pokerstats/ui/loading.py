import customtkinter as ctk
import threading
import time

class AsyncLoading:
    def __init__(self, master_window, task_func, callback_func=None, min_duration=1.0):
        self.master = master_window
        self.task = task_func
        self.callback = callback_func
        self.min_duration = min_duration
        self.result = None
        self.error = None
        
        self.popup = ctk.CTkToplevel(self.master)
        self.popup.withdraw() 
        
        self.popup.title("")
        self.popup.geometry("300x120")
        self.popup.resizable(False, False)
        
        self.popup.transient(self.master)
        
        self.popup.overrideredirect(True)
        
        self.center_popup()

        frame = ctk.CTkFrame(self.popup, border_width=2, border_color="#3498db")
        frame.pack(fill="both", expand=True)
        
        ctk.CTkLabel(frame, text="Processando...", font=("Arial", 16, "bold")).pack(pady=(30, 5))
        
        self.progress = ctk.CTkProgressBar(frame, width=200, mode="indeterminate")
        self.progress.pack(pady=15)
        self.progress.start()
        
        self.popup.deiconify() 
        self.popup.lift()      
        self.popup.update_idletasks()
        
        try:
            self.popup.grab_set() 
        except:
            pass 
        
        thread = threading.Thread(target=self._run_thread, daemon=True)
        thread.start()

    def center_popup(self):
        try:
            self.master.update_idletasks()
            x = self.master.winfo_rootx() + (self.master.winfo_width() // 2) - 150
            y = self.master.winfo_rooty() + (self.master.winfo_height() // 2) - 60
            self.popup.geometry(f"+{x}+{y}")
        except:
            pass

    def _run_thread(self):
        start_time = time.time()

        try:
            if self.task:
                self.result = self.task()
        except Exception as e:
            self.error = e

        elapsed_time = time.time() - start_time
        time_to_wait = self.min_duration - elapsed_time

        if time_to_wait > 0:
            time.sleep(time_to_wait)
        
        self.master.after(0, self._finish)

    def _finish(self):
        try:
            self.popup.grab_release()
            self.popup.destroy()
            self.master.update_idletasks()
        except:
            pass

        if self.callback:
            self.callback(self.result, self.error)

def executar_com_loading(master, tarefa, sucesso, close_early=False):
    AsyncLoading(master, tarefa, sucesso, min_duration=1.0)