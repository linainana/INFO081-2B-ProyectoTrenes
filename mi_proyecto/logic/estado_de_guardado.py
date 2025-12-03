import json
import os

class EstadoGuardado:
  def __init__(self, ruta_archivo="config/estado_guardado.json"):
    self.ruta_archivo = ruta_archivo


  def guardar(self, estado_simulacion):
    try:
      estado_dict = estado_simulacion.to_dict()
      carpeta = os.path.dirname(self.ruta_archivo)
      if carpeta:
        os.makedirs(carpeta, exist_ok=True)
      with open(self.ruta_archivo, "w", encoding="utf-8") as archivo_json:
        json.dump(estado_dict, archivo_json, indent=4, ensure_ascii=False)
    except Exception as e:
      print(f"Error al guardar en {self.ruta_archivo}: {e}")

  
  def cargar(self, clase_estado_simulacion):

    if not os.path.exists(self.ruta_archivo):
      print(f"No existe {self.ruta_archivo} - se utilizara estado por defecto.")
      return clase_estado_simulacion()

    try:
      with open(self.ruta_archivo, "r", encoding="utf-8") as archivo_json:
        data = json.load(archivo_json)
      print(f"Estado cargado desde {self.ruta_archivo}")
      estado = clase_estado_simulacion.from_dict(data)
      return estado
    except json.JSONDecodeError:
      print(f"Error al cargar {self.ruta_archivo} - se utilizara estado por defecto.")
      return clase_estado_simulacion()
    except Exception as e:
      print (f"Error al cargar {self.ruta_archivo}: {e}")
      return clase_estado_simulacion()
