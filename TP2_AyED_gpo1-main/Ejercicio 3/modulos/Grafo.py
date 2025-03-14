# -*- coding: utf-8 -*-
"""
@author: Anibal y Martina
"""

class Vertice:
    def __init__(self,clave):
        """
        Constructor de la clase Vertice

        Parameters
        clave: str que indica el identificador del vertice
            
        """
        
        self.id = clave
        self.conectadoA = {}
        self.predecesor = None
        self.distancia = 0

    def agregarVecino(self,vecino,ponderacion=0):
        """
        Agrega un vecino al vertice actual vertice, indicando el peso o ponderacion de la union

        Parameters
        ----------
        vecino : nuevo vertice vecino
        ponderacion : ponderacion o peso de la union. Por defecto es 0

        Returns
        -------
        None.

        """
        self.conectadoA[vecino] = ponderacion

    def __str__(self):
        """
        Devuelve un str que representa al vertice

        Returns
        -------
        str para representar al vertice. Incluye la union a sus vecinos

        """
        return str(self.id) + ' conectado A: ' + str([x.id for x in self.conectadoA])

    def obtenerConexiones(self):
        """
        Devuelve los vertices vecinos del vertice acutal

        Returns
        -------
            dict_keys: lista de adyacencia del vertice

        """
        return self.conectadoA.keys()

    def obtenerId(self):
        """
        Devuelve el identificador del vertice

        Returns
        -------
        identificador del vertice

        """
        return self.id

    def obtenerPonderacion(self,vecino):
        """
        Devuelve la poderacion de la conexion del vertice actual con un vecino
        Esto luego representa costos o pesos de traslado

        Parameters
        ----------
        vecino : vertice vecino

        Returns
        -------
        int: ponderacion de la union

        """
        return self.conectadoA[vecino]
    
    def obtenerPredecesor(self):
        """
        Obtiene el predecesor del vertice.

        Returns
        -------
        Predecesor del vertice

        """
        return self.predecesor
    
    def asignarPredecesor(self,nPredecesor):
        """
        Establece el predecesor del vertice

        Parameters
        ----------
        nPredecesor : nuevo predecesor del vertice actual

        Returns
        -------
        None.

        """
        self.predecesor = nPredecesor

    def obtenerDistancia(self):
        """
        Devuelve la distancia del vertice actual

        Returns
        -------
        int: la distancia del vertice

        """
        return self.distancia
    
    def asignarDistancia(self, nuevaDist):
        """
        Asigna una nueva distancia

        Parameters
        ----------
        nuevaDist : nueva distancia a asignar al vertice

        Returns
        -------
        None.

        """
        self.distancia = nuevaDist


class Grafo:
    def __init__(self):
        """
        constructor de la clase Grafo
        se representa usando un diccionario
            claves: id 
            valores: objetos vertice

        """
        self.listaVertices = {}
        self.numVertices = 0

    def agregarVertice(self,clave):
        """
        agrega un vertice al grafo

        Parameters
        ----------
        clave : id del vertice

        Returns
        -------
        nuevoVertice : objeto vertice creado

        """
        
        self.numVertices = self.numVertices + 1
        nuevoVertice = Vertice(clave)
        self.listaVertices[clave] = nuevoVertice
        return nuevoVertice


    def obtenerVertice(self,n):
        """
        Obtiene el objeto vertice asignado a la clave n

        Parameters
        ----------
            n : clave correspondiente al vertice (id)

        Returns
        -------
            Vertice: el objeto vertice correspondiente a la clave
            None si no existe vertice con dicha clave

        """
        if n in self.listaVertices:
            return self.listaVertices[n]
        else:
            return None


    def __contains__(self,n):
        """
        metodo magico que verifica si el vertice n esta contenido en el grafo

        Parameters
        ----------
        n : clave del vertice a verificar

        Returns
        -------
        bool: True si el vertice esta contenido en el grafo, False si no.

        """
        return n in self.listaVertices

    def agregarArista(self,de,a,costo=0):
        """
        Agrega una arista o conexion entre dos vertices

        Parameters
        ----------
        de : clave del vertice de partida
        a : clave del vertice de destino.
        costo : el costo o ponderacion de la arista. The default is 0.

        Returns
        -------
        None.

        """
        if de not in self.listaVertices:
            nv = self.agregarVertice(de)
        if a not in self.listaVertices:
            nv = self.agregarVertice(a)
        self.listaVertices[de].agregarVecino(self.listaVertices[a], costo)

    def obtenerVertices(self):
        """
        Obtiene la lista con las claves de todos los vertices contenidos en el grafo

        Returns
        -------
        list: lista de las claves de todos los vertices del grafo

        """
        return self.listaVertices.keys()
    
    def obtenerCamino (self, primero, ultimo):
        """
        Genera y devuelve una cadena con un camino entre dos vertices

        Parameters
        ----------
        primero : clave del vertice de origen.
        ultimo : clave del vertice de destino.

        Returns
        -------
        recorrido : cadena con las claves de los vertices visitados.

        """
        camino = []
        vertice_inicio = self.obtenerVertice(primero)
        vertice_final = self.obtenerVertice(ultimo)
        while vertice_final:
            camino.append(vertice_final.obtenerId())
            vertice_final = vertice_final.obtenerPredecesor()
            camino.append(" - ")
            
        camino.reverse()
        recorrido = ' '.join(camino)

        return recorrido
    

    def __iter__(self):
        """
        devuelve un iterador que permite recorrer los vertices
        
        Returns
        -------
        iter: iterados de los objetos vertices

        """
        return iter(self.listaVertices.values())
    
    def __str__(self):
        """
        permite mostrar los vertices del grafo

        Returns
        -------
        None.

        """
        for vertice in self.listaVertices:
            print(vertice)
    

  