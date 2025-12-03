from datetime import datetime, timedelta
from logic.evento import Evento 
from logic.gestor_eventos import GestorEventos
from models.trenes import Tren
from models.estaciones import Estacion
from models.rutas import Ruta
from models.via import Via

class EstadoSimulacion:
     
    def __init__(self):
        self.hora_actual = datetime(2015, 3, 1, 7, 0)
        self.trenes = []
        self.estaciones = []
        self.rutas = []
        self.vias = []
        self.gestor_eventos = GestorEventos()
        self.eventos_confirmados = []

    def estado_inicial_simulacion(self):
        # 1. Crear Estaciones
        e1 = Estacion(1, "Estación Central", "RM", 8242459)
        e2 = Estacion(2, "Rancagua", "O’Higgins", 274407)
        e3 = Estacion(3, "Talca", "Maule", 242344)
        e4 = Estacion(4, "Chillán", "Ñuble", 204091)

        self.estaciones = [e1, e2, e3, e4]
     
        e1.agregar_via(capacidad=1)
        e2.agregar_via(capacidad=1)
        e3.agregar_via(capacidad=1)
        e4.agregar_via(capacidad=1)

        self.vias = [e1.vias[-1], e2.vias[-1], e3.vias[-1], e4.vias[-1]]

        self.rutas = [
            Ruta("R1", [e1,e2], distancia_total=87),
            Ruta("R2", [e2,e3], distancia_total=200),
            Ruta("R3", [e3,e4], distancia_total=180),
            Ruta("R4", [e4,e3], distancia_total=180),
            Ruta("R5", [e3,e2], distancia_total=200),
            Ruta("R6", [e2,e1], distancia_total=87)
        ]
        
        self.trenes = [
            Tren("T001", "Tren BMU", 160, 236, ruta=self.rutas[0]),
            Tren("T002", "Tren EMU – EFE SUR", 120, 236, ruta=self.rutas[1])
        ]
         
        for tren in self.trenes:
            estacion_inicial = tren.posicion
            if estacion_inicial and estacion_inicial.vias:
                via = estacion_inicial.vias[0]
                via.tren_ingresa(tren)
                
                tiempo_salida = self.hora_actual + timedelta(minutes=5)
                self.programar_evento(tiempo_salida, "movimiento_tren", {"tren": tren})

        conexiones = {
            "Estación Central": ["Rancagua"],
            "Rancagua": ["Talca", "Estación Central"],
            "Talca": ["Chillán", "Rancagua"],
            "Chillán": ["Talca"]
        }

        for estacion in self.estaciones:
            if estacion.nombre in conexiones:
                for destino_nom in conexiones[estacion.nombre]:
                    dest_obj = next((e for e in self.estaciones if e.nombre == destino_nom), None)
                    if dest_obj:
                        estacion.agregar_conexion(dest_obj)

    def programar_evento(self, instante, tipo, datos):
        evento = self.gestor_eventos.crear_evento(instante, tipo, datos)
        self.gestor_eventos.agregar_evento(evento)
        return evento

    def avanzar_siguiente_evento(self):
        evento = self.gestor_eventos.obtener_siguiente_evento()

        if evento is None:
            return None 

        self.hora_actual = evento.instante
        self.eventos_confirmados.append(evento)
         
        if evento.tipo == "movimiento_tren":
            return self._procesar_movimiento_tren(evento)

        return f"Evento: {evento.tipo}"

    def _procesar_movimiento_tren(self, evento):
        tren = evento.datos["tren"]
        estacion_anterior = tren.posicion
        
        estacion_nueva = tren.avanzar()

        if estacion_nueva:
            tiempo_viaje = 30 
            proximo_instante = self.hora_actual + timedelta(minutes=tiempo_viaje)
            self.programar_evento(proximo_instante, "movimiento_tren", {"tren": tren})
            
            return f"[{self.hora_actual.strftime('%H:%M')}] {tren.nombre} llegó a {estacion_nueva.nombre}"
        else:
            return f"[{self.hora_actual.strftime('%H:%M')}] {tren.nombre} terminó su recorrido."

    def crear_linea_temporal(self, id_evento):
        pass
    
    def to_dict(self):
        return {"hora": self.hora_actual.isoformat()}

