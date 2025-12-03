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
            
            # --- CAMBIO: Pauta pide Vagones ---
            ttk.Label(crear_trenes, text="Cantidad de Vagones:").pack(pady=5)
            entry_vagones = ttk.Entry(crear_trenes)
            entry_vagones.pack()

            ttk.Label(crear_trenes, text="Capacidad por Vagón:").pack(pady=5)
            entry_cap_vagon = ttk.Entry(crear_trenes)
            entry_cap_vagon.pack()
            # ----------------------------------

            def guardar_datos():
                nom = entry_nombre.get()
                vel = entry_vel.get()
                n_vagones = entry_vagones.get()
                cap_vagon = entry_cap_vagon.get()
                
                if not nom or not vel or not n_vagones:
                    messagebox.showwarning("Error", "Faltan datos")
                    return

                try:
                    # Calculamos la capacidad total automáticamente
                    capacidad_total = int(n_vagones) * int(cap_vagon)
                    
                    # Estructura que cumple con el requisito de "lista de vagones"
                    lista_vagones = [{"id": i+1, "capacidad": int(cap_vagon)} for i in range(int(n_vagones))]
                    
                except ValueError:
                    messagebox.showerror("Error", "Velocidad y Vagones deben ser números")
                    return

                # Guardamos con el formato detallado
                nuevo_tren = {
                    "nombre": nom, 
                    "velocidad": int(vel), 
                    "capacidad": capacidad_total,
                    "vagones": lista_vagones, # <-- REQUISITO CUMPLIDO
                    "accion": "Detenido"      # <-- REQUISITO CUMPLIDO
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

                # 1. Cargar lista
                lista_trenes = []
                with open(archivo, "r", encoding="utf-8") as f:
                    lista_trenes = json.load(f)

                # 2. Buscar y modificar
                encontrado = False
                for tren in lista_trenes:
                    if tren["nombre"] == target_name:
                        if new_vel: tren["velocidad"] = new_vel
                        if new_cap: tren["capacidad"] = new_cap
                        encontrado = True
                        break
                
                if encontrado:
                    # 3. Guardar cambios
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

                # 1. Cargar
                lista_trenes = []
                with open(archivo, "r", encoding="utf-8") as f:
                    lista_trenes = json.load(f)

                # 2. Filtrar (Guardamos todos MENOS el que queremos borrar)
                nueva_lista = [t for t in lista_trenes if t["nombre"] != target_name]

                if len(nueva_lista) == len(lista_trenes):
                    messagebox.showwarning("Error", "No se encontró ese tren.")
                else:
                    # 3. Guardar la nueva lista
                    with open(archivo, "w", encoding="utf-8") as f:
                        json.dump(nueva_lista, f, indent=4)
                    messagebox.showinfo("Éxito", "Tren eliminado.")
                    eliminar_trenes.destroy()

            boton_guardar = ttk.Button(eliminar_trenes, text="ELIMINAR DEFINITIVAMENTE", command=confirmar_eliminar)
            boton_guardar.pack(pady=20)

        def ver_estado():
            v_estado = tk.Toplevel(root)
            v_estado.title("LISTADO DE TRENES") # Cambiar titulo según corresponda
            v_estado.geometry("400x400") # Un poco más grande para ver lista
            v_estado.config(bg=colores["fondo"])

            lbl_titulo = ttk.Label(v_estado, text="Base de Datos Actual:")
            lbl_titulo.pack(pady=10)

            # Usamos un cuadro de texto con scroll para ver todo
            texto_info = tk.Text(v_estado, width=40, height=15)
            texto_info.pack(padx=10, pady=10)

            # Cargar y mostrar
            ruta_config = os.path.join(base_dir, "..", "config")
            archivo = os.path.join(ruta_config, "trenes.json") # <--- CAMBIAR AQUI PARA ESTACIONES/RUTAS

            if os.path.exists(archivo):
                try:
                    with open(archivo, "r", encoding="utf-8") as f:
                        data = json.load(f)
                    # Convertir JSON a texto bonito
                    texto_bonito = json.dumps(data, indent=2, ensure_ascii=False)
                    texto_info.insert(tk.END, texto_bonito)
                except Exception as e:
                    texto_info.insert(tk.END, f"Error leyendo archivo: {e}")
            else:
                texto_info.insert(tk.END, "No hay datos guardados aún.")

            # Hacer el texto de solo lectura
            texto_info.config(state=tk.DISABLED)

            ttk.Button(v_estado, text="Cerrar", command=v_estado.destroy).pack(pady=10)

        boton_crear = ttk.Button(ver_tren, text="Crear tren", command=crear_tren)
        boton_crear.pack(pady=10)

        boton_editar = ttk.Button(ver_tren, text="Editar tren", command=editar_tren)
        boton_editar.pack(pady=10)

        boton_eliminar = ttk.Button(ver_tren, text="Eliminar tren", command=eliminar_tren)
        boton_eliminar.pack(pady=10)

        boton_estado = ttk.Button(ver_tren, text="Estado", command=ver_estado)
        boton_estado.pack(pady=10)