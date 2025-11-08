from models.tren import Tren
from models.estacion import Estacion
from models.ruta import Ruta

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
            Tren("Tren EMU – EFE SUR", 120, 314)
        ]

        self.estaciones = [
            Estacion("Estación Central", "RM", 8242459),
            Estacion("Rancagua", "O’Higgins", 274407),
            Estacion("Talca", "Maule", 242344),
            Estacion("Chillan", "Ñuble", 204091)
        ]

        self.rutas = [
            Ruta("Estación Central", "Rancagua", 87)
        ]

    def tiempo_avanzado(self, minutos):
        print(f"Ha avanzando {minutos} minutos...")

    def registrao_de_evento(self, descripcion):
        self.eventos.append(descripcion)
        print(f"Nuevo evento registrado: {descripcion}")
