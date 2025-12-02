class Tren:
    def __init__(self, id_,nombre, velocidad, capacidad, ruta=None):
        self.id = id_
        self.nombre = nombre
        self.velocidad = velocidad
        self.capacidad_maxima = capacidad
        self.cantidad_pasajeros = 0
        self.ruta= ruta
        self.posicion = ruta.estaciones[0] if ruta else none

    def pasajeros_que_abordan(self, cantidad):
        if self.cantidad_pasajeros + cantidad <= self.capacidad_maxima:
            self.cantidad_pasajeros += cantidad
        else:
            print(f"El tren {self.nombre} llegó a su capacidad máxima.")

    def pasajeros_que_descienden(self, cantidad):
        self.cantidad_pasajeros = max(0, self.cantidad_pasajeros - cantidad)

    def descripcion_tren(self):
        ubicacion = self.posicion.nombre if sel.posicion else "Sin ruta"
        return f"{self.nombre} - Velocidad: {self.velocidad} km/h - f"Ocupación: {self.cantidad_pasajeros}/{self.capacidad_maxima}" - f"Ubicación:{ubicacion}")

    def avanzar(self):
        """Mueve el tren a la siguiente estación en su ruta."""
        if not self.ruta:
            print("Este tren no tiene ruta asignada.")
            return None

        siguiente = self.ruta.obtener_siguiente(self.posicion)
        if siguiente:
            self.posicion = siguiente
            return siguiente:
        else:
            print(f"El tren {self.nombre} ya llegó al final de la ruta.")
            return None
