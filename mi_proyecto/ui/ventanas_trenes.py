import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import json
import os

base_dir = os.path.dirname(__file__)

def ver_trenes(root, ventana, colores):
        ver_tren = tk.Toplevel(root)
        ver_tren.title("TRENES")
        ver_tren.geometry(f"{ventana['ancho']}x{ventana['altura']}")
        ver_tren.config(bg=colores["fondo"])

        ttk.Label(ver_tren, text="VER TRENES").pack(pady=20)
        ttk.Label(ver_tren, text="TRENES").pack(padx=50, pady=20)
    
        def crear_tren():
            crear_trenes = tk.Toplevel(root)
            crear_trenes.title("CREAR TREN COMPLETO")
            crear_trenes.geometry(f"{ventana['ancho']}x{ventana['altura']}")
            crear_trenes.config(bg=colores["fondo"])

            ttk.Label(crear_trenes, text="Nombre del Tren:").pack(pady=5)
            entry_nombre = ttk.Entry(crear_trenes)
            entry_nombre.pack()
            
            ttk.Label(crear_trenes, text="Velocidad (km/h):").pack(pady=5)
            entry_vel = ttk.Entry(crear_trenes)
            entry_vel.pack()

            ttk.Label(crear_trenes, text="Cantidad de Vagones:").pack(pady=5)
            entry_vagones = ttk.Entry(crear_trenes)
            entry_vagones.pack()

            ttk.Label(crear_trenes, text="Capacidad por Vagón:").pack(pady=5)
            entry_cap_vagon = ttk.Entry(crear_trenes)
            entry_cap_vagon.pack()


            def guardar_datos():
                nom = entry_nombre.get()
                vel = entry_vel.get()
                n_vagones = entry_vagones.get()
                cap_vagon = entry_cap_vagon.get()
                
                if not nom or not vel or not n_vagones:
                    messagebox.showwarning("Error", "Faltan datos")
                    return

                try:

                    capacidad_total = int(n_vagones) * int(cap_vagon)
                    lista_vagones = [{"id": i+1, "capacidad": int(cap_vagon)} for i in range(int(n_vagones))]
                    
                except ValueError:
                    messagebox.showerror("Error", "Velocidad y Vagones deben ser números")
                    return
                nuevo_tren = {
                    "nombre": nom, 
                    "velocidad": int(vel), 
                    "capacidad": capacidad_total,
                    "vagones": lista_vagones, 
                    "accion": "Detenido"     
                }

                ruta_config = os.path.join(base_dir, "..", "config")
                if not os.path.exists(ruta_config): os.makedirs(ruta_config)
                archivo = os.path.join(ruta_config, "trenes.json")
                
                lista_trenes = []
                if os.path.exists(archivo):
                    with open(archivo, "r", encoding="utf-8") as f:
                        lista_trenes = json.load(f)
                
                lista_trenes.append(nuevo_tren)
                
                with open(archivo, "w", encoding="utf-8") as f:
                    json.dump(lista_trenes, f, indent=4)
                
                messagebox.showinfo("Éxito", f"Tren guardado con {capacidad_total} capacidad total.")
                crear_trenes.destroy()

            ttk.Button(crear_trenes, text="GUARDAR", command=guardar_datos).pack(pady=20)

        def editar_tren():
            editar_trenes = tk.Toplevel(root)
            editar_trenes.title("EDITAR TREN")
            editar_trenes.geometry(f"{ventana['ancho']}x{ventana['altura']}")
            editar_trenes.config(bg=colores["fondo"])

            ttk.Label(editar_trenes, text="Nombre del Tren a editar (Exacto):").pack(pady=5)
            entry_nombre = ttk.Entry(editar_trenes)
            entry_nombre.pack()
            
            ttk.Label(editar_trenes, text="NUEVA Velocidad:").pack(pady=5)
            entry_vel = ttk.Entry(editar_trenes)
            entry_vel.pack()
            
            ttk.Label(editar_trenes, text="NUEVA Capacidad:").pack(pady=5)
            entry_cap = ttk.Entry(editar_trenes)
            entry_cap.pack()

            def guardar_cambios():
                target_name = entry_nombre.get()
                new_vel = entry_vel.get()
                new_cap = entry_cap.get()

                ruta_config = os.path.join(base_dir, "..", "config")
                archivo = os.path.join(ruta_config, "trenes.json")

                if not os.path.exists(archivo):
                    messagebox.showerror("Error", "No hay trenes guardados para editar.")
                    return

                lista_trenes = []
                with open(archivo, "r", encoding="utf-8") as f:
                    lista_trenes = json.load(f)

                encontrado = False
                for tren in lista_trenes:
                    if tren["nombre"] == target_name:
                        if new_vel: tren["velocidad"] = new_vel
                        if new_cap: tren["capacidad"] = new_cap
                        encontrado = True
                        break
                
                if encontrado:
                    with open(archivo, "w", encoding="utf-8") as f:
                        json.dump(lista_trenes, f, indent=4)
                    messagebox.showinfo("Éxito", "Tren actualizado correctamente.")
                    editar_trenes.destroy()
                else:
                    messagebox.showwarning("Error", f"No se encontró el tren '{target_name}'")
            boton_guardar = ttk.Button(editar_trenes, text="GUARDAR CAMBIOS", command=guardar_cambios)
            boton_guardar.pack(pady=20)
        
        def eliminar_tren():
            eliminar_trenes = tk.Toplevel(root)
            eliminar_trenes.title("ELIMINAR TREN")
            eliminar_trenes.geometry(f"{ventana['ancho']}x{ventana['altura']}")
            eliminar_trenes.config(bg=colores["fondo"])

            ttk.Label(eliminar_trenes, text="Nombre del Tren a eliminar:").pack(pady=20)
            entry_nombre = ttk.Entry(eliminar_trenes)
            entry_nombre.pack()

            def confirmar_eliminar():
                target_name = entry_nombre.get()
                
                ruta_config = os.path.join(base_dir, "..", "config")
                archivo = os.path.join(ruta_config, "trenes.json")

                if not os.path.exists(archivo):
                    messagebox.showerror("Error", "No hay datos.")
                    return
                lista_trenes = []
                with open(archivo, "r", encoding="utf-8") as f:
                    lista_trenes = json.load(f)
                nueva_lista = [t for t in lista_trenes if t["nombre"] != target_name]

                if len(nueva_lista) == len(lista_trenes):
                    messagebox.showwarning("Error", "No se encontró ese tren.")
                else:
                    with open(archivo, "w", encoding="utf-8") as f:
                        json.dump(nueva_lista, f, indent=4)
                    messagebox.showinfo("Éxito", "Tren eliminado.")
                    eliminar_trenes.destroy()

            boton_guardar = ttk.Button(eliminar_trenes, text="ELIMINAR DEFINITIVAMENTE", command=confirmar_eliminar)
            boton_guardar.pack(pady=20)

        def ver_estado():
            v_estado = tk.Toplevel(root)
            v_estado.title("LISTADO DE TRENES")
            v_estado.geometry("400x400") 
            v_estado.config(bg=colores["fondo"])

            lbl_titulo = ttk.Label(v_estado, text="Base de Datos Actual:")
            lbl_titulo.pack(pady=10)

            texto1 = tk.Text(v_estado, width=40, height=15)
            texto1.pack(padx=10, pady=10)

            ruta_config = os.path.join(base_dir, "..", "config")
            archivo = os.path.join(ruta_config, "trenes.json")

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

        boton_crear = ttk.Button(ver_tren, text="Crear tren", command=crear_tren)
        boton_crear.pack(pady=10)

        boton_editar = ttk.Button(ver_tren, text="Editar tren", command=editar_tren)
        boton_editar.pack(pady=10)

        boton_eliminar = ttk.Button(ver_tren, text="Eliminar tren", command=eliminar_tren)
        boton_eliminar.pack(pady=10)

        boton_estado = ttk.Button(ver_tren, text="Estado", command=ver_estado)
        boton_estado.pack(pady=10)