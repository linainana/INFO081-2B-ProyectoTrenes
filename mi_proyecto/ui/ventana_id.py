# ventana_login.py
import tkinter as tk
from tkinter import ttk, messagebox

from .ventanas_trenes import ver_trenes
from .ventana_estaciones import ver_estaciones
from .ventana_rutas import ver_rutas

def ventana_ingreso_id(root, ventana, colores):
    login = tk.Toplevel(root)
    login.title("Ingreso ID")
    login.geometry(f"{ventana['ancho']}x{ventana['altura']}")
    login.config(bg=colores["fondo"])

    ttk.Label(login, text="Bienvenido").pack(pady=20)
    ttk.Label(login, text="Ingrese su ID:").pack(pady=15)

    entry_id = ttk.Entry(login)
    entry_id.pack(pady=5)

    ttk.Button(
        login,
        text="Aceptar",
        command=lambda: abrir_id(root, entry_id, ventana, colores)
    ).pack(pady=20)

def abrir_id(root, entry_id, ventana, colores):
    user_id = entry_id.get().strip()

    if not user_id:
        messagebox.showwarning("Atención", "Debe ingresar un ID antes de continuar.")
        return

    ventana_id = tk.Toplevel(root)
    ventana_id.title(f"Pestaña ID {user_id}")
    ventana_id.geometry(f"{ventana['ancho']}x{ventana['altura']}")
    ventana_id.config(bg=colores["fondo"])

    ttk.Label(ventana_id, text=f"Bienvenido, usuario con ID: {user_id}").pack(pady=20)

    ttk.Button(ventana_id, text="Ver trenes", command=lambda: ver_trenes(root, ventana, colores)).pack(pady=10)
    ttk.Button(ventana_id, text="Ver rutas", command=lambda: ver_rutas(root, ventana, colores)).pack(pady=10)
    ttk.Button(ventana_id, text="Ver estaciones", command=lambda: ver_estaciones(root, ventana, colores)).pack(pady=10)
