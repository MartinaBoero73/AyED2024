# -*- coding: utf-8 -*-
"""
@author: Anibal y Martina
"""

class ColaPrioridadMin:
    def __init__(self):
        """
        Constructor de la clase ColaPrioridadMin
        Adaptado de libro para trabajar con vertices

        Returns
        -------
        None.

        """
        self.listaMonticulo = [(0,0)]
        self.tamanio = 0
    
    def estaVacia(self):
        """
        determina si la lista esta vacia

        Returns
        -------
        bool: True si la lista esta vacia, False si tiene elementos
        
        """
        return self.tamanio == 0
    
    def infiltrarArriba(self,i):   
        """"
        desplaza un elemento insertado en el final comparandolo con su padre e intercambiando hasta llevar el minimo arriba.
       
        Parametros
        i : contador (corresponde al tamanio del arbol).
        -------
        Returns
        None.

        """
        while i // 2 > 0:
          if self.listaMonticulo[i][0] < self.listaMonticulo[i // 2][0]:
             tmp = self.listaMonticulo[i // 2]
             self.listaMonticulo[i // 2] = self.listaMonticulo[i]
             self.listaMonticulo[i] = tmp
          i = i // 2
          
          
    def insertar(self,k):
        """
        agrega el dato k al final de la lista y lo infiltra hacia arriba hasta su posicion correcta

        Parametros
        k : dato a insertar
        ----------
        Returns
        None.

        """

        self.listaMonticulo.append(k)
        self.tamanio = self.tamanio + 1
        self.infiltArriba(self.tamanio)
        
    def infiltAbajo(self,i):
        """
        intercambia un nodo con su hijo menor hasta llegar a su posicion correcta

        Parametros
        i : posicion del nodo a infiltrar
        ----------
        Returns
        None.

        """
        
        while (i * 2) <= self.tamanio:
            hm = self.hijoMin(i)
            if self.listaMonticulo[i][0] > self.listaMonticulo[hm][0]:
                tmp = self.listaMonticulo[i]
                self.listaMonticulo[i] = self.listaMonticulo[hm]
                self.listaMonticulo[hm] = tmp
            i = hm
        
  
    def hijoMin(self,i):
        """
        Compara los dos nodos de un nivel con el mismo padre para devolver la posicion del menor
      
        Parametros
        i : Nodo padre
        -------
        Returns
        La posicion del nodo mas pequenio.
        """

        if i * 2 + 1 > self.tamanio:
            return i * 2
        else:
            if self.listaMonticulo[i*2][0] < self.listaMonticulo[i*2+1][0]:
                return i * 2
            else:
                return i * 2 + 1
            
            
    def eliminarMin(self):
        """
        Elimina el menor elemento, ubicado en la raiz (posicion 1). Para esto lo cambia con el último nodo, elimina el ultimo e infiltra hacia abajo la nueva raiz.
       
        Parametros:
        None
        -------
        Returns
        valorSacado: elemento ubicado en la raiz

        """

        valorSacado = self.listaMonticulo[1]
        self.listaMonticulo[1] = self.listaMonticulo[self.tamanio]
        self.tamanio = self.tamanio - 1
        self.listaMonticulo.pop()
        self.infiltAbajo(1)
        return valorSacado
    
    
    def construirMonticulo(self,unaLista):
        """
       Organiza internamente una lista de python como monticulo de minimos.
      
       Parametros:
       unaLista: una lista de python que se desea implementar como min heap
       -------
       Returns
       None

       """
        i = len(unaLista) // 2
        self.tamanio = len(unaLista)
        self.listaMonticulo = [(0,0)] + unaLista[:]
        while (i > 0):
            self.infiltAbajo(i)
            i = i - 1

    def __str__(self):
        """
        Permite visualizar  el monticulo

        Returns
        -------
        str de los elementos de la lista

        """
        return str(self.listaMonticulo)
     
    def __iter__(self):
        """
        Permite iterar sobre el monticulo desde el elemento en posicion 1

        Returns
        -------
        iter sobre la lista

        """
        return iter(self.listaMonticulo[1:])
    
    
    def decrementarClave(self,valor,clave_nueva):
        """
        Permite disminuir la clave de un elemento y reubicarlo a mayor prioridad

        Parameters
        ----------
        valor : elemento que se busca
        clave_nueva : nueva clave a asignar

        Returns
        -------
        None.

        """
        contador = self.tamanio
        for i in range(contador):
            if self.listaMonticulo[i][1] == valor:
                self.listaMonticulo[i] = (clave_nueva,self.listaMonticulo[i][1])
                self.infiltrarArriba(i)
                break
            