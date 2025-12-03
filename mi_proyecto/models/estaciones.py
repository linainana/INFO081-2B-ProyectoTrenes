from models.via import Via

class Estacion:
    def __init__(self, id_, nombre, region, poblacion, vias=None):
        self.id = id_
        self.nombre = nombre
        self.region = region
        self.poblacion = poblacion
        self.conexiones = []  
        self.vias = []

        if vias:
            for v in vias:
                nueva = Via(id_via=v["id"], estacion=self, capacidad=1)
                self.vias.append(nueva)

    def agregar_via(self, capacidad=1):
        nueva = Via(id_via=len(self.vias)+1, estacion=self, capacidad=capacidad)
        self.vias.append(nueva)

    def agregar_conexion(self, estacion_destino):
        if estacion_destino not in self.conexiones:
            self.conexiones.append(estacion_destino)

    def descripcion_estacion(self):
        return f"{self.nombre} ({self.region}) - Población: {self.poblacion}"
