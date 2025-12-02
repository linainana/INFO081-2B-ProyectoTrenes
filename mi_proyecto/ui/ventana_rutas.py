
import tkinter as tk
from tkinter import ttk

def ver_rutas(root, ventana, colores):
    ver_ruta = tk.Toplevel(root)
    ver_ruta.title("RUTAS")
    ver_ruta.geometry(f"{ventana['ancho']}x{ventana['altura']}")
    ver_ruta.config(bg=colores["fondo"])

    ttk.Label(ver_ruta, text="VER RUTAS").pack(pady=20)
    ttk.Label(ver_ruta, text="RUTAS").pack(padx=50, pady=20)

    def crear_rutas():
        crear = tk.Toplevel(root)
        crear.title("CREAR RUTA")
        crear.geometry(f"{ventana['ancho']}x{ventana['altura']}")
        crear.config(bg=colores["fondo"])

        ttk.Label(crear, text="Crear ruta").pack(pady=20)
        ttk.Button(crear, text="GUARDAR").pack(pady=10)

    def editar_rutas():
        editar = tk.Toplevel(root)
        editar.title("EDITAR RUTA")
        editar.geometry(f"{ventana['ancho']}x{ventana['altura']}")
        editar.config(bg=colores["fondo"])

        ttk.Label(editar, text="Editar ruta").pack(pady=20)
        ttk.Button(editar, text="GUARDAR").pack(pady=10)

    def eliminar_rutas():
        eliminar = tk.Toplevel(root)
        eliminar.title("ELIMINAR RUTA")
        eliminar.geometry(f"{ventana['ancho']}x{ventana['altura']}")
        eliminar.config(bg=colores["fondo"])

        ttk.Label(eliminar, text="Eliminar ruta").pack(pady=20)
        ttk.Button(eliminar, text="GUARDAR").pack(pady=10)

    def ver_estado():
        estado = tk.Toplevel(root)
        estado.title("ESTADO DE RUTA")
        estado.geometry(f"{ventana['ancho']}x{ventana['altura']}")
        estado.config(bg=colores["fondo"])

        ttk.Label(estado, text="Estado de ruta").pack(pady=20)
        ttk.Button(estado, text="GUARDAR").pack(pady=10)

    ttk.Button(ver_ruta, text="Crear ruta", command=crear_rutas).pack(pady=10)
    ttk.Button(ver_ruta, text="Editar ruta", command=editar_rutas).pack(pady=10)
    ttk.Button(ver_ruta, text="Eliminar ruta", command=eliminar_rutas).pack(pady=10)
    ttk.Button(ver_ruta, text="Estado", command=ver_estado).pack(pady=10)
