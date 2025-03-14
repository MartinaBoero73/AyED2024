# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 11:05:03 2023

@author: Anibal y Martina
"""

class Nodo:
    def __init__(self,datoInicial):
        self.dato = datoInicial
        self.siguiente = None
        self.anterior = None
        
    def __str__(self):
        return str(self.dato)

    def __repr__(self):
        """adentro de una lista"""
        return str(self.dato)    

    @property 
    def dato(self):
        return self._dato
    @dato.setter 
    def dato(self,valor):
        self._dato=valor
        
        
    @property
    def siguiente(self):
        return self._siguiente
    
    @siguiente.setter
    def siguiente(self,nsiguiente):
        self._siguiente=nsiguiente
    
    @property
    def anterior(self):
        return self._anterior
    
    @anterior.setter
    def anterior(self,nanterior):
        self._anterior=nanterior