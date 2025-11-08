class Tren:
    def __init__(self, nombre, velocidad, capacidad):
        self.nombre = nombre
        self.velocidad = velocidad
        self.capacidad_maxima = capacidad
        self.cantidad_pasajeros = 0

    def pasajeros_abordo(self, cantidad):
        if self.cantidad_pasajeros + cantidad <= self.capacidad_maxima:
            self.cantidad_pasajeros += cantidad
        else:
            print(f"El tren {self.nombre} llegó a su capacidad máxima.")

    def pasajeros_decendidos(self, cantidad):
        self.cantidad_pasajeros = max(0, self.cantidad_pasajeros - cantidad)

    def desripcion_tren(self):
        return f"{self.nombre} - Velocidad: {self.velocidad} km/h - Ocupación: {self.cantidad_pasajeros}/{self.capacidad_maxima}"
