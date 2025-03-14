# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 11:09:01 2023

@author: Anibal y Martina
"""

from modulos.LDE import ListaDobleEnlazada
import random
import time
import matplotlib.pyplot as plt

if __name__ == "__main__":
     
    tiempos= []
    var = [10, 100, 500, 750 ,1000] 
    
    lista1= ListaDobleEnlazada()
    lista2= ListaDobleEnlazada()
    lista3= ListaDobleEnlazada()
    lista4= ListaDobleEnlazada()
    lista5= ListaDobleEnlazada()
    
    for i in range (10):
        numero=random.randint(0, 1000)
        lista1.agregar_al_final(numero)
    
    for i in range (100):
        numero=random.randint(0, 1000)
        lista2.agregar_al_final(numero)
    
    for i in range (500):
        numero=random.randint(0, 1000)
        lista3.agregar_al_final(numero)
    
    for i in range (750):
        numero=random.randint(0, 1000)
        lista4.agregar_al_final(numero)
    
    for i in range (1000):
        numero=random.randint(0, 1000)
        lista5.agregar_al_final(numero)
    
    tic1 = time.perf_counter()
    lista1.ordenar()
    toc1 = time.perf_counter()
    delta_t1 = toc1 - tic1
    tiempos.append(delta_t1)
    
    tic2 = time.perf_counter()
    lista2.ordenar()
    toc2 = time.perf_counter()
    delta_t2 = toc2 - tic2
    tiempos.append(delta_t2)
    
    tic3 = time.perf_counter()
    lista3.ordenar()
    toc3 = time.perf_counter()
    delta_t3 = toc3 - tic3
    tiempos.append(delta_t3)
    
    tic4 = time.perf_counter()
    lista4.ordenar()
    toc4 = time.perf_counter()
    delta_t4 = toc4 - tic4
    tiempos.append(delta_t4)
    
    tic5 = time.perf_counter()
    lista5.ordenar()
    toc5 = time.perf_counter()
    delta_t5 = toc5 - tic5
    tiempos.append(delta_t5)
    
    plt.plot(var, tiempos)
    plt.title('Tiempo de ordenamiento según cantidad de elementos en la lista')
    plt.xlabel('cantidad de elementos en la lista')
    plt.ylabel('tiempos ($s$)')
    
    print(tiempos)
    
    
    
    
    
    
