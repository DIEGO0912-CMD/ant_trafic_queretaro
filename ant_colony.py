import numpy as np
import networkx as nx
import random

class AntColony:
    def __init__(self, graph, pheromone_map, n_ants=20, alpha=1.0, beta=2.0):
        self.graph = graph
        self.pheromones = pheromone_map
        self.n_ants = n_ants
        self.alpha = alpha
        self.beta = beta

    def correr_iteracion(self, origen, destino):
        rutas = []
        for _ in range(self.n_ants):
            ruta = self.construir_ruta(origen, destino)
            if ruta:
                rutas.append(ruta)
                costo = self.calcular_costo(ruta)
                self.pheromones.depositar(ruta, 1 / costo)
        self.pheromones.evaporar()
        return rutas

    def construir_ruta(self, origen, destino):
        ruta = [origen]
        visitado = set(ruta)
        actual = origen
        while actual != destino:
            vecinos = list(self.graph.neighbors(actual))
            vecinos = [v for v in vecinos if v not in visitado]
            if not vecinos:
                return None  # sin salida
            probabilidades = []
            for vecino in vecinos:
                edge = (actual, vecino)
                tau = self.pheromones.pheromones.get(edge, 0.1)
                eta = 1 / self.graph[actual][vecino][0]['length']
                probabilidades.append((tau ** self.alpha) * (eta ** self.beta))
            suma = sum(probabilidades)
            probabilidades = [p / suma for p in probabilidades]
            actual = random.choices(vecinos, weights=probabilidades)[0]
            ruta.append(actual)
            visitado.add(actual)
        return ruta

    def calcular_costo(self, ruta):
        return sum(self.graph[ruta[i]][ruta[i+1]][0]['length'] for i in range(len(ruta) - 1))
