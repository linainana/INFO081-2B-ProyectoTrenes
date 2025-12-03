import tkinter as tk
from tkinter import ttk

from .ventanas_trenes import ver_trenes
from .ventana_rutas import ver_rutas
from .ventana_estaciones import ver_estaciones
from .ventana_id import Ingreso_ID

def Ventana_principal(root, ventana, colores):
    root.title("Inicial")
    root.geometry(f"{ventana['ancho']}x{ventana['altura']}")
    root.config(bg=colores["fondo"])

    notebook = ttk.Notebook(root)
    notebook.pack(expand=True, fill="both")

    pestana_principal = tk.Frame(notebook, bg=colores["fondo"])
    notebook.add(pestana_principal, text=ventana["titulo"])

    boton_registro = ttk.Button(
        pestana_principal,
        text="Ingresar",
        command=lambda: Ingreso_ID(root, ventana, colores)
    )
    boton_registro.pack(pady=100)
