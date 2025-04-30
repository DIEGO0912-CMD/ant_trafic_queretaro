import numpy as np

class PheromoneMap:
    def __init__(self, graph, initial_pheromone=0.1):
        self.pheromones = {}
        for u, v in graph.edges():
            self.pheromones[(u, v)] = initial_pheromone

    def evaporar(self, tasa=0.1):
        for key in self.pheromones:
            self.pheromones[key] *= (1 - tasa)

    def depositar(self, ruta, cantidad):
        for i in range(len(ruta) - 1):
            edge = (ruta[i], ruta[i+1])
            self.pheromones[edge] += cantidad
