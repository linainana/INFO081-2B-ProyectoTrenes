import heapq
from typing import List
from datetime import datetime
from logic.evento import Evento

class GestorEventos:

    def __init__(self):
        self._heap = []
        self._contador = 0 
        self.todos_los_eventos = []

    def crear_evento(self, instante, tipo, datos) -> Evento:
        evento = Evento(instante, tipo, datos, id_evento=self._contador)
        self._contador += 1
        return evento

    def agregar_evento(self, evento: Evento):
        heapq.heappush(self._heap, (evento.instante, evento.id, evento))
        self.todos_los_eventos.append(evento)

    def obtener_siguiente_evento(self) -> Evento:
        if not self._heap:
            return None
        _, _, evento = heapq.heappop(self._heap)
        return evento

    def ver_siguiente_evento(self):
        return self._heap[0][2] if self._heap else None

    def sin_evento(self):
        return len(self._heap) == 0

    def listar_eventos(self):
        return sorted(self.todos_los_eventos, key=lambda e: e.instante)

    def reemplazar_eventos_futuros(self, id_evento_corte: int, nuevos_eventos: List[Evento]):
        eventos_confirmados = [
            e for e in self.todos_los_eventos if e.id_evento <= id_evento_corte
        ]

        self.todos_los_eventos = eventos_confirmados + nuevos_eventos

        self._heap = []
        for e in self.listar_eventos():
            heapq.heappush(self._heap, (e.instante, e.id_evento, e))

