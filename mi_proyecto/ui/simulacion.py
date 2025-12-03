import tkinter as tk
from tkinter import messagebox, ttk
import sys
import os
import math

def iniciar_simulacion_en_frame(frame_padre):

    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if base_dir not in sys.path:
        sys.path.append(base_dir)

    try:
        from logic.estado_de_simulacion import EstadoSimulacion
 
        simulacion = EstadoSimulacion()
        simulacion.estado_inicial_simulacion()

        panel_principal = tk.PanedWindow(frame_padre, orient=tk.HORIZONTAL)
        panel_principal.pack(fill="both", expand=True)

        frame_izq = tk.Frame(panel_principal, width=320)
        panel_principal.add(frame_izq)

        frame_stats = tk.Frame(frame_izq, bg="#f0f0f0", bd=2, relief="groove")
        frame_stats.pack(fill="x", padx=5, pady=5)
        
        lbl_reloj = tk.Label(frame_stats, text="07:00", font=("Arial", 16, "bold"), bg="#f0f0f0", fg="#333")
        lbl_reloj.pack(pady=5)

        tk.Label(frame_izq, text="Historial de Eventos:", font=("Arial", 10, "bold")).pack(anchor="w", padx=5)
        lista_box = tk.Listbox(frame_izq, height=15, font=("Consolas", 9))
        lista_box.pack(fill="both", expand=True, padx=5, pady=5)
 
        frame_btn = tk.Frame(frame_izq)
        frame_btn.pack(fill="x", pady=10)

        frame_der = tk.Frame(panel_principal, bg="white")
        panel_principal.add(frame_der)
        
        tk.Label(frame_der, text="Mapa de la Red", bg="white", font=("Arial", 10, "bold")).pack(pady=5)
        canvas_mapa = tk.Canvas(frame_der, bg="#e6e6e6", width=500, height=400)
        canvas_mapa.pack(fill="both", expand=True, padx=10, pady=10)

        coords_estaciones = {} 

        def dibujar_mapa():
            canvas_mapa.delete("all")
            estaciones = simulacion.estaciones
            num_est = len(estaciones)
            
            if num_est == 0: 
                canvas_mapa.create_text(250, 200, text="No hay estaciones cargadas.", justify="center")
                return

            centro_x, centro_y = 250, 200
            radio = 150
            angulo_paso = 360 / num_est

            for i, est in enumerate(estaciones):
                angulo_rad = math.radians(i * angulo_paso)
                x = centro_x + radio * math.cos(angulo_rad)
                y = centro_y + radio * math.sin(angulo_rad)
                coords_estaciones[est.nombre] = (x, y)

            for ruta in simulacion.rutas:

                lista_puntos = ruta.estaciones 
                
                if len(lista_puntos) > 1:
                    for i in range(len(lista_puntos) - 1):
                        est_a = lista_puntos[i]
                        est_b = lista_puntos[i+1]
                        if est_a.nombre in coords_estaciones and est_b.nombre in coords_estaciones:
                            x1, y1 = coords_estaciones[est_a.nombre]
                            x2, y2 = coords_estaciones[est_b.nombre]
 
                            canvas_mapa.create_line(x1, y1, x2, y2, fill="#bdc3c7", width=4)

            for est in estaciones:
                if est.nombre in coords_estaciones:
                    x, y = coords_estaciones[est.nombre]
                    r = 20
                    canvas_mapa.create_oval(x-r, y-r, x+r, y+r, fill="#3498db", outline="white", width=2)
                    canvas_mapa.create_text(x, y-30, text=est.nombre, font=("Arial", 9, "bold"), fill="#2c3e50")

            for tren in simulacion.trenes:
                if tren.posicion and tren.posicion.nombre in coords_estaciones:
                    tx, ty = coords_estaciones[tren.posicion.nombre]
   
                    tr = 12
                    canvas_mapa.create_rectangle(tx-tr, ty-tr, tx+tr, ty+tr, fill="#f39c12", outline="black")
                    canvas_mapa.create_text(tx, ty-18, text=tren.nombre[:6], font=("Arial", 8), fill="black")
        def refrescar_pantalla():

            try: hora = simulacion.hora_actual.strftime("%H:%M")
            except: hora = str(simulacion.hora_actual)
            lbl_reloj.config(text=hora)
  
            lista_box.delete(0, tk.END)
            ultimos = simulacion.eventos_confirmados[-15:]
            for evt in ultimos:
                try: h = evt.instante.strftime("%H:%M")
                except: h = "??"

                desc = f"{evt.tipo}"
                if isinstance(evt.datos, dict) and "tren" in evt.datos:
                     desc += f" | {evt.datos['tren'].nombre}"
                
                lista_box.insert(tk.END, f"[{h}] {desc}")
            
            dibujar_mapa()

        def btn_avanzar_click():
            evento = simulacion.avanzar_siguiente_evento()
            if evento:
                refrescar_pantalla()
            else:
                messagebox.showinfo("Fin", "No hay más eventos pendientes.")

        btn = tk.Button(frame_btn, text=">> AVANZAR EVENTO >>", 
                        bg="green", fg="white", font=("Arial", 11, "bold"),
                        command=btn_avanzar_click)
        btn.pack(side="left", padx=10, fill="x", expand=True)
        refrescar_pantalla()

    except Exception as e:
        tk.Label(frame_padre, text=f"Error: {e}", fg="red").pack()
        print(f"Error UI: {e}")