# -*- coding: utf-8 -*-
"""
Created on Mon May 15 11:52:32 2023

@author: Anibal y Martina
"""
class NodoArbol:
    
    def __init__(self,clave,valor,izquierdo=None,derecho=None, padre=None):
        """
        Constructor de la clase nodo

        Parameters:
        clave : clave del nodo
        valor : carga util del nodo
        izquierdo : referencia al hijo izquierdo del nodo. Default: None
        derecho : referencia al hijo derecho del nodo. Default: None
        padre : referencia al padre del nodo. Default: none
        ----------
        Returns
        None.

        """
        self.clave = clave
        self.cargaUtil = valor
        self.hijoIzquierdo = izquierdo
        self.hijoDerecho = derecho
        self.padre = padre
        self.factorEquilibrio = 0
        
    def __iter__(self):
        """
        Iterador en inorden
    
        """
        if self:
          if self.tieneHijoIzquierdo():
              for elem in self.hijoIzquierdo:
                  yield elem
          yield self
          if self.tieneHijoDerecho():
              for elem in self.hijoDerecho:
                  yield elem

    def iter_preorden(self):
        """
        iterador en preorden
        """
        if self:
          yield self
          if self.tieneHijoIzquierdo():
              for elem in self.hijoIzquierdo.iter_preorden():
                  yield elem
          if self.tieneHijoDerecho():
              for elem in self.hijoDerecho.iter_preorden():
                  yield elem

    def tieneHijoIzquierdo(self):
        """
        Chequea que el nodo tenga hijo izquierdo

        Returns
        True si tiene hijo izquierdo

        """
        return self.hijoIzquierdo

    def tieneHijoDerecho(self):
        """
        Chequea que el nodo tenga hijo derecho

        Returns
        True si tiene hijo derecho

        """
        return self.hijoDerecho

    def esHijoIzquierdo(self):
        """
        Verifica si el nodo actual es el hijo izquierdo de su padre

        Returns
        True si es hijo izquierdo de su padre

        """
        return self.padre and self.padre.hijoIzquierdo == self

    def esHijoDerecho(self):
        """
        Verifica si el nodo actual es el hijo izquierdo de su padre

        Returns
        True si es hijo izquierdo de su padre

        """
        return self.padre and self.padre.hijoDerecho == self

    def esRaiz(self):
        """
        Verifica si el nodo actual es la raiz del arbol

        Returns
        True si es la raiz, es decir, si no tiene padre

        """
        return not self.padre

    def esHoja(self):
        """
        Verifica si el nodo actual es hoja, es decir, no tiene descendientes

        Returns
        True si es hoja
        """
        return not (self.hijoDerecho or self.hijoIzquierdo)

    def tieneAlgunHijo(self):
        """
        Verifica si el nodo actual tiene como mínimo un hijo
        
        Returns
        True si tiene uno o ambos hijos

        """
        return self.hijoDerecho or self.hijoIzquierdo

    def tieneAmbosHijos(self):
        """
        Verifica si el nodo tiene dos hijos

        Returns
        True si el nodo actual tiene ambos hijos, derecho e izquierdo

        """
        return self.hijoDerecho and self.hijoIzquierdo

    def reemplazarDatoDeNodo(self,clave,valor,hizq,hder):
        """
        Cambia los datos del nodo actual por valores nuevos

        Parameters
        clave : la nueva clave a asignar al nodo actual
        valor : la nueva caraga util a asociar al nodo
        hizq : una nueva referecnai al hijo izquierdo
        hder : una nueva referencia al hijo derecho
        -------
        Returns
        None.

        """
        self.clave = clave
        self.cargaUtil = valor
        self.hijoIzquierdo = hizq
        self.hijoDerecho = hder
        if self.tieneHijoIzquierdo():
            self.hijoIzquierdo.padre = self
        if self.tieneHijoDerecho():
            self.hijoDerecho.padre = self

    def __str__(self):
        """
        método para mostrar por consola un nodo 

        Returns
        string: nodo representado como (clave, valor)

        """
        return '(' + str(self.clave) + ',' + str(self.cargaUtil) + ')' 
    
    def __repr__(self):
        """
        metodo para mostrar por consola nodos en una lista
        """
        return self.__str__() 