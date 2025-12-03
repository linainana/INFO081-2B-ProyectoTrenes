from datetime import datetime

class Evento:
    def __init__(self, instante: datetime, tipo: str, datos: dict):
        self.id = None             
        self.instante = instante   
        self.tipo = tipo         
        self.datos = datos        
    def convertir_a_diccionario(self):
        return {
            "id": self.id,
            "instante": self.instante.isoformat(),
            "tipo": self.tipo,
            "datos": self.datos
        }
    
    @staticmethod
    def desde_diccionario(data: dict):
        instante = datetime.fromisoformat(data["instante"])
        evento = Evento(instante, data["tipo"], data["datos"])
        evento.id = data.get("id", None)
        return evento

    def __repr__(self):
        return (
            f"Evento(id={self.id}, "
            f"instante='{self.instante}', "
            f"tipo='{self.tipo}', "
            f"datos={self.datos})"
        )
