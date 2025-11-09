import json
import os

class EstadoGuardado:
  """
  Maneja la lectura y escritura del estado de la simulacion en JSON.
  """
  
  def __init__(self, ruta_archivo="config/estado_guardado.json"):
    self.ruta_archivo = ruta_archivo

  def guardar(self, estado):
    """
    Guarda el diccionario 'estado' en un archivo JSON.
    """

    try:
      carpeta=os.path.dirname(self.ruta_archivo)
      if carpeta:
        os.makedirs(carpeta, exist_ok=True)
      with open(self.ruta_archivo, "w", encoding="utf-8") as archivo_json:
        json.dump(estado, archivo_json, indent= 4, ensure_ascii=False)
    except Exception as e:
      print(f"Error al guardar en {self.ruta_archivo}:{e}")
  
  def cargar(self):
    """
    Carga y devuelve el diccionario con el estado desde el archivo JSON.
    Si no existe o está corrupto, devuelve un estado por defecto automaticamente.
    """

    if not os.path.exists(self.ruta_archivo):
      print(f"No existe {self.ruta_archivo} - se utilizara estado por defecto.")
      return self.estado_por_defecto()

    try:
      with open(self.ruta_archivo, "r", encoding="utf-8") as archivo_json:
        estado = json.load(archivo_json)
      print(f"Estado cargado desde {self.ruta_archivo}")
      return estado
    except json.JSONDecodeError:
      print(f"Error al cargar {self.ruta_archivo} - se utilizara estado por defecto.")
      return self.estado_por_defecto()
    except Exception as e:
      print (f"Error al cargar {self.ruta_archivo}: {e}")
      return self.estado_por_defecto()


  def estado_por_defecto(self):
    """
    Devuelve el estado inicial por defecto.
    """
    return {
      "tiempo": 0,
      "trenes_activos": 0,
      "pasajeros_totales": 0,
      "eventos": [],
      "en_ejecucion": False
    }
    



