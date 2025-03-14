# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 11:55:56 2023

@author: Anibal y Martina
"""

from random import randint
import math

def crear_archivo_de_datos(nombre):
    f = 1000
    N = 5*f
    cifras = 20
    tam_bloque = f # 1 M de valores por bloque a escribir
    
    # print('Cantidad de valores a escribir:', N)
    
    # truncar archivo si existe
    with open(nombre, 'w') as archivo:
        pass
    
    # escribir datos
    N_restantes = N
    while N_restantes > 0:
        cif = cifras
        r = N_restantes % tam_bloque
        c = N_restantes // tam_bloque
        if c > 0:
            t = tam_bloque
        elif c == 0:
            t = r
        N_restantes -= t
        # print('t =', t, ', N_restantes =', N_restantes)
        bloque = [str(randint(10**(cif-1), 10**cif-1))+'\n'
                  for i in range(t)]        
        with open(nombre, 'a+') as archivo:
            archivo.writelines(bloque)


def ordenar_sublistas(archivo, B):
    cont=-1
    sublista=[]
    archiorig = open(archivo, "r")
    archiordenado = open ("datosord.txt", "w" )
    
    for linea in archiorig:
        if cont< B-1:
            sublista.append(linea)
            cont+=1
        
        else:
            ordenar_por_insercion(sublista)
            archiordenado.writelines(sublista)
            cont=0
            
            sublista=[]
            sublista.append(linea)
    ordenar_por_insercion(sublista)
    archiordenado.writelines(sublista)
    archiorig.close()
    archiordenado.close()


        
def ordenar_por_insercion(lista):
    for indice in range(1,len(lista)):
        valorActual = lista[indice]
        posicion = indice

        while posicion>0 and lista[posicion-1]>valorActual:
            lista[posicion]=lista[posicion-1]
            posicion = posicion-1

        lista[posicion]=valorActual


def dividir(archivo, tamdelistas, B):
    aux1 = open ('archivoaux1.txt', 'w')
    aux2 = open ('archivoaux2.txt', 'w')
    archi = open(archivo, 'r' )
    listaB= []
    variable = True
    contador = 0
    tamanio1, tamanio2 = 0, 0 
    for linea in archi:
        if variable:
            listaB.append(linea)
            tamanio1 +=1
        else:
            listaB.append(linea)
            tamanio2 +=1
        
        contador += 1 
        
        if len(listaB)%B == 0:
            if variable:
                aux1.writelines(listaB)
            else:
                aux2.writelines(listaB)
            listaB=[]
            
        
        if contador == tamdelistas:
            contador=0
            variable = not variable
            
    if len(listaB)>0:
        if variable:
            aux1.writelines(listaB)
        else:
            aux2.writelines(listaB)
        listaB=[]
                        
    aux1.close()
    aux2.close()
    archi.close() 
    return (tamanio1, tamanio2)
       
                      
   
    
def fusionar (archivo, tamdelistas, t1, B):
    aux1 = open ('archivoaux1.txt', 'r')
    aux2 = open ('archivoaux2.txt', 'r')
    archivo = open( archivo, 'w' )
    listaB= []
    num1 = aux1.readline()
    num2 = aux2.readline()
    ciclos= math.ceil((t1)/tamdelistas)    #que redondee para arriba
    for i in range (ciclos):
        movpuntero1, movpuntero2 = 0,0
        while movpuntero1 < tamdelistas and movpuntero2 < tamdelistas :
             if num1>num2:
                 listaB.append(num2)
                 movpuntero2 += 1 
                 num2 = aux2.readline()
                 if len(listaB)%B == 0:
                     archivo.writelines(listaB) 
                     listaB = []
                 
             else: #toma el caso de ser iguales y el de num2 mayor
                 listaB.append(num1)
                 movpuntero1 += 1 
                 num1 = aux1.readline()
                 if len(listaB)%B == 0:
                     archivo.writelines(listaB)
                     listaB = []
                     
        while movpuntero1<tamdelistas:
            listaB.append(num1)
            movpuntero1+=1 
            num1 = aux1.readline()
            if len(listaB)%B == 0:
                archivo.writelines(listaB)
                listaB = []
                
        while movpuntero2<tamdelistas:
            listaB.append(num2)
            movpuntero2+=1 
            num2 = aux2.readline()
            if len(listaB)%B == 0:
                archivo.writelines(listaB) 
                listaB = []
        
        if len(listaB)>0:
            archivo.writelines(listaB)
            listaB=[]
                    
        
    aux1.close()
    aux2.close()
    archivo.close()        
                     
def mezcla_directa (archivo, B):
    tamdelistas = B
    t1, t2 = dividir(archivo, tamdelistas, B)
    fusionar(archivo, tamdelistas, t1, B)
    tamdelistas = tamdelistas*2
    while tamdelistas < t1+t2:
        t1, t2 = dividir(archivo, tamdelistas, B)
        fusionar(archivo, tamdelistas, t1, B)
        tamdelistas = tamdelistas*2
  





