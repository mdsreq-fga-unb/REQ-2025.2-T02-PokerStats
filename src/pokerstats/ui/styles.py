import tkinter as tk
from tkinter import ttk

def aplicar_estilo_treeview():
    style = ttk.Style()
    
    style.theme_use("default")

    bg_color = "#2b2b2b"
    fg_color = "white"
    header_bg = "#343638"
    selected_bg = "#1f6aa5"

    style.configure("Treeview",
                    background=bg_color,
                    foreground=fg_color,
                    fieldbackground=bg_color,
                    borderwidth=0,
                    rowheight=30, 
                    font=("Arial", 11))

    style.configure("Treeview.Heading",
                    background=header_bg,
                    foreground="white",
                    relief="flat",
                    font=("Arial", 11, "bold"))
    
    style.map("Treeview",
              background=[('selected', selected_bg)],
              foreground=[('selected', 'white')])
    
    style.map("Treeview.Heading",
              background=[('active', '#404040')])

    return style