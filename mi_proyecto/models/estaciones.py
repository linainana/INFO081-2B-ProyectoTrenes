from models.via import Via

class Estacion:
    def __init__(self, id_, nombre, region, poblacion):
        self.id = id_
        self.nombre = nombre
        self.region = region
        self.poblacion = poblacion
        
        self.conexiones = []  
        self.vias = []
        
        via_rotacion = Via(id_=f"{id_}_rotacion", es_rotacion=True)
        self.vias.append(via_rotacion)

    def agregar_via(self, via: Via):
        self.vias.append(via)

    def agregar_conexion(self, estacion_destino):
        if estacion_destino not in self.conexiones:
            self.conexiones.append(estacion_destino)

    def descripcion_estacion(self):
        return f"{self.nombre} ({self.region}) - Población: {self.poblacion}"
