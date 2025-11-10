import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import json


with open("config/colores.json", "r", encoding="utf-8") as archivo: 
    colores = json.load(archivo)
    
with open("config/ventana.json","r", encoding="utf-8") as archivo: 
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
    
        # Crear una ventana
        ventana_ID = tk.Toplevel(root)
        ventana_ID.title(f"Pestaña de ID {user_id}")
        ventana_ID.geometry(f"{ventana['ancho']}x{ventana['altura']}")
        ventana_ID.config(bg=colores["fondo"])
    
        # Contenido de la pestaña
        label_bienvenida = ttk.Label(ventana_ID, text=f"Bienvenido, usuario con ID: {user_id}")
        label_bienvenida.pack(pady=20)
    
        # notebook dentro de la ventana
        nuevo_notebook = ttk.Notebook(ventana_ID)
        nuevo_notebook.pack(expand=True, fill="both", padx=10, pady=10)
    
        # Crear una pestaña dentro de la ventana
        frame_datos = ttk.Frame(nuevo_notebook)
    
        nuevo_notebook.add(frame_datos, text="Datos")
    
        # Agregar contenido a la subpestañas
        ttk.Label(frame_datos, text="Aqui texto para la siguiente elección (estación, horario, etc.)").pack(pady=10)
    
    # Botón para iniciar el registro
    boton_abrir = ttk.Button(pestana_principal, text="Registro", command=Ingreso_ID)
    boton_abrir.pack(pady=20)

if __name__ == "__main__":
    root = tk.Tk()
    Ventana_principal(root)
    root.mainloop()
