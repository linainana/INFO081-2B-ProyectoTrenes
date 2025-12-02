# ventanas_estaciones.py
import tkinter as tk
from tkinter import ttk

def ver_estaciones(root, ventana, colores):
    ver_estacion = tk.Toplevel(root)
    ver_estacion.title("ESTACIONES")
    ver_estacion.geometry(f"{ventana['ancho']}x{ventana['altura']}")
    ver_estacion.config(bg=colores["fondo"])

    ttk.Label(ver_estacion, text="VER ESTACIONES").pack(pady=20)
    ttk.Label(ver_estacion, text="ESTACIONES").pack(padx=50, pady=20)

    def crear_estaciones():
        crear = tk.Toplevel(root)
        crear.title("CREAR ESTACIÓN")
        crear.geometry(f"{ventana['ancho']}x{ventana['altura']}")
        crear.config(bg=colores["fondo"])

        ttk.Label(crear, text="Crear estación").pack(pady=20)
        ttk.Button(crear, text="GUARDAR").pack(pady=10)

    def editar_estaciones():
        editar = tk.Toplevel(root)
        editar.title("EDITAR ESTACIÓN")
        editar.geometry(f"{ventana['ancho']}x{ventana['altura']}")
        editar.config(bg=colores["fondo"])

        ttk.Label(editar, text="Editar estación").pack(pady=20)
        ttk.Button(editar, text="GUARDAR").pack(pady=10)

    def eliminar_estaciones():
        eliminar = tk.Toplevel(root)
        eliminar.title("ELIMINAR ESTACIÓN")
        eliminar.geometry(f"{ventana['ancho']}x{ventana['altura']}")
        eliminar.config(bg=colores["fondo"])

        ttk.Label(eliminar, text="Eliminar estación").pack(pady=20)
        ttk.Button(eliminar, text="GUARDAR").pack(pady=10)

    def ver_estado():
        estado = tk.Toplevel(root)
        estado.title("ESTADO DE ESTACIÓN")
        estado.geometry(f"{ventana['ancho']}x{ventana['altura']}")
        estado.config(bg=colores["fondo"])

        ttk.Label(estado, text="Estado de estación").pack(pady=20)
        ttk.Button(estado, text="GUARDAR").pack(pady=10)

    ttk.Button(ver_estacion, text="Crear estación", command=crear_estaciones).pack(pady=10)
    ttk.Button(ver_estacion, text="Editar estación", command=editar_estaciones).pack(pady=10)
    ttk.Button(ver_estacion, text="Eliminar estación", command=eliminar_estaciones).pack(pady=10)
    ttk.Button(ver_estacion, text="Estado", command=ver_estado).pack(pady=10)
