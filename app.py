import streamlit as st
from city_graph import cargar_mapa_queretaro
from pheromone_map import PheromoneMap
from ant_colony import AntColony
from visualize import mostrar_ruta
import random
import os

st.set_page_config(page_title="Simulación de Tráfico en Querétaro", layout="wide")
st.title("🚦 Simulación de Tráfico con Colonia de Hormigas (Querétaro)")

G = cargar_mapa_queretaro()
nodos = list(G.nodes)

origen = st.selectbox("Selecciona nodo origen", nodos)
destino = st.selectbox("Selecciona nodo destino", nodos)

n_ants = st.slider("Número de hormigas", 1, 100, 20)
evaporacion = st.slider("Tasa de evaporación", 0.01, 1.0, 0.1)
iteraciones = st.slider("Iteraciones", 1, 50, 10)

if st.button("Simular"):
    feromonas = PheromoneMap(G)
    colonia = AntColony(G, feromonas, n_ants=n_ants)

    for i in range(iteraciones):
        rutas = colonia.correr_iteracion(origen, destino)

    if rutas:
        mejor_ruta = min(rutas, key=lambda r: colonia.calcular_costo(r))
        mostrar_ruta(G, mejor_ruta)
        st.success("Simulación completada. Ruta generada.")
        st.components.v1.html(open("ruta_simulada.html", "r", encoding="utf-8").read(), height=600)
    else:
        st.error("No se encontró ruta. Prueba con otros nodos.")
