import folium
import osmnx as ox

def mostrar_ruta(G, ruta):
    mapa = folium.Map(location=[20.5888, -100.3899], zoom_start=13)
    puntos = [(G.nodes[n]['y'], G.nodes[n]['x']) for n in ruta]
    folium.PolyLine(puntos, color="blue", weight=4).add_to(mapa)
    for lat, lon in puntos:
        folium.CircleMarker(location=(lat, lon), radius=2, color="red").add_to(mapa)
    mapa.save("ruta_simulada.html")
