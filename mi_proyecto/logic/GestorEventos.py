import heapq
from typing import List
from datetime import datetime
from .event import Event

class GestorEventos:

    def __init__(self):
        self._heap = []
        self._contador = 0
        self.todos_los_eventos = []

    def agregar_evento(self, evento: Event):
        self._contador += 1
        evento.id = self._contador  #asigna id único
        heapq.heappush(self._heap, (evento.timestamp, self._contador, evento))
        self.todos_los_eventos.append(evento)   #lo guarda en historial

    def obtener_siguiente_evento(self) -> Event:
        if not self._heap:
            return None
        _, _, evento = heapq.heappop(self._heap)
        return evento

    def ver_siguiente_evento(self):
        return self._heap[0][2] if self._heap else None

    def sin_evento(self):
        return len(self._heap) == 0

    def listar_eventos(self):   #eventos ordenados cronológicamente
        return sorted(self.todos_los_eventos, key=lambda e: e.timestamp)

    def reemplazar_eventos_futuros(self, id_evento_corte: int, nuevos_eventos: List[Event]):
        eventos_confirmados = [
            e for e in self.todos_los_eventos
            if e.id and e.id <= id_evento_corte
        ]

        self.todos_los_eventos = eventos_confirmados + nuevos_eventos
        self._heap = []
        self._contador = 0
        for evento in self.listar_eventos(): 
            self._contador += 1
            evento.id = self._contador
            heapq.heappush(self._heap, (evento.timestamp, evento.id, evento))
