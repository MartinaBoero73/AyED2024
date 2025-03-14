# -*- coding: utf-8 -*-
"""
@author: Anibal y Martina
"""

from modulos.Grafo import Grafo, Vertice
from modulos.Dijkstra import dijkstra, dijkstra_modificado


def crearGrafoPeso(nombre_archi, peso_min = 0):
    """
    Crea un grafo segun los pesos a partir de un archivo con informacion de vertices y aristas    
    Para su correcta ejecucion necesita que el archivo este dispuesto en lineas con
    "id del vertice o ciudad", "id del vertice vecino", peso, costo
    Donde solo nos interesa el peso de la arista o ruta que los une
    
    Parameters
    ----------
    nombre_archi : nombre del archivo que contiene esta informacion
    peso_min : int, es el peso minimo que se desea trasladar.
        en el grafo final se excluyen las rutas con peso menor al indicado
        The default is 0.

    Returns
    -------
    grafo_peso : objeto grafo con aristas basadas en peso

    """
    grafo_peso = Grafo()
    with open(nombre_archi, 'r') as archivo:
       for linea in archivo:
           partida, destino, peso, costo = linea.strip().split(',')
           if int(peso) >= peso_min:    
               grafo_peso.agregarArista(partida, destino, peso)    

    return grafo_peso


def crearGrafoCosto(nombre_archi):
    """
    Crea un grafo segun los costos a partir de un archivo con informacion de vertices y aristas    
    Para su correcta ejecucion necesita que el archivo este dispuesto en lineas con
    "id del vertice o ciudad", "id del vertice vecino", peso, costo
    Donde solo nos interesa el costo de la arista o ruta que los une
    
    Parameters
    ----------
    nombre_archi : nombre del archivo que contiene esta informacion


    Returns
    -------
    grafo_costo : objeto grafo con aristas basadas en costo

    """
    grafo_costo = Grafo()
    with open(nombre_archi, 'r') as archivo:
       for linea in archivo:
           partida, destino, peso, costo = linea.strip().split(',')   
           grafo_costo.agregarArista(partida, destino, costo)    

    return grafo_costo


def obtenerCuelloBotellaMax(grafo, partida, destino):
    """
    Devuelve el cuello de botella maximo y la ruta a tomar en un grafo basado en pesos
    Da uso al algoritmo de Dijkstra modificado
    
    Parameters
    ----------
    grafo : objeto grafo basado en pesos
    partida : id del vertice de inicio
    destino : id del vertice de destino

    Returns
    -------
    peso_max : int, es el peso maximo o mayor cuello de botella trasladable entre las ciudades de destino y origen
    recorrido : str, representacion del recorrido a realizar con el peso indicado

    """
    vertice_partida = grafo.obtenerVertice(partida)
    vertice_destino = grafo.obtenerVertice(destino)
    
    dijkstra_modificado(grafo, vertice_partida)
    recorrido = grafo.obtenerCamino(partida, destino)
    peso_max = vertice_destino.obtenerDistancia()
    
    return  peso_max, recorrido
    
    
    
def obtenerCostoMin(grafo, partida, destino):
    """
    Devuelve el costo minimo y la ruta a tomar en un grafo basado en costos
    Da uso al algoritmo de Dijkstra
    
    Parameters
    ----------
    grafo : objeto grafo basado en costos
    partida : id del vertice de inicio
    destino : id del vertice de destino

    Returns
    -------
    costo_min : int, es el costo minimo de trasladar por esa ruta
    recorrido : str, representacion del recorrido a realizar con el costo indicado

    """
    vertice_partida = grafo.obtenerVertice(partida)
    vertice_destino = grafo.obtenerVertice(destino)
   
    dijkstra(grafo, vertice_partida)
    recorrido = grafo.obtenerCamino(partida, destino)
    costo_min = vertice_destino.obtenerDistancia()
    
    return  costo_min, recorrido
    

def obtenerMejorRuta(nombre_archi, opcion, origen, destino, peso_min=0):
    """
    permite obtener la ruta optima entre dos ciudades, sea por costos o peso
    segun la opcion que se elija.
    Si el peso es 0 o el costo es muy grande, denota que las rutas no existen o, en 
    caso del peso, puede indicar que no hay ruta posible con el peso minimo que se 
    desea trasladar

    Parameters
    ----------
    nombre_archi : str
        nombre del archivo donde se aloja la informacion de las rutas
    opcion : int
        idicador del algoritmo a aplicar
        1 indica ejecutar el algoritmo de Dijkstra modificado para obtener el mayor cuello de botella
        2 indica ejecutar algoritmo de Dijkstra para obtener el menor costo
    
    origen : id del vertice o ciudad de origen
    destino : id del vertice o ciudad de destino
    
    peso_min : int
        Es el peso minimo que se desea trasladar entre las dos ciudades
        Es opcional y por defecto es 0.

    Returns
    -------
    None.

    """
    
    if opcion == 1 :
        grafoPeso = crearGrafoPeso(nombre_archi, peso_min)
        peso_max, recorrido = obtenerCuelloBotellaMax(grafoPeso,origen, destino)
        if peso_max == 0:
            print ("No existe ruta")
        else:
            print ("La ruta con mejor cuello de botella es: ", recorrido, " y permite trasladar un peso maximo de: ", peso_max )
        
    
    elif opcion == 2:
        grafoCosto = crearGrafoCosto(nombre_archi)
        costo_min, recorrido = obtenerCostoMin(grafoCosto, origen, destino)
        
        if costo_min > 100:
            print ("No existe ruta")
        else:
            print ("La ruta con menor costo es : ", recorrido, " y tiene un costo de:  ", costo_min*1000 )
        
        

    