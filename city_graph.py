import osmnx as ox
import networkx as nx

def cargar_mapa_queretaro():
    lugar = "Querétaro, Mexico"
    G = ox.graph_from_place(lugar, network_type='drive')
    G = ox.add_edge_lengths(G)
    return G
