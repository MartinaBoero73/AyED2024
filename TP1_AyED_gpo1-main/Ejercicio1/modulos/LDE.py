# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 11:04:53 2023

@author: Anibal y Martina
"""
from modulos.Nodo import Nodo

class ListaVaciaError(Exception):
    '''Error que ocurre al querer extraer un elemento de una lista vacia'''


class ListaDobleEnlazada:
    
    def __init__(self):
        self.cabeza=None
        self.cola= None
        self.tamanio=0

    def __iter__(self):
        """iterador"""
        nodo=self.cabeza 
        while nodo:
            yield nodo.dato
            nodo = nodo.siguiente
    
    def __str__(self):
      lista=[nodo  for nodo in self]
      return str(lista)
    
    def __len__ (self):
        return self.tamanio
    
    def tamanio(self):
        """
        Devuelve la cantidad de items en la lista
        """
        return self.tamanio
     
    def esta_vacia(self):
        """
        Devuelve True si la lista está vacía
        """
        return self.tamanio==0
        
   
        
    def agregar_al_inicio(self,item):
        """
        Agrega un nuevo ítem al inicio de la lista.
        ----------
        Parametros: item
        ----------
        item : el elemento a agregar.
        """

        n1=Nodo(item)
        
        if self.esta_vacia():
            self.cabeza = n1
            self.cola=n1
            
        else:
            n1.siguiente= self.cabeza
            self.cabeza.anterior=n1
            self.cabeza=n1
            
        self.tamanio+=1
        
    def agregar_al_final(self,item):
        """
        agrega un elemento al final de la lista.
        
        Parametro: item
        ----------
        item : el elemento a agregar_al_final
        """
        n1=Nodo(item)
       
        if self.esta_vacia():
            self.cabeza = n1
            self.cola=n1
            
        else:
            n1.anterior=self.cola
            self.cola.siguiente=n1
            self.cola=n1
        
        self.tamanio+=1
        
   
        
    def insertar(self,item,posicion):
        """
        Inserta un elemento en una posicion de la lista
           ----------
        Parametros:
        
        posicion : indice en el que se desea insertar el dato
        item : elemento que se desea insertar
        ------
        Raises

        IndexError
            posicion ingresada esta fuera del tamño de la lista.

        """
        nuevo=Nodo(item)

        if (posicion<0 or posicion>self.tamanio):
            raise IndexError("posicion fuera de tamaño de la lista")
            
        if posicion == 0:
            self.agregar_al_inicio(item)

        elif (self.tamanio == posicion):  
            self.agregar_al_final(item)           

        elif (posicion > 0 and posicion < self.tamanio):
            "Guardo la cabeza, avanzo hasta el anterior a la posición. Redefino los enlazes"
            temp = self.cabeza
            for i in range(posicion-1):
                temp = temp.siguiente
            nuevo.siguiente = temp.siguiente
            temp.siguiente.anterior = nuevo
            temp.siguiente = nuevo
            nuevo.anterior = temp 
            
            self.tamanio += 1

   
    
    def extraer(self, posicion=(-1)):
        """
        extrae el dato alojado en la posicion indicada.

        Parameters
        ----------
        posicion : indice en el que se desea realizar la extraccion.
        El valor por defecto es -1, que permite, al no pasar el parámetro, extraer al final de la lista

        Raises
        ------
        ListaVaciaError
            La lista esta vacia.
        IndexError
            el indice ingresado se encuentra fuera del rango.

        Returns
        -------
        almacenado : devuelve el dato extraido

        """
        
        if(self.esta_vacia()):
            raise ListaVaciaError("no puede extraer nada de una lista vacia.")
        
        elif (posicion<-1 or posicion>=self.tamanio):
            raise IndexError("posicion fuera de tamaño de la lista")
        
        elif (self.tamanio==1):
            "por si quiero extraer uno, que no es lo mismo que quede en posicion cero"
            almacenado=self.cabeza
            self.cabeza=None
            self.cola=None
            
        elif posicion==0:
            almacenado=self.cabeza
            almacenado.siguiente.anterior=None
            self.cabeza=almacenado.siguiente
            almacenado.siguiente= None 

        
        elif posicion==self.tamanio-1 or posicion==-1:
            almacenado = self.cola
            almacenado.anterior.siguiente=None
            self.cola=almacenado.anterior
            almacenado.anterior=None

        else:
            temp=self.cabeza
            for i in range(posicion-1):
                temp=temp.siguiente
            almacenado=temp.siguiente 
            temp.siguiente= almacenado.siguiente 
            almacenado.siguiente.anterior=temp
                
        self.tamanio-=1
        
        return  almacenado.dato
    
    def copiar(self):
        """
        Realiza una copia de la lista y devuelve la copia.

        Returns
        -------
        almacenado : una copia de la lista inicial

        """
        almacenado = ListaDobleEnlazada()
        
        for dato in self:
            almacenado.agregar_al_final(dato)
        
        return almacenado
    
    
    def concatenar(self, Lista):
        """
        Modifica la lista actual para concatenarle la lista indicada a su final

        Parametros
        ----------
        Lista :  una lista doblemente enlazada que será concatenada al final de self 

        Returns
        -------
        self: la lista concatenada con la segunda

        """
        
        lista2= Lista.copiar()
        
        lista2.cabeza.anterior=self.cola
        self.cola.siguiente=lista2.cabeza 
        self.cola=lista2.cola
        
        self.tamanio+=lista2.tamanio
        return self 
       
       
    def __add__(self,Lista):
        """
        Se concatenan las dos listas conectadas por el operador "+" pero sin modificar las listas iniciales

        Parameters
        ----------
        Listas a concatenar

        Returns
        -------
        Nueva lista que contiene ambas listas concatenadas

        """
        lista3 = self.copiar()
        return lista3.concatenar(Lista)
  
    
    def invertir(self):
        """
        Se invierten el orden de la lista
       
        Returns
        -------
        None.

        """
        cabeza =self.cabeza 
        cola =self.cola  
       
        temp = self.cabeza
        while temp:
            aux = temp.siguiente
            temp.siguiente = temp.anterior
            temp.anterior = aux
            temp=temp.anterior
        self.cola=cabeza
        self.cabeza=cola
        
    def ordenar(self):
        """
        Ordena los elementos de la lista de "menor a mayor". 
        La lista se ordena sobre sí misma con un algoritmo de insercion

        Returns
        -------
        None.

        """
        temp=self.cabeza.siguiente
        while temp:
            while (temp.anterior and temp.dato < temp.anterior.dato):
                temp.dato, temp.anterior.dato = temp.anterior.dato, temp.dato
                temp=temp.anterior    
            temp=temp.siguiente
            
            
            
            
            
            
        