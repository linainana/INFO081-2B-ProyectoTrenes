import copy

class LíneaTiempo:
    def __init__(self, estado_simulacion):
        
        self.estado_inicial = estado_simulacion
        self.snapshots = {} 

    def guardar_snapshot(self, estado_simulacion, event_index):
        
        estado_dict = estado_simulacion.to_dict()
        self.snapshots[event_index] = copy.deepcopy(estado_dict)

    def crear_nueva_lineatiempo(self, event_index):
        if event_index not in self.snapshots:
            raise ValueError(f"No existe snapshot para el evento {event_index}")

        estado_guardado = self.snapshots[event_index]

        from logic.estado_de_simulacion import EstadoSimulacion
        nuevo_estado = EstadoSimulacion.from_dict(estado_guardado)

        return nuevo_estado
