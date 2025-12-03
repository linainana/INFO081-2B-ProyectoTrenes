import tkinter as tk
from tkinter import ttk
from tkinter import ttk, messagebox
import json
import os

base_dir = os.path.dirname(__file__)

def ver_estaciones(root, ventana, colores):
        ver_estacion = tk.Toplevel(root)
        ver_estacion.title("ESTACIONES")
        ver_estacion.geometry(f"{ventana['ancho']}x{ventana['altura']}")
        ver_estacion.config(bg=colores["fondo"])

        ttk.Label(ver_estacion, text="VER ESTACIONES").pack(pady=20)
        ttk.Label(ver_estacion, text="ESTACIONES").pack(padx=50, pady=20)
    
        def crear_estaciones():
            crear_estaciones = tk.Toplevel(root)
            crear_estaciones.title("CREAR ESTACIÓN")
            crear_estaciones.geometry(f"{ventana['ancho']}x{ventana['altura']}")
            crear_estaciones.config(bg=colores["fondo"])

            ttk.Label(crear_estaciones, text="Nombre de la estación: ").pack(pady=5)
            entry_nombre = ttk.Entry(crear_estaciones)
            entry_nombre.pack()
    
            ttk.Label(crear_estaciones, text="Región:").pack(pady=5)
            entry_reg = ttk.Entry(crear_estaciones) 
            entry_reg.pack()
            
            ttk.Label(crear_estaciones, text="Población:").pack(pady=5)
            entry_pob = ttk.Entry(crear_estaciones)
            entry_pob.pack()

            ttk.Label(crear_estaciones, text="Configuración de Vías (ej: Norte-Sur):").pack(pady=5)
            entry_vias = ttk.Entry(crear_estaciones)
            entry_vias.pack()
  
            def guardar_datos():
                nom = entry_nombre.get()
                reg = entry_reg.get()
                pob = entry_pob.get()
                vias = entry_vias.get()
                
                if not nom or not pob:
                    messagebox.showwarning("Error", "Faltan datos")
                    return

                nueva_est = {
                    "nombre": nom, 
                    "region": reg, 
                    "poblacion": int(pob),
                    "vias": [{"id": 1, "orientacion": vias, "ocupada": False}],
                    "flujo_acumulado": 0 
                }

                ruta_config = os.path.join(base_dir, "..", "config")
                archivo = os.path.join(ruta_config, "estaciones.json")
                
                lista = []
                if os.path.exists(archivo):
                    with open(archivo, "r", encoding="utf-8") as f: lista = json.load(f)
                
                lista.append(nueva_est)
                with open(archivo, "w", encoding="utf-8") as f: json.dump(lista, f, indent=4)
                
                messagebox.showinfo("Éxito", "Estación guardada.")
                crear_estaciones.destroy()

            ttk.Button(crear_estaciones, text="GUARDAR", command=guardar_datos).pack(pady=20)

        def editar_estaciones():
            editar_est = tk.Toplevel(root)
            editar_est.title("EDITAR ESTACIÓN")
            editar_est.geometry(f"{ventana['ancho']}x{ventana['altura']}")
            editar_est.config(bg=colores["fondo"])

            ttk.Label(editar_est, text="Nombre exacto de la estación a editar:").pack(pady=5)
            entry_target = ttk.Entry(editar_est)
            entry_target.pack()
            
            ttk.Label(editar_est, text="Nueva Región:").pack(pady=5)
            entry_reg = ttk.Entry(editar_est)
            entry_reg.pack()
            
            ttk.Label(editar_est, text="Nueva Población:").pack(pady=5)
            entry_pob = ttk.Entry(editar_est)
            entry_pob.pack()

        def eliminar_estaciones():
            elim_est = tk.Toplevel(root)
            elim_est.title("ELIMINAR ESTACIÓN")
            elim_est.geometry(f"{ventana['ancho']}x{ventana['altura']}")
            elim_est.config(bg=colores["fondo"])

            ttk.Label(elim_est, text="Nombre de la estación a eliminar:").pack(pady=20)
            entry_nombre = ttk.Entry(elim_est)
            entry_nombre.pack()

            def confirmar():
                target = entry_nombre.get()
                ruta_config = os.path.join(base_dir, "..", "config")
                archivo = os.path.join(ruta_config, "estaciones.json")

                if not os.path.exists(archivo):
                    messagebox.showerror("Error", "No hay datos.")
                    return

                with open(archivo, "r", encoding="utf-8") as f:
                    lista = json.load(f)

                nueva_lista = [e for e in lista if e["nombre"] != target]

                if len(nueva_lista) == len(lista):
                    messagebox.showwarning("Error", "No se encontró esa estación.")
                else:
                    with open(archivo, "w", encoding="utf-8") as f:
                        json.dump(nueva_lista, f, indent=4)
                    messagebox.showinfo("Éxito", "Estación eliminada.")
                    elim_est.destroy()

                ttk.Button(elim_est, text="ELIMINAR", command=confirmar).pack(pady=20)
        
        def ver_estado():
            v_estado = tk.Toplevel(root)
            v_estado.title("LISTADO DE ESTACIONES") 
            v_estado.geometry("400x400") 
            v_estado.config(bg=colores["fondo"])

            lbl_titulo = ttk.Label(v_estado, text="Base de Datos Actual:")
            lbl_titulo.pack(pady=10)

            texto1 = tk.Text(v_estado, width=40, height=15)
            texto1.pack(padx=10, pady=10)

            ruta_config = os.path.join(base_dir, "..", "config")
            archivo = os.path.join(ruta_config, "estaciones.json")

            if os.path.exists(archivo):
                try:
                    with open(archivo, "r", encoding="utf-8") as f:
                        data = json.load(f)
                    texto2 = json.dumps(data, indent=2, ensure_ascii=False)
                    texto1.insert(tk.END, texto2)
                except Exception as e:
                    texto1.insert(tk.END, f"Error leyendo archivo: {e}")
            else:
                texto1.insert(tk.END, "No hay datos guardados aún.")

            texto1.config(state=tk.DISABLED)

            ttk.Button(v_estado, text="Cerrar", command=v_estado.destroy).pack(pady=10)

        boton_crear = ttk.Button(ver_estacion, text="Crear estación", command=crear_estaciones)
        boton_crear.pack(pady=10)

        boton_editar = ttk.Button(ver_estacion, text="Editar estación", command=editar_estaciones)
        boton_editar.pack(pady=10)

        boton_eliminar = ttk.Button(ver_estacion, text="Eliminar estación", command=eliminar_estaciones)
        boton_eliminar.pack(pady=10)

        boton_estado = ttk.Button(ver_estacion, text="Estado", command=ver_estado)
        boton_estado.pack(pady=10)