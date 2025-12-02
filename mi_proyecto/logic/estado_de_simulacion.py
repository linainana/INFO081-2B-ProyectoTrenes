from models.trenes import Tren
from models.estaciones import Estacion
from models.rutas import Ruta

class EstadoSimulacion:
    def __init__(self):
        self.hora_actual = 7 * 60
        self.trenes = []
        self.estaciones = []
        self.rutas = []
        self.eventos = []

    def estado_inicial_simulacion(self):
       
        e1 = Estacion(1, "Estación Central", "RM", 8242459),
        e2 = Estacion(2, "Rancagua", "O’Higgins", 274407),
        e3 = Estacion(3, "Talca", "Maule", 242344),
        e4 = Estacion(4, "Chillán", "Ñuble", 204091)

        self.estaciones = [e1, e2, e3, e4]
        
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
        self.hora_actual += minutos

    def registro_de_evento(self, descripcion):
        evento = {
            "hora": self.hora_actual,
            "descripcion": descripcion
        }
        self.eventos.append(evento)

    def avanzar_evento_tren(self, tren):
        estacion_anterior = tren.posicion
        estacion_nueva = tren.avanzar()
        
        if estacion_nueva:
            self.registrar_evento(
                f"El tren {tren.nombre} avanzó de {estacion_anterior.nombre} a {estacion_nueva.nombre}"
            )
        else:
            self.registrar_evento(
                f"El tren {tren.nombre} lleg´po al final de la ruta"
            )

