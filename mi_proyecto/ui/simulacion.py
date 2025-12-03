import tkinter as tk
from tkinter import messagebox, ttk
import sys
import os
import math

def iniciar_simulacion_en_frame(frame_padre):
    
    # 1. IMPORTACIÓN SEGURA DE LA LÓGICA
    ruta_actual = os.path.dirname(os.path.abspath(__file__))
    ruta_raiz = os.path.dirname(ruta_actual)
    if ruta_raiz not in sys.path:
        sys.path.append(ruta_raiz)

    try:
        from logic.estado_de_simulacion import EstadoSimulacion
        
        # Instanciamos la clase lógica
        simulacion = EstadoSimulacion()
        
        # Función interna para recargar datos frescos desde JSON
        def cargar_datos_frescos():
            simulacion.estado_inicial_simulacion() # Lee JSON
            # Si hay datos, planifica viaje de prueba automáticamente
            if simulacion.trenes and simulacion.rutas:
                simulacion.cola_eventos = [] # Limpiar eventos viejos
                r = simulacion.rutas[0]
                t = simulacion.trenes[0]
                simulacion.planificar_viaje(t, r.origen, r.destino, simulacion.hora_actual)

        # Carga inicial al abrir
        cargar_datos_frescos()

        # ==========================================
        # 2. ESTRUCTURA VISUAL (INTERFAZ)
        # ==========================================
        panel_principal = tk.PanedWindow(frame_padre, orient=tk.HORIZONTAL)
        panel_principal.pack(fill="both", expand=True)

        # --- COLUMNA IZQUIERDA (Datos y Controles) ---
        frame_izq = tk.Frame(panel_principal, width=320)
        panel_principal.add(frame_izq)

        # Panel de Estadísticas (Arriba a la izquierda)
        frame_stats = tk.Frame(frame_izq, bg="#f0f0f0", bd=2, relief="groove")
        frame_stats.pack(fill="x", padx=5, pady=5)
        
        lbl_reloj = tk.Label(frame_stats, text="07:00", font=("Arial", 16, "bold"), bg="#f0f0f0", fg="#333")
        lbl_reloj.pack(pady=5)
        
        lbl_info = tk.Label(frame_stats, text="Cargando...", bg="#f0f0f0", font=("Arial", 9))
        lbl_info.pack(pady=5)

        # --- AQUÍ ESTÁ EL BOTÓN QUE TE FALTABA ---
        def btn_recargar_click():
            cargar_datos_frescos()     # Recarga la lógica
            refrescar_pantalla()       # Redibuja el mapa
            messagebox.showinfo("Actualizado", "Datos recargados desde archivos JSON.")

        btn_refresh = tk.Button(frame_stats, text="🔄 Recargar Datos Nuevos", command=btn_recargar_click, bg="orange", fg="black")
        btn_refresh.pack(fill="x", padx=10, pady=5)
        # ------------------------------------------

        # Lista de Eventos
        tk.Label(frame_izq, text="Cola de Eventos:", font=("Arial", 10, "bold")).pack(anchor="w", padx=5)
        lista_box = tk.Listbox(frame_izq, height=15, font=("Consolas", 9))
        lista_box.pack(fill="both", expand=True, padx=5, pady=5)
        
        # Botones de Control (Avanzar)
        frame_btn = tk.Frame(frame_izq)
        frame_btn.pack(fill="x", pady=10)

        # --- COLUMNA DERECHA (MAPA) ---
        frame_der = tk.Frame(panel_principal, bg="white")
        panel_principal.add(frame_der)
        
        tk.Label(frame_der, text="Mapa de la Red (Vista Satelital)", bg="white", font=("Arial", 10, "bold")).pack(pady=5)
        
        canvas_mapa = tk.Canvas(frame_der, bg="#e6e6e6", width=500, height=400)
        canvas_mapa.pack(fill="both", expand=True, padx=10, pady=10)

        # ==========================================
        # 3. LÓGICA DE DIBUJADO (MAPA + TRENES + PASAJEROS)
        # ==========================================
        coords_estaciones = {} 

        def dibujar_mapa():
            canvas_mapa.delete("all")
            num_est = len(simulacion.estaciones)
            
            if num_est == 0: 
                canvas_mapa.create_text(250, 200, text="No hay estaciones cargadas.\nVe a 'Gestión' y crea una.", justify="center")
                return

            centro_x, centro_y = 250, 200
            radio = 150
            angulo_paso = 360 / num_est

            # A) Calcular posiciones y Dibujar Rutas (Fondo)
            for i, est in enumerate(simulacion.estaciones):
                angulo_rad = math.radians(i * angulo_paso)
                x = centro_x + radio * math.cos(angulo_rad)
                y = centro_y + radio * math.sin(angulo_rad)
                coords_estaciones[est.nombre] = (x, y)

            for ruta in simulacion.rutas:
                if ruta.origen in coords_estaciones and ruta.destino in coords_estaciones:
                    x1, y1 = coords_estaciones[ruta.origen]
                    x2, y2 = coords_estaciones[ruta.destino]
                    canvas_mapa.create_line(x1, y1, x2, y2, fill="#bdc3c7", width=4)
                    mx, my = (x1+x2)/2, (y1+y2)/2
                    canvas_mapa.create_text(mx, my, text=f"{ruta.distancia}km", font=("Arial", 8), fill="gray")

            # B) Dibujar Estaciones y Pasajeros
            for est in simulacion.estaciones:
                if est.nombre in coords_estaciones:
                    x, y = coords_estaciones[est.nombre]
                    
                    # Círculo Estación
                    r = 20
                    canvas_mapa.create_oval(x-r, y-r, x+r, y+r, fill="#3498db", outline="white", width=2)
                    canvas_mapa.create_text(x, y-30, text=est.nombre, font=("Arial", 9, "bold"), fill="#2c3e50")
                    
                    # Indicador de Pasajeros Esperando (Rojo)
                    pax = est.pasajeros_esperando
                    if pax > 0:
                        canvas_mapa.create_text(x+25, y, text=f"👤{pax}", font=("Arial", 10, "bold"), fill="#c0392b", anchor="w")

            # C) Dibujar Trenes (Cuadrados Naranjas)
            for tren in simulacion.trenes:
                # Solo dibujamos si está en una estación (no en tránsito)
                if tren.ubicacion_actual in coords_estaciones:
                    tx, ty = coords_estaciones[tren.ubicacion_actual]
                    tr = 12
                    canvas_mapa.create_rectangle(tx-tr, ty-tr, tx+tr, ty+tr, fill="#f39c12", outline="black")
                    canvas_mapa.create_text(tx, ty-18, text=tren.nombre[:6], font=("Arial", 7), fill="black")

        # ==========================================
        # 4. ACTUALIZACIÓN PANTALLA
        # ==========================================
        def refrescar_pantalla():
            # Reloj
            try: hora = simulacion.hora_actual.strftime("%d/%m %H:%M")
            except: hora = str(simulacion.hora_actual)
            lbl_reloj.config(text=hora)
            
            # Info Stats
            lbl_info.config(text=f"Estaciones: {len(simulacion.estaciones)} | Trenes: {len(simulacion.trenes)}")

            # Lista
            lista_box.delete(0, tk.END)
            for evt in simulacion.cola_eventos:
                try: h = evt.tiempo.strftime("%H:%M")
                except: h = "??"
                lista_box.insert(tk.END, f"[{h}] {evt.descripcion}")
            
            # Mapa
            dibujar_mapa()

        def btn_avanzar_click():
            msg = simulacion.avanzar_siguiente_evento()
            refrescar_pantalla()
            if isinstance(msg, str):
                messagebox.showinfo("Simulación", msg)

        # --- NUEVO: Función para abrir ventanita de programar viaje ---
        def btn_planificar_click():
            # Validar que existan datos
            if not simulacion.trenes or not simulacion.estaciones:
                messagebox.showwarning("Error", "Primero debe crear Trenes y Estaciones en la pestaña 'Gestión'.")
                return

            win = tk.Toplevel()
            win.title("Programar Salida")
            win.geometry("300x300")

            # 1. Elegir Tren
            ttk.Label(win, text="Seleccione Tren:").pack(pady=5)
            nombres_trenes = [t.nombre for t in simulacion.trenes]
            cb_tren = ttk.Combobox(win, values=nombres_trenes, state="readonly")
            cb_tren.pack()
            if nombres_trenes: cb_tren.current(0)

            # 2. Elegir Origen
            ttk.Label(win, text="Estación Origen:").pack(pady=5)
            nombres_est = [e.nombre for e in simulacion.estaciones]
            cb_origen = ttk.Combobox(win, values=nombres_est, state="readonly")
            cb_origen.pack()
            if nombres_est: cb_origen.current(0)

            # 3. Elegir Destino
            ttk.Label(win, text="Estación Destino:").pack(pady=5)
            cb_destino = ttk.Combobox(win, values=nombres_est, state="readonly")
            cb_destino.pack()

            def confirmar():
                t_nombre = cb_tren.get()
                ori = cb_origen.get()
                dest = cb_destino.get()

                if ori == dest:
                    messagebox.showerror("Error", "Origen y Destino no pueden ser iguales")
                    return

                # Buscar el objeto tren real
                tren_obj = next((t for t in simulacion.trenes if t.nombre == t_nombre), None)
                
                # Llamar a la lógica (Esto crea los EVENTOS de Salida y Llegada)
                mensaje = simulacion.planificar_viaje(tren_obj, ori, dest, simulacion.hora_actual)
                
                # Mostrar resultado y actualizar lista de eventos
                if "Error" in mensaje or "BLOQUEO" in mensaje:
                    messagebox.showerror("Problema", mensaje)
                else:
                    messagebox.showinfo("Éxito", mensaje)
                    refrescar_pantalla() # <--- IMPORTANTE: Actualiza la lista visual
                    win.destroy()

            ttk.Button(win, text="PROGRAMAR VIAJE", command=confirmar).pack(pady=20)
        # ---------------------------------------------------------------

        # BOTONERA
        # Botón Nuevo: Programar
        btn_plan = tk.Button(frame_btn, text="+ Programar Viaje", 
                             bg="#3498db", fg="white", font=("Arial", 10),
                             command=btn_planificar_click)
        btn_plan.pack(side="left", padx=5, fill="x", expand=True)

        # Botón Existente: Avanzar
        btn_avanzar = tk.Button(frame_btn, text=">> AVANZAR EVENTO >>", 
                        bg="green", fg="white", font=("Arial", 10, "bold"),
                        command=btn_avanzar_click)
        btn_avanzar.pack(side="left", padx=5, fill="x", expand=True)

        # Iniciar todo visualmente
        refrescar_pantalla()

    except Exception as e:
        tk.Label(frame_padre, text=f"Error en simulación: {e}", fg="red").pack()
        print(f"Error detallado: {e}")