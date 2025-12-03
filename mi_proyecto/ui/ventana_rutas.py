
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import json
import os

base_dir = os.path.dirname(__file__)

def ver_rutas(root, ventana, colores):
        ver_ruta = tk.Toplevel(root)
        ver_ruta.title("RUTAS")
        ver_ruta.geometry(f"{ventana['ancho']}x{ventana['altura']}")
        ver_ruta.config(bg=colores["fondo"])

        ttk.Label(ver_ruta, text="VER RUTAS").pack(pady=20)
        ttk.Label(ver_ruta, text="TRENES").pack(padx=50, pady=20)
    
        def crear_rutas():
            crear_ruta = tk.Toplevel(root)
            crear_ruta.title("CREAR RUTA")
            crear_ruta.geometry(f"{ventana['ancho']}x{ventana['altura']}")
            crear_ruta.config(bg=colores["fondo"])

            ttk.Label(crear_ruta, text="Estación de Origen:").pack(pady=5)
            e_ori = ttk.Entry(crear_ruta)
            e_ori.pack()
            
            ttk.Label(crear_ruta, text="Estación de Destino:").pack(pady=5)
            e_dest = ttk.Entry(crear_ruta)
            e_dest.pack()
            
            ttk.Label(crear_ruta, text="Longitud (kms):").pack(pady=5)
            e_dist = ttk.Entry(crear_ruta)
            e_dist.pack()

            def guardar():
                ori = e_ori.get().strip()
                dest = e_dest.get().strip()
                dist_str = e_dist.get().strip()

                if not ori or not dest or not dist_str:
                    messagebox.showwarning("Error", "Todos los campos son obligatorios.")
                    return
                
                try:
                    distancia_km = int(dist_str)
                except ValueError:
                    messagebox.showerror("Error", "La distancia debe ser un número entero.")
                    return
                
                nueva_ruta = {
                    "origen": ori,
                    "destino": dest,
                    "distancia": distancia_km
                }
                
                ruta_config = os.path.join(base_dir, "..", "config")
                if not os.path.exists(ruta_config):
                    os.makedirs(ruta_config)
                    
                archivo = os.path.join(ruta_config, "rutas.json")
                
                lista = []
                if os.path.exists(archivo):
                    try:
                        with open(archivo, "r", encoding="utf-8") as f: 
                            lista = json.load(f)
                    except Exception as e:
                        print(f"Error leyendo rutas previas: {e}")              
                lista.append(nueva_ruta)
                
                with open(archivo, "w", encoding="utf-8") as f: 
                    json.dump(lista, f, indent=4)
                
                messagebox.showinfo("Éxito", f"Ruta de {ori} a {dest} guardada.")
                crear_ruta.destroy()
            ttk.Button(crear_ruta, text="GUARDAR RUTA", command=guardar).pack(pady=20)
        
        def editar_rutas():
            edit_ruta = tk.Toplevel(root)
            edit_ruta.title("EDITAR RUTA")
            edit_ruta.geometry(f"{ventana['ancho']}x{ventana['altura']}")
            edit_ruta.config(bg=colores["fondo"])

            ttk.Label(edit_ruta, text="Origen de la ruta a editar:").pack(pady=5)
            e_ori_target = ttk.Entry(edit_ruta)
            e_ori_target.pack()
            
            ttk.Label(edit_ruta, text="Destino de la ruta a editar:").pack(pady=5)
            e_dest_target = ttk.Entry(edit_ruta)
            e_dest_target.pack()
            
            ttk.Label(edit_ruta, text="NUEVA Distancia (km):").pack(pady=5)
            e_dist_new = ttk.Entry(edit_ruta)
            e_dist_new.pack()

            def guardar():
                t_ori = e_ori_target.get()
                t_dest = e_dest_target.get()
                new_dist = e_dist_new.get()

                ruta_config = os.path.join(base_dir, "..", "config")
                archivo = os.path.join(ruta_config, "rutas.json")

                if not os.path.exists(archivo):
                    messagebox.showerror("Error", "No hay rutas.")
                    return

                with open(archivo, "r", encoding="utf-8") as f:
                    lista = json.load(f)

                encontrado = False
                for r in lista:
                    # Buscamos que coincida origen Y destino
                    if r["origen"] == t_ori and r["destino"] == t_dest:
                        if new_dist: r["distancia"] = int(new_dist)
                        encontrado = True
                        break
                
                if encontrado:
                    with open(archivo, "w", encoding="utf-8") as f:
                        json.dump(lista, f, indent=4)
                    messagebox.showinfo("Éxito", "Ruta actualizada.")
                    edit_ruta.destroy()
                else:
                    messagebox.showwarning("Error", "No se encontró esa ruta específica.")

            ttk.Button(edit_ruta, text="GUARDAR CAMBIOS", command=guardar).pack(pady=20)

        def eliminar_rutas():
            elim_ruta = tk.Toplevel(root)
            elim_ruta.title("ELIMINAR RUTA")
            elim_ruta.geometry(f"{ventana['ancho']}x{ventana['altura']}")
            elim_ruta.config(bg=colores["fondo"])

            ttk.Label(elim_ruta, text="Origen de la ruta:").pack(pady=5)
            e_ori = ttk.Entry(elim_ruta)
            e_ori.pack()
            
            ttk.Label(elim_ruta, text="Destino de la ruta:").pack(pady=5)
            e_dest = ttk.Entry(elim_ruta)
            e_dest.pack()

            def confirmar():
                t_ori = e_ori.get()
                t_dest = e_dest.get()
                
                ruta_config = os.path.join(base_dir, "..", "config")
                archivo = os.path.join(ruta_config, "rutas.json")

                if not os.path.exists(archivo): return

                with open(archivo, "r", encoding="utf-8") as f:
                    lista = json.load(f)

                nueva_lista = [r for r in lista if not (r["origen"] == t_ori and r["destino"] == t_dest)]

                if len(nueva_lista) == len(lista):
                    messagebox.showwarning("Error", "Ruta no encontrada.")
                else:
                    with open(archivo, "w", encoding="utf-8") as f:
                        json.dump(nueva_lista, f, indent=4)
                    messagebox.showinfo("Éxito", "Ruta eliminada.")
                    elim_ruta.destroy()

            ttk.Button(elim_ruta, text="ELIMINAR", command=confirmar).pack(pady=20)
        
        def ver_estado():
            v_estado = tk.Toplevel(root)
            v_estado.title("LISTADO DE RUTAS") 
            v_estado.geometry("400x400") 
            v_estado.config(bg=colores["fondo"])

            lbl_titulo = ttk.Label(v_estado, text="Base de Datos Actual:")
            lbl_titulo.pack(pady=10)

            texto_info = tk.Text(v_estado, width=40, height=15)
            texto_info.pack(padx=10, pady=10)

            ruta_config = os.path.join(base_dir, "..", "config")
            archivo = os.path.join(ruta_config, "rutas.json") 

            if os.path.exists(archivo):
                try:
                    with open(archivo, "r", encoding="utf-8") as f:
                        data = json.load(f)
                    texto_bonito = json.dumps(data, indent=2, ensure_ascii=False)
                    texto_info.insert(tk.END, texto_bonito)
                except Exception as e:
                    texto_info.insert(tk.END, f"Error leyendo archivo: {e}")
            else:
                texto_info.insert(tk.END, "No hay datos guardados aún.")
            texto_info.config(state=tk.DISABLED)

            ttk.Button(v_estado, text="Cerrar", command=v_estado.destroy).pack(pady=10)
        
        boton_crear = ttk.Button(ver_ruta, text="Crear ruta", command=crear_rutas)
        boton_crear.pack(pady=10)

        boton_editar = ttk.Button(ver_ruta, text="Editar ruta", command=editar_rutas)
        boton_editar.pack(pady=10)

        boton_eliminar = ttk.Button(ver_ruta, text="Eliminar ruta", command=eliminar_rutas)
        boton_eliminar.pack(pady=10)

        boton_estado = ttk.Button(ver_ruta, text="Estado", command=ver_estado)
        boton_estado.pack(pady=10)