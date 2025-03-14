# -*- coding: utf-8 -*-
"""
Created on Mon May 29 23:31:30 2023

@author: Martina y Anibal
"""

from modulo.Temperaturas_DB import Temperaturas_DB
from modulo.AVL import AVL


    # print(arbol.tamano)

if __name__ == "__main__":
    # BaseDeDatos = Temperaturas_DB()
    # BaseDeDatos.guardar_temperatura('20230812',17)
    # BaseDeDatos.guardar_temperatura('20230719',15)
    # BaseDeDatos.guardar_temperatura('20230316',0)
    # BaseDeDatos.guardar_temperatura('20230802',12)
    # BaseDeDatos.guardar_temperatura('20231109',30)
    # BaseDeDatos.mostrar_cantidad_muestras()
    # print(BaseDeDatos.max_temp_rango('20230316', '20231109'))
    # print(BaseDeDatos.min_temp_rango('20230512', '20230915'))
    # print(BaseDeDatos.temp_extremos_rango('20230101', '20231231'))
    # print(BaseDeDatos.mostrar_temperaturas('20230316', '20231109'))
    arbol = AVL()
    arbol.agregar('20230812', 17)
    arbol.agregar('20230719',15)
    arbol.agregar('20230316',0)
    arbol.agregar('20230802',12)
    arbol.agregar('20231109',30)
    # print("eliminado:", arbol.eliminar('20230719'))
    arbol.eliminar('20230719')
    for nodo in arbol:
        print(nodo)
    print("---------")    
    for nodo in arbol.raiz.iter_preorden():
        print(nodo)