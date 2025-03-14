# -*- coding: utf-8 -*-
"""
Created on Mon May  1 18:12:46 2023

@author: Anibal y Martina
"""

from modulos.mezcladirecta import *
import unittest
import os


class TestMezclaDirecta (unittest.TestCase):
    """Test de la mezcla directa"""
    
    def setUp(self):
        crear_archivo_de_datos("datos.txt")
        
            
    def test_tamanio (self):  
        """
            Comparamos si los tamaños en kb son iguales 
            en amboss archivos, por lo que importo la galeria os que me 
            permite saber el tamaño del archivo como es requerido
        """
        tamanioArchivo1 = os.stat('datos.txt').st_size
        # print (tamanioArchivo1)
       
        ordenar_sublistas ("datos.txt", 4)
        mezcla_directa('datosord.txt', 4)
        
        tamanioArchivo2 = os.stat('datosord.txt').st_size
        # print (tamanioArchivo2)
        
        self.assertEqual(tamanioArchivo1, tamanioArchivo2, "El tamaño antes y despues de ordenar debe ser igual")
    
    
    def test_ordenamiento(self):
        """
            Comparamos si el archivo se ordenó. Ordenamos y luego mezclamos. Una vez hecho esto creamos una variable
            ordenada (booleano) que se verdadera y a medida que vamos leyendo comprobamos que ese valor nunca se haga falso
            con el assertTrue de la clase unittest
        """
        ordenar_sublistas ("datos.txt", 4)
        mezcla_directa('datosord.txt', 4)
       
        ordenado = True
        archi = open('datosord.txt', 'r')
        
        linea = archi.readline()
        # print (linea)
        while linea != '':
            linea2 = archi.readline()
            # print (linea2)
            if linea < linea2 or linea2 == '':
                ordenado = True
            else: 
                ordenado = False
                break
            linea = linea2
            
        self.assertTrue(ordenado)
        archi.close()
        
        
if __name__ == "__main__":
    unittest.main()
        