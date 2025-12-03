class Tren:
    def __init__(self, id_,nombre, velocidad, capacidad, ruta=None):
        self.id = id_
        self.nombre = nombre
        self.velocidad = velocidad
        self.capacidad_maxima = capacidad
        self.cantidad_pasajeros = 0
        self.ruta= ruta
        self.posicion = ruta.estaciones[0] if ruta else None
        self.via_actual = None

    def pasajeros_que_abordan(self, cantidad):
        if self.cantidad_pasajeros + cantidad <= self.capacidad_maxima:
            self.cantidad_pasajeros += cantidad
        else:
            print(f"El tren {self.nombre} llegó a su capacidad máxima.")

    def pasajeros_que_descienden(self, cantidad):
        self.cantidad_pasajeros = max(0, self.cantidad_pasajeros - cantidad)

    def descripcion_tren(self):
        ubicacion = self.posicion.nombre if self.posicion else "Sin ruta"
        via = self.via_actual.id_via if self.via_actual else "--"
        return (
            f"{self.nombre} - Velocidad: {self.velocidad} km/h - "
            f"Ocupación: {self.cantidad_pasajeros}/{self.capacidad_maxima} - "
            f"Ubicación: {ubicacion} (Vía {via})"
        )

    def avanzar(self):
        """Mueve el tren a la siguiente estación en su ruta."""
        if not self.ruta:
            print("Este tren no tiene ruta asignada.")
            return None
        if self.posicion not in self.ruta.estaciones:
            print("La posición actual no está en la ruta.")
            return None

        estaciones = self.ruta.estaciones
        idx = estaciones.index(self.posicion)
        
        if idx + 1 >= len(estaciones):
            print(f"El tren {self.nombre} llegó al final de su ruta.")
            return None
        
        estacion_anterior = self.posicion
        estacion_nueva = estaciones[idx+ 1]
        
        if self.via_actual:
            self.via_actual.trenes_sale(self)
            self.via_actual = None
        
        self.posicion = estacion_nueva
        
        if estacion_nueva.vias:
            via_destino = estacion_nueva.vias[0]
            
            if via_destino.tren_ingresa(self):
                self.via_actual = via_destino
            else:
                print(f" La vía en {estacion_nueva.nombre} está ocupada. Tren queda sin vía asignada.")
                self.via_actual = None
                
        return estacion_nueva
                

