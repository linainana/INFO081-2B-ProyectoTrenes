import tkinter as tk
from tkinter import ttk, messagebox
from ui.simulacion import iniciar_simulacion_en_frame
from .ventanas_trenes import ver_trenes
from .ventana_estaciones import ver_estaciones
from .ventana_rutas import ver_rutas

def Ingreso_ID(root, ventana, colores):
    ventana_ingreso = tk.Toplevel(root)
    ventana_ingreso.title("Ingreso ID")
    ventana_ingreso.geometry(f"{ventana['ancho']}x{ventana['altura']}")
    ventana_ingreso.config(bg=colores["fondo"])

    ttk.Label(ventana_ingreso, text="Bienvenido").pack(pady=20)
    ttk.Label(ventana_ingreso, text="Ingrese su ID:").pack(pady=15)

    entry_id = ttk.Entry(ventana_ingreso)
    entry_id.pack(pady=5)

    boton_registro = ttk.Button(
        ventana_ingreso,
        text="Aceptar",
        command=lambda: abrir_ID(entry_id, root, ventana, colores)
    )
    boton_registro.pack(pady=20)

def abrir_ID(entry_id, root, ventana, colores):
    user_id = entry_id.get().strip()
    if not user_id:
        messagebox.showwarning("Atención", "Debe ingresar un ID antes de continuar.")
        return
    entry_id.winfo_toplevel().destroy()

    ventana_ID = tk.Toplevel(root)
    ventana_ID.title(f"Pestaña de ID {user_id}")
    ventana_ID.geometry(f"{ventana['ancho']}x{ventana['altura']}")
    ventana_ID.config(bg=colores["fondo"])

    ttk.Label(ventana_ID, text=f"Bienvenido, usuario con ID: {user_id}").pack(pady=20)

    nuevo_notebook = ttk.Notebook(ventana_ID)
    nuevo_notebook.pack(expand=True, fill="both", padx=10, pady=10)

    frame_datos = ttk.Frame(nuevo_notebook)
    nuevo_notebook.add(frame_datos, text="Gestión de Datos")

    ttk.Button(frame_datos, text="Ver trenes", command=lambda: ver_trenes(root, ventana, colores) ).pack(pady=10)
    ttk.Button(frame_datos,text="Ver rutas",command=lambda: ver_rutas(root, ventana, colores)).pack(pady=10)
    ttk.Button(frame_datos,text="Ver estaciones",command=lambda: ver_estaciones(root, ventana, colores)).pack(pady=10)

    frame_simulacion = tk.Frame(nuevo_notebook)
    nuevo_notebook.add(frame_simulacion, text="Simulación EFE")

    nuevo_notebook.select(0)
