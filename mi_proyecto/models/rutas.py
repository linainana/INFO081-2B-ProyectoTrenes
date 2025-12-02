class Ruta:
    def __init__(self, id_, estaciones, distancia_total=0):
        """
        id_ : identificador de la ruta
        estaciones : lista de objetos Estacion en orden
        distancia_total :  distancia total
        """
        self.id = id_
        self.estaciones = estaciones
        self.distancia_total = distancia_total

    def descripcion_ruta(self):
        nombres = "->".join([e.nombre for e in self.estaciones])
        return f"{nombres} ({self.distancia_total} km)"

    def obtener_siguiente(self, estacion_actual):
        """Devuelve la siguiente estación en la ruta"""
        if estacion_actual in self.estaciones:
            i = self.estaciones.index(estacion_actual)
            if i + 1 < len(self.estaciones):
                return self.estaciones[i+1]
        return None

        
