import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import json
import os

base_dir = os.path.dirname(__file__)

config_path = os.path.join(base_dir, "..", "config", "colores.json")
with open(config_path, "r", encoding="utf-8") as archivo: 
    colores = json.load(archivo)
    
ventana_path = os.path.join(base_dir, "..", "config", "ventana.json")
with open(ventana_path,"r", encoding="utf-8") as archivo: 
    ventana = json.load(archivo)


# Crea la ventana principal
def Ventana_principal(root):
    root.title("Inicial")
    root.geometry(f"{ventana['ancho']}x{ventana['altura']}")
    root.config(bg=colores["fondo"])
    
    # Crear el contenedor de la pestaña
    notebook = ttk.Notebook(root)
    notebook.pack(expand=True, fill="both")
    
    # Crear la pestaña 
    pestana_principal = tk.Frame(notebook, bg=colores["fondo"])
    notebook.add(pestana_principal, text=ventana["titulo"])


    #Función que abre la ventana para ingresar el ID
    def Ingreso_ID():
        # Crear la ventana para igresar el ID
        ventana_ingreso = tk.Toplevel(root)
        ventana_ingreso.title(f"Ingreso ID")
        ventana_ingreso.geometry(f"{ventana['ancho']}x{ventana['altura']}")
        ventana_ingreso.config(bg=colores["fondo"])
    
        # Crear la pestaña
        label_bienvenida = ttk.Label(ventana_ingreso, text=f"Bienvenido")
        label_bienvenida.pack(pady=20)
    
        # Etiqueta y campo para ingresar el ID
        label_id = ttk.Label(ventana_ingreso, text="Ingrese su ID:")
        label_id.pack(pady=15)
    
        entry_id = ttk.Entry(ventana_ingreso)
        entry_id.pack(pady=5)
    
        # Botón para confirmar el ID y pasar entry a la siguiente ventana
        boton_registro = ttk.Button(ventana_ingreso, text="Aceptar", command=lambda: abrir_ID(entry_id))
        boton_registro.pack(pady=20)
    
    # Función que abre una nueva ventana con el ID ingresado
    def abrir_ID(entry_id):
        user_id = entry_id.get().strip()
        if not user_id:
            messagebox.showwarning("Atención", "Debe ingresar un ID antes de continuar.")
            return
    
            ventana_ID = tk.Toplevel(root)
        ventana_ID.title(f"Pestaña de ID {user_id}")
        ventana_ID.geometry("400x300")

        ttk.Label(ventana_ID, text=f"Bienvenido, usuario con ID: {user_id}").pack(pady=20)
    
        boton_trenes = ttk.Button(ventana_ID, text="Ver trenes", command=ver_trenes)
        boton_trenes.pack(pady=10)

        boton_rutas = ttk.Button(ventana_ID, text="Ver rutas", command=ver_rutas)
        boton_rutas.pack(pady=10)

        boton_estaciones = ttk.Button(ventana_ID, text="Ver estaciones", command=ver_estaciones)
        boton_estaciones.pack(pady=10)

    def ver_trenes():
        ver_tren = tk.Toplevel(root)
        ver_tren.title("TRENES")
        ver_tren.geometry("400x300")

        ttk.Label(ver_tren, text="VER TRENES").pack(pady=20)
        ttk.Label(ver_tren, text="TRENES").pack(padx=50, pady=20)
    
        def crear_tren():
            crear_trenes = tk.Toplevel(root)
            crear_trenes.title("CREAR TREN")
            crear_trenes.geometry("400x300")

            ttk.Label(crear_trenes, text="TEXTO").pack(pady=20)
    
            boton_guardar = ttk.Button(crear_trenes, text="GUARDAR")
            boton_guardar.pack(pady=10)
        
        def editar_tren():
            editar_trenes = tk.Toplevel(root)
            editar_trenes.title("EDITAR TREN")
            editar_trenes.geometry("400x300")

            ttk.Label(editar_trenes, text="TEXTO").pack(pady=20)
    
            boton_guardar = ttk.Button(editar_trenes, text="GUARDAR")
            boton_guardar.pack(pady=10)
        
        def eliminar_tren():
            eliminar_trenes = tk.Toplevel(root)
            eliminar_trenes.title("ELIMINAR TREN")
            eliminar_trenes.geometry("400x300")

            ttk.Label(eliminar_trenes, text="TEXTO").pack(pady=20)
    
            boton_guardar = ttk.Button(eliminar_trenes, text="GUARDAR")
            boton_guardar.pack(pady=10)
        
        def ver_estado():
            v_estado = tk.Toplevel(root)
            v_estado.title("ESTADO DE TRENES")
            v_estado.geometry("400x300")

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
       
    def ver_estaciones():
        ver_estacion = tk.Toplevel(root)
        ver_estacion.title("ESTACIONES")
        ver_estacion.geometry("400x300")

        ttk.Label(ver_estacion, text="VER ESTACIONES").pack(pady=20)
        ttk.Label(ver_estacion, text="ESTACIONES").pack(padx=50, pady=20)
    
        def crear_estaciones():
            crear_estacion = tk.Toplevel(root)
            crear_estacion.title("CREAR ESTACIÓN")
            crear_estacion.geometry("400x300")

            ttk.Label(crear_estacion, text="TEXTO").pack(pady=20)
    
            boton_guardar = ttk.Button(crear_estacion, text="GUARDAR")
            boton_guardar.pack(pady=10)
        
        def editar_estaciones():
            editar_estacion = tk.Toplevel(root)
            editar_estacion.title("EDITAR ESTACIÓN")
            editar_estacion.geometry("400x300")

            ttk.Label(editar_estacion, text="TEXTO").pack(pady=20)
    
            boton_guardar = ttk.Button(editar_estacion, text="GUARDAR")
            boton_guardar.pack(pady=10)
        
        def eliminar_estaciones():
            eliminar_estacion = tk.Toplevel(root)
            eliminar_estacion.title("ELIMINAR ESTACIÓN")
            eliminar_estacion.geometry("400x300")

            ttk.Label(eliminar_estacion, text="TEXTO").pack(pady=20)
    
            boton_guardar = ttk.Button(eliminar_estacion, text="GUARDAR")
            boton_guardar.pack(pady=10)
        
        def ver_estado():
            v_estado = tk.Toplevel(root)
            v_estado.title("ESTADO DE ESTACIÓN")
            v_estado.geometry("400x300")

            ttk.Label(v_estado, text="TEXTO").pack(pady=20)
    
            boton_guardar = ttk.Button(v_estado, text="GUARDAR")
            boton_guardar.pack(pady=10)

        boton_crear = ttk.Button(ver_estacion, text="Crear estación", command=crear_estaciones)
        boton_crear.pack(pady=10)

        boton_editar = ttk.Button(ver_estacion, text="Editar estación", command=editar_estaciones)
        boton_editar.pack(pady=10)

        boton_eliminar = ttk.Button(ver_estacion, text="Eliminar estación", command=eliminar_estaciones)
        boton_eliminar.pack(pady=10)

        boton_estado = ttk.Button(ver_estacion, text="Estado", command=ver_estado)
        boton_estado.pack(pady=10)
          
    def ver_rutas():
        ver_ruta = tk.Toplevel(root)
        ver_ruta.title("RUTAS")
        ver_ruta.geometry("400x300")

        ttk.Label(ver_ruta, text="VER RUTAS").pack(pady=20)
        ttk.Label(ver_ruta, text="TRENES").pack(padx=50, pady=20)
    
        def crear_rutas():
            crear_ruta = tk.Toplevel(root)
            crear_ruta.title("CREAR RUTA")
            crear_ruta.geometry("400x300")

            ttk.Label(crear_ruta, text="TEXTO").pack(pady=20)
    
            boton_guardar = ttk.Button(crear_ruta, text="GUARDAR")
            boton_guardar.pack(pady=10)
        
        def editar_rutas():
            editar_ruta = tk.Toplevel(root)
            editar_ruta.title("EDITAR RUTA")
            editar_ruta.geometry("400x300")

            ttk.Label(editar_ruta, text="TEXTO").pack(pady=20)
    
            boton_guardar = ttk.Button(editar_ruta, text="GUARDAR")
            boton_guardar.pack(pady=10)
        
        def eliminar_rutas():
            eliminar_ruta = tk.Toplevel(root)
            eliminar_ruta.title("ELIMINAR RUTA")
            eliminar_ruta.geometry("400x300")

            ttk.Label(eliminar_ruta, text="TEXTO").pack(pady=20)
    
            boton_guardar = ttk.Button(eliminar_ruta, text="GUARDAR")
            boton_guardar.pack(pady=10)
        
        def ver_estado():
            v_estado = tk.Toplevel(root)
            v_estado.title("ESTADO DE RUTA")
            v_estado.geometry("400x300")

            ttk.Label(v_estado, text="TEXTO").pack(pady=20)
    
            boton_guardar = ttk.Button(v_estado, text="GUARDAR")
            boton_guardar.pack(pady=10)
        
        boton_crear = ttk.Button(ver_ruta, text="Crear ruta", command=crear_rutas)
        boton_crear.pack(pady=10)

        boton_editar = ttk.Button(ver_ruta, text="Editar ruta", command=editar_rutas)
        boton_editar.pack(pady=10)

        boton_eliminar = ttk.Button(ver_ruta, text="Eliminar ruta", command=eliminar_rutas)
        boton_eliminar.pack(pady=10)

        boton_estado = ttk.Button(ver_ruta, text="Estado", command=ver_estado)
        boton_estado.pack(pady=10)
    
    boton_registro = ttk.Button(pestana_principal, text="Ingresar", command=Ingreso_ID)
    boton_registro.pack(pady=100)

if __name__ == "__main__":
    root = tk.Tk()
    Ventana_principal(root)
    root.mainloop()
