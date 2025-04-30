from city_graph import cargar_mapa_queretaro
from pheromone_map import PheromoneMap
from ant_colony import AntColony
from visualize import mostrar_ruta
import random

G = cargar_mapa_queretaro()
origen = random.choice(list(G.nodes))
destino = random.choice(list(G.nodes))

feromonas = PheromoneMap(G)
colonia = AntColony(G, feromonas)

for i in range(10):
    rutas = colonia.correr_iteracion(origen, destino)
    print(f"Iteración {i+1}: {len(rutas)} rutas generadas")

mejor_ruta = min(rutas, key=lambda r: colonia.calcular_costo(r))
mostrar_ruta(G, mejor_ruta)
print("Ruta visualizada en ruta_simulada.html")
