# -*- coding: utf-8 -*-
"""
@author: Anibal y Martina

"""
import sys
from modulos.Grafo import Grafo, Vertice
from modulos.ColaPrioridadMax import ColaPrioridadMax
from modulos.ColaPrioridadMin import ColaPrioridadMin


def dijkstra(unGrafo,inicio):
    """
    Algoritmo de Dijkstra para encontrar el camino con menor ponderacion en un grafo a partir de un vertice
    Esta es la funcion que luego se utiliza para encontrar la ruta con menor costo
    Da uso a la cola de prioridad de minimos
    
    Parameters
    ----------
    unGrafo : grafo en el que se busca
    inicio : vertice de comienzo

    Returns
    -------
    None.

    """
    cp = ColaPrioridadMin()
    for vert in unGrafo:
        vert.asignarDistancia(sys.maxsize)    
    inicio.asignarDistancia(0)
    
    cp.construirMonticulo([(v.obtenerDistancia(),v) for v in unGrafo])
    
    while not cp.estaVacia():
        verticeActual = cp.eliminarMin()[1]
        for verticeSiguiente in verticeActual.obtenerConexiones():
            nuevaDistancia = verticeActual.obtenerDistancia() \
                    + int(verticeActual.obtenerPonderacion(verticeSiguiente))
            if nuevaDistancia < verticeSiguiente.obtenerDistancia():
                verticeSiguiente.asignarDistancia( nuevaDistancia )
                verticeSiguiente.asignarPredecesor(verticeActual)
                cp.decrementarClave(verticeSiguiente,nuevaDistancia)
                
                
def dijkstra_modificado(unGrafo,inicio):
    """
    Algoritmo de Dijkstra para encontrar el camino con mayor ponderacion en un grafo a partir de un vertice inicial
    Esta es la funcion que luego se utiliza para encontrar la ruta con mayor cuello de botella de peso trasladable
    Da uso a la cola de prioridad de maximos
    
    Parameters
    ----------
    unGrafo : grafo en el que se busca
    inicio : vertice de comienzo
    
    Returns
    -------
    None.

    """
    cp = ColaPrioridadMax()
    inicio.asignarDistancia(sys.maxsize)
    cp.construirMonticulo([(v.obtenerDistancia(),v) for v in unGrafo])
    
    while not cp.estaVacia():
        verticeActual = cp.eliminarMax()
        for verticeSiguiente in verticeActual.obtenerConexiones():
            nuevaDistancia = min(verticeActual.obtenerDistancia(),int(verticeActual.obtenerPonderacion(verticeSiguiente)))
            if nuevaDistancia > verticeSiguiente.obtenerDistancia():
                verticeSiguiente.asignarDistancia( nuevaDistancia )
                verticeSiguiente.asignarPredecesor(verticeActual)
                cp.incrementarClave(verticeSiguiente,nuevaDistancia)
                
    