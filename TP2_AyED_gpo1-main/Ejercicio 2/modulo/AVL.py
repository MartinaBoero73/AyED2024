# -*- coding: utf-8 -*-
"""
Created on Mon May 15 11:49:26 2023

@author: Anibal y Martina
"""
from  modulo.nodo import NodoArbol

class AVL:

    def __init__(self):
        """
        Constructor de la clase AVL
        """
        self.raiz = None
        self.tamano = 0

    def longitud(self):
        """
        obtiene el tamaño del arbol

        Returns
        int: cantidad de nodos en el arbol
        """
        return self.tamano

    def __len__(self):
        """
        obtiene el tamaño del arbol

        Returns
        int: cantidad de nodos en el arbol
        """
        return self.tamano

    def __iter__(self):
        """
        permite iterar sobre los nodos en inorden

        """
        return self.raiz.__iter__()
    
    def __iter_preorden__(self):
        """
        permite iterar sobre los nodos en preorden
        """
        return self.raiz.iter_preorden()
    
    def obtener(self,clave):
        """
        devuelve el valor almacenado en el nodo con clave indicada
        
        Parameters
        clave : clave del nodo cuya carga util se desea obtener
        -------
        Returns
        valor almacenado en nodo

        """
        if self.raiz:
            resultado = self._obtener(clave,self.raiz)
            if resultado:
                return resultado.cargaUtil
            else:
                return None
        else:
            return None

    def _obtener(self,clave,nodoActual):
        """
        busca y devuelve el nodo con clave indicada
        es un metodo privado 
        
        Parameters
        clave : clave del nodo que se esta buscando
        -------
        Returns
        nodo buscado
        
        """
        if not nodoActual:
            return None
        elif nodoActual.clave == clave:
            return nodoActual
        elif clave < nodoActual.clave:
            return self._obtener(clave,nodoActual.hijoIzquierdo)
        else:
            return self._obtener(clave,nodoActual.hijoDerecho)

    # def _obtener_nodo_con_clave_igual_o_mayor(self,clave,nodoActual, nodoAnterior=None):
    #     """
    #             Devuelve el primer nodo delraango, en caso de que se ingrese una fecha que no esta en el arbol se busca la fecha más cercana 
    #             pero que esté anterior a la fehca indicada para que se muestren las fechas que si estan en el rango.

    #     """        
        
        
        
    #     if not nodoActual:
    #         return None
    #     elif nodoActual.clave == clave:
    #         return nodoActual
    #     elif nodoActual != self.raiz:
    #         if nodoAnterior.clave > clave \
    #            and (nodoActual.clave < clave or nodoActual is None):
    #               return nodoAnterior
              
    #     if clave < nodoActual.clave:
    #         return self._obtener_nodo_con_clave_igual_o_mayor(clave,nodoActual.hijoIzquierdo,nodoActual)
    #     else:
    #         return self._obtener_nodo_con_clave_igual_o_mayor(clave,nodoActual.hijoDerecho,nodoActual)


    def agregar (self, clave, valor):
        """
        agrega un nodo al arbol

        Parameters
        clave : clave del nuevo nodo
        valor : carga util del nuevo nodo
        ----------

        Returns
        None.

        """
        self.raiz = self._agregar(self.raiz, clave, valor)
        nodoAgregado = self._obtener(clave, self.raiz)
        self.actualizarEquilibrio(nodoAgregado) 
        
    def _agregar (self, raiz_subarbol, clave, valor, padre= None):
        """
        metodo llamado por agregar para buscar la posicion en la que agregar
        Es un metodo privado

        Parameters
        raiz_subarbol : raiz del subarbol en el que se busca agregar el dato
        clave : clave del nuevo nodo
        valor : carga util del nuevo nodo
        padre : nodo padre del actual. The default is None.
        -------
        Returns
        raiz_subarbol : nueva raiz del subarbol donde se seguira buscando

        """
        if not raiz_subarbol:
            raiz_subarbol = NodoArbol(clave, valor, padre = padre)
            self.tamano = self.tamano +1
        else:
            if clave < raiz_subarbol.clave:
                raiz_subarbol.hijoIzquierdo = self._agregar (raiz_subarbol.hijoIzquierdo, clave, valor, raiz_subarbol)
            else: 
                raiz_subarbol.hijoDerecho = self._agregar (raiz_subarbol.hijoDerecho, clave, valor, raiz_subarbol)
        
        return raiz_subarbol

    
    def actualizarEquilibrio(self,nodo):
        """
        Actualiza los factores de equilibrio de los nodos

        Parameters
        nodo : nodo desde el que se comienza a equilibraar
        -------
        Returns
        None.

        """
        if nodo.factorEquilibrio > 1 or nodo.factorEquilibrio < -1:
            self.reequilibrar(nodo)
            return
        if nodo.padre != None:
            if nodo.esHijoIzquierdo():
                    nodo.padre.factorEquilibrio += 1
            elif nodo.esHijoDerecho():
                    nodo.padre.factorEquilibrio -= 1
    
            if nodo.padre.factorEquilibrio != 0:
                    self.actualizarEquilibrio(nodo.padre)

    def rotarIzquierda(self,rotRaiz):
        """
        Ejecuta una rotacion izquierda a partir del nodo dado

        Parameters
        rotRaiz nodo a partir del cual se rota a la izquierda
        ---------
        Returns
        None.

        """
        nuevaRaiz = rotRaiz.hijoDerecho
        rotRaiz.hijoDerecho = nuevaRaiz.hijoIzquierdo
        if nuevaRaiz.hijoIzquierdo != None:
            nuevaRaiz.hijoIzquierdo.padre = rotRaiz
        nuevaRaiz.padre = rotRaiz.padre
        if rotRaiz.esRaiz():
            self.raiz = nuevaRaiz
        else:
            if rotRaiz.esHijoIzquierdo():
                    rotRaiz.padre.hijoIzquierdo = nuevaRaiz
            else:
                rotRaiz.padre.hijoDerecho = nuevaRaiz
        nuevaRaiz.hijoIzquierdo = rotRaiz
        rotRaiz.padre = nuevaRaiz
        rotRaiz.factorEquilibrio = rotRaiz.factorEquilibrio + 1 - min(nuevaRaiz.factorEquilibrio, 0)
        nuevaRaiz.factorEquilibrio = nuevaRaiz.factorEquilibrio + 1 + max(rotRaiz.factorEquilibrio, 0)
        
    def rotarDerecha (self, rotRaiz):
        """
        Ejecuta una rotacion derecha a partir del nodo dado

        Parameters
        rotRaiz nodo a partir del cual se rota a la derecha
        ---------
        Returns
        None.

        """
        
        # print('rotRaiz:', rotRaiz)
        # print('factoreq:', rotRaiz.factorEquilibrio)
        nuevaRaiz = rotRaiz.hijoIzquierdo
        # print('nuevaRaiz:',nuevaRaiz)
        # print('eq:',nuevaRaiz.factorEquilibrio)
        # print(nuevaRaiz.hijoDerecho)
        
        rotRaiz.hijoIzquierdo = nuevaRaiz.hijoDerecho
        
        if nuevaRaiz.hijoDerecho != None:
            nuevaRaiz.hijoDerecho.padre = rotRaiz
        nuevaRaiz.padre = rotRaiz.padre
        if rotRaiz.esRaiz():
            self.raiz = nuevaRaiz
        else:
            if rotRaiz.esHijoDerecho():
                    rotRaiz.padre.hijoDerecho = nuevaRaiz
            else:
                rotRaiz.padre.hijoIzquierdo = nuevaRaiz
        nuevaRaiz.hijoDerecho = rotRaiz
        rotRaiz.padre = nuevaRaiz
        rotRaiz.factorEquilibrio = rotRaiz.factorEquilibrio - 1 + max(-nuevaRaiz.factorEquilibrio, 0)
        nuevaRaiz.factorEquilibrio = nuevaRaiz.factorEquilibrio - 1 + max(rotRaiz.factorEquilibrio, 0)
    
    def reequilibrar(self,nodo):
        """
        realiza las rotaciones necesarias para reequilibrar el arbol

        Parameters
        nodo : nodo a partir del cual se ejecuta el reequilibrio
        -------

        Returns
        None.

        """
        if nodo.factorEquilibrio < 0:
                if nodo.hijoDerecho.factorEquilibrio > 0:
                  self.rotarDerecha(nodo.hijoDerecho)
                  self.rotarIzquierda(nodo)
                else:
                  self.rotarIzquierda(nodo)
        elif nodo.factorEquilibrio > 0:
                if nodo.hijoIzquierdo.factorEquilibrio < 0:
                  self.rotarIzquierda(nodo.hijoIzquierdo)
                  self.rotarDerecha(nodo)
                else:
                  self.rotarDerecha(nodo)
                    

    def obtener_sucesor(self, nodo):
        """
        obtiene el numero con menor clave siguiente al nodo

        Parameters
        nodo : nodo al que se le busca el sucesor
        ----------

        Returns
        -------
        sucesor : nodo encontrado como sucesor

        """
        sucesor = nodo.hijoDerecho
        while sucesor.hijoIzquierdo:
            sucesor = sucesor.hijoIzquierdo
        return sucesor
                  
                   
    def eliminar(self,clave):
        
        if self.tamano > 1:
          nodoAEliminar = self._obtener(clave,self.raiz)
          # print("elimindao: ",nodoAEliminar)
          nodoPadre = nodoAEliminar.padre
          
          if nodoAEliminar:
              self.remover(nodoAEliminar)
              self.tamano = self.tamano-1
              while nodoPadre:  
                  self.actualizarEquilibrio(nodoPadre)
                  nodoPadre = nodoPadre.padre
          else:
              raise KeyError('Error, la clave no está en el árbol')
        elif self.tamano == 1 and self.raiz.clave == clave:
          self.raiz = None
          self.tamano = self.tamano - 1
        else:
          raise KeyError('Error, la clave no está en el árbol')
        
        
        # return nodoAEliminar
    
    def remover(self,nodoActual):
        if nodoActual.esHoja(): #hoja
          if nodoActual == nodoActual.padre.hijoIzquierdo:
              nodoActual.padre.hijoIzquierdo = None
          else:
              nodoActual.padre.hijoDerecho = None
              
        elif nodoActual.tieneAmbosHijos(): #interior
            sucesor = self.obtener_sucesor(nodoActual)
            nodoActual.clave = sucesor.clave
            nodoActual.cargaUtil = sucesor.cargaUtil
            self.remover(sucesor)

        else: # este nodo tiene un (1) hijo
            if nodoActual.tieneHijoIzquierdo():
              if nodoActual.esHijoIzquierdo():
                  nodoActual.hijoIzquierdo.padre = nodoActual.padre
                  nodoActual.padre.hijoIzquierdo = nodoActual.hijoIzquierdo
              elif nodoActual.esHijoDerecho():
                  nodoActual.hijoIzquierdo.padre = nodoActual.padre
                  nodoActual.padre.hijoDerecho = nodoActual.hijoIzquierdo
              else:
                  nodoActual.reemplazarDatoDeNodo(nodoActual.hijoIzquierdo.clave,nodoActual.hijoIzquierdo.cargaUtil,nodoActual.hijoIzquierdo.hijoIzquierdo,nodoActual.hijoIzquierdo.hijoDerecho)
            else:
              if nodoActual.esHijoIzquierdo():
                  nodoActual.hijoDerecho.padre = nodoActual.padre
                  nodoActual.padre.hijoIzquierdo = nodoActual.hijoDerecho
              elif nodoActual.esHijoDerecho():
                  nodoActual.hijoDerecho.padre = nodoActual.padre
                  nodoActual.padre.hijoDerecho = nodoActual.hijoDerecho
              else:
                  nodoActual.reemplazarDatoDeNodo(nodoActual.hijoDerecho.clave,nodoActual.hijoDerecho.cargaUtil,nodoActual.hijoDerecho.hijoIzquierdo,nodoActual.hijoDerecho.hijoDerecho)
      

