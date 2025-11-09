from models.trenes import Tren
from models.estaciones import Estacion
from models.rutas import Ruta

class EstadoSimulacion:
    def __init__(self):
        self.hora_actual = "07:00"
        self.trenes = []
        self.estaciones = []
        self.rutas = []
        self.eventos = []

    def estado_inicial_simulacion(self):
        self.trenes = [
            Tren("Tren BMU", 160, 236),
            Tren("Tren EMU – EFE SUR", 120, 236)
        ]

        self.estaciones = [
            Estacion("Estación Central", "RM", 8242459),
            Estacion("Rancagua", "O’Higgins", 274407),
            Estacion("Talca", "Maule", 242344),
            Estacion("Chillán", "Ñuble", 204091)
        ]

        self.rutas = [
            Ruta("Estación Central", "Rancagua", 87),
            Ruta("Rancagua", "Talca", 200),
            Ruta("Talca", "Chillán", 180),
            Ruta("Chillán", "Talca", 180),
            Ruta("Talca", "Rancagua", 200),
            Ruta("Rancagua", "Estación Central", 87)
        ]
        conexiones = {
            "Estación Central": ["Rancagua", "Chillán"],
            "Rancagua": ["Talca", "Estación Central"],
            "Talca": ["Chillán", "Rancagua"],
            "Chillán": ["Talca", "Estación Central"]
        }

        for estacion in self.estaciones:
            if estacion.nombre in conexiones:
                for destino in conexiones[estacion.nombre]:
                    estacion.agregar_conexion(destino)

    def tiempo_avanzado(self, minutos):
        print(f"Ha avanzando {minutos} minutos")

    def registro_de_evento(self, descripcion):
        self.eventos.append(descripcion)
        print(f"Nuevo evento registrado: {descripcion}")
