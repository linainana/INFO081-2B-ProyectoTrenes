class Via: 
  def __init__(self, id_via, estacion, capacidad=1):
    """
    id_via: identificador único de la vía
    estacion: objeto Estacion al que pertenece
    capacidad: cantidad de trenes que pueden usarla (normalmente 1)
    """
    self.id_via = id_via
    self.estacion = estacion
    self.capacidad = capacidad
    self.trenes_actuales = []

  def tren_ingresa(self, tren):
    """Intenta ingresar un tren a la vía."""
    if len(self.trenes_actuales) < self.capacidad:
      self.trenes_actuales.append(tren)
      return True
    return False 

  def trenes_sale(self, tren):
    """Saca un tren si está en la vía."""
    if tren in self.trenes_actuales:
      self.trenes_actuales.remove(tren)

  def descripcion_via(self):
    return f"Vía {self.id_via} en {self.estacion.nombre} - "
    (f"Ocupacion {len(self.trenes_actuales)}/{self.capacidad}")

