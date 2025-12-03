from datetime import datetime, timedelta
from logic.evento import Evento
from logic.gestor_eventos import GestorEventos
from logic.Líneatemporal import lineatemporal
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
        self.timeline = TimeLine(self)

    def estado_inicial_simulacion(self):
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

    def programar_evento(self, instante, tipo, datos):
        """Correcto: crear evento directamente sin método inexistente."""
        evento = Evento(instante, tipo, datos)
        self.gestor_eventos.agregar_evento(evento)
        return evento

    def avanzar_siguiente_evento(self):
        evento = self.gestor_eventos.obtener_siguiente_evento()

        if evento is None:
            print("No hay más eventos")
            return None

        self.hora_actual = evento.instante
        self.eventos_confirmados.append(evento)
         
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

    def crear_linea_temporal(self, id_evento):
        """
        Crea una nueva simulación exactamente como estaba en el
        evento con ID = id_evento.
        """
        return self.timeline.create_new_timeline(id_evento)

    def to_dict(self):
        return {
            "hora_actual": self.hora_actual.isoformat(),
            "eventos_confirmados": [e.convertir_a_diccionario() for e in self.eventos_confirmados],
            "eventos_futuros": [ev.convertir_a_diccionario() for ev in self.gestor_eventos.todos_los_eventos],
        }
    @staticmethod
    def from_dict(data):
        estado = EstadoSimulacion()
        estado.hora_actual = datetime.fromisoformat(data["hora_actual"])
        for ev_data in data["eventos_futuros"]:
            ev = Evento.desde_diccionario(ev_data)
            estado.gestor_eventos.agregar_evento(ev)

        for ev_data in data["eventos_confirmados"]:
            ev = Evento.desde_diccionario(ev_data)
            estado.eventos_confirmados.append(ev)
        return estado

