# -*- coding: utf-8 -*-
"""
@author: Anibal y Martina
"""

from aplicaciones.rutas import *


if __name__ == '__main__':
        
    print("Bienvenido!")
    print(" ")
    

    archivo = input("Ingrese el nombre del archivo de rutas: ")
    
    print("Elija una de las siguientes opciones: ")
    print("1 si desea saber la ruta con mayor cuello de botella")
    print("2 si desea saber la ruta con precio minimo")
    opcion = input(": ")
    opcion = int(opcion)
    
   
    while opcion != 1 and opcion != 2 :
        opcion = input("Elija una opcion valida ")

    peso_min = 0 
    
    if opcion == 1 :
        peso_min = input ("Ingrese, si desea, el peso minimo a transportar: ")
    
    peso_min = int(peso_min)
    
    origen = input("Ingrese la ciudad de origen: ")
    destino = input("Ingrese la ciudad de destino: ")
    
    obtenerMejorRuta(archivo, opcion, origen, destino, peso_min)
    
    # obtenerMejorRuta("rutas.txt", 2, "CiudadBs.As.", "S.delEstero", peso_min=0)