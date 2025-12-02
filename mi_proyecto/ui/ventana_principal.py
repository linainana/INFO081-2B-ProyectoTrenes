# ventana_principal.py
import tkinter as tk
from tkinter import ttk, messagebox

from .ventanas_trenes import ver_trenes
from .ventana_rutas import ver_rutas
from .ventana_estaciones import ver_estaciones
from .ventana_id import ventana_ingreso_id

def Ventana_principal(root, ventana, colores):
    root.title("Inicial")
    root.geometry(f"{ventana['ancho']}x{ventana['altura']}")
    root.config(bg=colores["fondo"])

    notebook = ttk.Notebook(root)
    notebook.pack(expand=True, fill="both")

    pestana_principal = tk.Frame(notebook, bg=colores["fondo"])
    notebook.add(pestana_principal, text=ventana["titulo"])

    ttk.Button(
        pestana_principal,
        text="Ingresar",
        command=lambda: ventana_ingreso_id(root, ventana, colores)
    ).pack(pady=100)
