from datetime import datetime

class Evento:
    def __init__(self, instante: datetime, tipo: str, datos: dict, id_evento=None):
        self.id_evento = id_evento 
        self.instante = instante   
        self.tipo = tipo          
        self.datos = datos               

    def convertir_a_diccionario(self):
        return {
            "id_evento": self.id_evento,
            "instante": self.instante.isoformat(),
            "tipo": self.tipo,
            "datos": self.datos
        }
    
    @staticmethod
    def desde_diccionario(data: dict):
        instante = datetime.fromisoformat(data["instante"])
        evento = Evento(
            instante, 
            data["tipo"], 
            data["datos"], 
            id_evento=data.get("id_evento", None)
        )
        return evento

    def __repr__(self):
        return (
            f"Evento(id_evento={self.id_evento}, "
            f"instante='{self.instante}', "
            f"tipo='{self.tipo}', "
            f"datos={self.datos})"
        )
