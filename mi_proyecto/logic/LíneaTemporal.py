import copy

class LíneaTiempo:
    """
    Maneja los snapshots de la simulación para permitir
    volver atrás y crear nuevas líneas temporales (RF09).
    """

    def __init__(self, estado_simulacion):
        # Guardamos el estado inicial como referencia
        self.estado_inicial = estado_simulacion
        self.snapshots = {} 

    def guardar_snapshot(self, estado_simulacion, event_index):
        # Convertimos el estado completo a diccionario
        estado_dict = estado_simulacion.to_dict()

        # Guardamos el diccionario directamente como snapshot
        self.snapshots[event_index] = copy.deepcopy(estado_dict)

    def crear_nueva_lineatiempo(self, event_index):
        if event_index not in self.snapshots:
            raise ValueError(f"No existe snapshot para el evento {event_index}")

        estado_guardado = self.snapshots[event_index]

        # Importamos aquí para evitar importaciones circulares
        from logic.estado_simulacion import EstadoSimulacion

        # Usamos from_dict() para reconstruir la simulación
        nuevo_estado = EstadoSimulacion.from_dict(estado_guardado)

        return nuevo_estado
