import tkinter as tk
from tkinter import ttk

def ver_trenes(root,ventana,colores):
        ver_tren = tk.Toplevel(root)
        ver_tren.title("TRENES")
        ver_tren.geometry(f"{ventana['ancho']}x{ventana['altura']}")
        ver_tren.config(bg=colores["fondo"])

        ttk.Label(ver_tren, text="VER TRENES").pack(pady=20)
        ttk.Label(ver_tren, text="TRENES").pack(padx=50, pady=20)
    
        def crear_tren():
            crear_trenes = tk.Toplevel(root)
            crear_trenes.title("CREAR TREN")
            crear_trenes.geometry(f"{ventana['ancho']}x{ventana['altura']}")
            crear_trenes.config(bg=colores["fondo"])

            ttk.Label(crear_trenes, text="TEXTO").pack(pady=20)

            boton_guardar = ttk.Button(crear_trenes, text="GUARDAR")
            boton_guardar.pack(pady=10)
        
        def editar_tren():
            editar_trenes = tk.Toplevel(root)
            editar_trenes.title("EDITAR TREN")
            editar_trenes.geometry(f"{ventana['ancho']}x{ventana['altura']}")
            editar_trenes.config(bg=colores["fondo"])

            ttk.Label(editar_trenes, text="TEXTO").pack(pady=20)
    
            boton_guardar = ttk.Button(editar_trenes, text="GUARDAR")
            boton_guardar.pack(pady=10)
        
        def eliminar_tren():
            eliminar_trenes = tk.Toplevel(root)
            eliminar_trenes.title("ELIMINAR TREN")
            eliminar_trenes.geometry(f"{ventana['ancho']}x{ventana['altura']}")
            eliminar_trenes.config(bg=colores["fondo"])

            ttk.Label(eliminar_trenes, text="TEXTO").pack(pady=20)
    
            boton_guardar = ttk.Button(eliminar_trenes, text="GUARDAR")
            boton_guardar.pack(pady=10)
        
        def ver_estado():
            v_estado = tk.Toplevel(root)
            v_estado.title("ESTADO DE TRENES")
            v_estado.geometry(f"{ventana['ancho']}x{ventana['altura']}")
            v_estado.config(bg=colores["fondo"])

            ttk.Label(v_estado, text="TEXTO").pack(pady=20)
    
            boton_guardar = ttk.Button(v_estado, text="GUARDAR")
            boton_guardar.pack(pady=10)

        boton_crear = ttk.Button(ver_tren, text="Crear tren", command=crear_tren)
        boton_crear.pack(pady=10)

        boton_editar = ttk.Button(ver_tren, text="Editar tren", command=editar_tren)
        boton_editar.pack(pady=10)

        boton_eliminar = ttk.Button(ver_tren, text="Eliminar tren", command=eliminar_tren)
        boton_eliminar.pack(pady=10)

        boton_estado = ttk.Button(ver_tren, text="Estado", command=ver_estado)
        boton_estado.pack(pady=10)