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
        e1 = Estacion(1, "Estación Central", "RM", 8242459)
        e2 = Estacion(2, "Rancagua", "O’Higgins", 274407)
        e3 = Estacion(3, "Talca", "Maule", 242344)
        e4 = Estacion(4, "Chillán", "Ñuble", 204091)

        self.estaciones = [e1, e2, e3, e4]

        via1 = Via("V1", estacion=e1)
        via2 = Via("V2", estacion=e2)
        via3 = Via("V3", estacion=e3)
        via4 = Via("V4", estacion=e4)

        e1.agregar_via(via1)
        e2.agregar_via(via2)
        e3.agregar_via(via3)
        e4.agregar_via(via4)

        self.vias = [via1, via2, via3, via4]

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

        # Conexiones
        conexiones = {
            "Estación Central": ["Rancagua"],
            "Rancagua": ["Talca", "Estación Central"],
            "Talca": ["Chillán", "Rancagua"],
            "Chillán": ["Talca"]
        }

        for estacion in self.estaciones:
            if estacion.nombre in conexiones:
                for destino in conexiones[estacion.nombre]:
                    estacion.agregar_conexion(destino)

     def avanzar_tiempo(self, minutos=1):
        self.hora_actual += timedelta(minutes=minutos)

    def programar_evento(self, instante, tipo, datos):
        evento = Evento(instante, tipo, datos)
        self.gestor_eventos.agregar_evento(evento)

    def avanzar_siguiente_evento(self):
        evento = self.gestor_eventos.obtener_siguiente_evento()

        if evento is None:
            print("No hay más eventos")
            return None

        #Actualizar hora
        self.hora_actual = evento.instante

        #Guardarlo en historial
        self.eventos_confirmados.append(evento)

        #Despachar según tipo
        if evento.tipo == "movimiento_tren":
            self._procesar_movimiento_tren(evento)

        return evento

    def _procesar_movimiento_tren(self, evento):
        tren = evento.datos["tren"]
        
        estacion_anterior = tren.posicion
        estacion_nueva = tren.avanzar()

        if estacion_nueva:
            print(f"{tren.nombre} avanzó de {estacion_anterior.nombre} a {estacion_nueva.nombre}")
        else:
            print(f"{tren.nombre} llegó al final de su ruta")

    def retroceder_hasta_evento(self, id_evento):
        self.gestor_eventos.reemplazar_eventos_futuros(id_evento, nuevos_eventos=[])

        #Ajustar hora
        for e in self.eventos_confirmados:
            if e.id == id_evento:
                self.hora_actual = e.instante
                break

        #Recortar historial
        self.eventos_confirmados = [
            e for e in self.eventos_confirmados if e.id <= id_evento
        ]


