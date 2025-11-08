class Ruta:
    def __init__(self, origen, destino, distancia):
        self.origen = origen
        self.destino = destino
        self.distancia = distancia

    def descripcion_ruta(self):
        return f"{self.origen} → {self.destino} ({self.distancia} km)"
