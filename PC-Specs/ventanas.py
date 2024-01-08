import tkinter as tk
from tkinter import ttk

def resize_panes(event):
    # Ajusta la proporción de los paneles al cambiar el tamaño de la ventana
    panedwindow.paneconfig(pane1, width=window.winfo_width() // 3)
    panedwindow.paneconfig(pane3, width=window.winfo_width() // 3)

# Crear una instancia de la clase Tk
window = tk.Tk()
window.title("División en 3 Secciones")

# Crear un objeto PanedWindow
panedwindow = ttk.Panedwindow(window, orient="horizontal")

# Crear tres paneles
pane1 = ttk.Frame(panedwindow, width=window.winfo_width() // 3, relief="sunken")
pane2 = ttk.Frame(panedwindow, relief="sunken")
pane3 = ttk.Frame(panedwindow, width=window.winfo_width() // 3, relief="sunken")

# Agregar paneles al PanedWindow
panedwindow.add(pane1)
panedwindow.add(pane2)
panedwindow.add(pane3)

# Configurar evento para ajustar la proporción al cambiar el tamaño de la ventana
window.bind("<Configure>", resize_panes)

# Empacar el PanedWindow en la ventana principal
panedwindow.pack(expand=True, fill="both")

# Iniciar el bucle principal de Tkinter
window.mainloop()
