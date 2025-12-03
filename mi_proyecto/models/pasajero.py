class Pasajero:
  def __init__(self, id_pasajero, origen, destino, hora_llegada):
    self.id = id_pasajero
    self.origen = origen
    self.destino = destino
    self.hora_llegada = hora_llegada


  def descripcion_pasajero(self):
    return (f"Pasajero {self.id}: {self.origen.nombre} -> {self.destino.nombre}, "
            f"hora llegada {self.hora_llegada}")
