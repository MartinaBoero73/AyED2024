# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 16:09:07 2023

@author: Martina y Anibal
"""

from modulo.Temperaturas_DB import Temperaturas_DB
import unittest

class TestTemperatura_DB(unittest.TestCase):
    """
    Test de la clase Temperatura_DB

    """
    
    def setUp(self):
        """
        Inicializa dos bases de datos y comienza a guardar temperaturas

        Returns
        -------
        None.

        """
        #donde creo las fechas y creo el registro
        self.BaseDeDatos = Temperaturas_DB()
        self.OtraBD = Temperaturas_DB()
        self.BaseDeDatos.guardar_temperatura('20230812',17)
        self.BaseDeDatos.guardar_temperatura('20230719',15)
        self.BaseDeDatos.guardar_temperatura('20230316',0)
        self.BaseDeDatos.guardar_temperatura('20230802',12)
        self.BaseDeDatos.guardar_temperatura('20231109',30)
        
        
    def test_guardar_temperatura(self):
        """
        Prueba el metodo guardar_temperatura de la clase.
        
        Agrega temperaturas en una nueva BD, las muestra en una lista 
        y compara con el resultado esperado
        Tambien prueba devolver temperaturas y compararlas con el resultado esperado
        Es decir, este test presupone que los metodos de mostrar_temperaturas y 
        devolver_termperatura funcionan correctamente
        """
        lista = [36,6,2,12]
        self.OtraBD.guardar_temperatura('20231015', 12)
        self.OtraBD.guardar_temperatura('20230526', 6)
        self.OtraBD.guardar_temperatura('20230731', 2)
        self.OtraBD.guardar_temperatura('20230108', 36)
        lista_obt = self.OtraBD.mostrar_temperaturas('20230108', '20231015')
        self.assertEqual(lista, lista_obt)
        
        lista2 = [36,30,6,2,12]
        self.OtraBD.guardar_temperatura('20230225', 30)
        lista_obt2 = self.OtraBD.mostrar_temperaturas('20230108', '20231015')
        self.assertEqual(lista2, lista_obt2)
        
        lista3 = [36,30,27,18,6,2,5,21,12,16]
        self.OtraBD.guardar_temperatura('20230816', 5)
        self.OtraBD.guardar_temperatura('20230401', 18)
        self.OtraBD.guardar_temperatura('20230315', 27)
        self.OtraBD.guardar_temperatura('20231021', 16)
        self.OtraBD.guardar_temperatura('20230926', 21)
        lista_obt3 = self.OtraBD.mostrar_temperaturas('20230108', '20231021')
        self.assertEqual(lista3, lista_obt3)
        
        val_obt = self.OtraBD.devolver_temperatura('20230926')
        self.assertEqual(21, val_obt)
        
        val_obt2 = self.OtraBD.devolver_temperatura('20230225')
        self.assertEqual(30, val_obt2)

     
    def test_devolver_temperatura(self): 
        """
        Prueba el metodo devolver_temperatura de la clase
        
        Comprueba que el metodo devuelva correctamente la temperatura esperada
        guardada previamente en el setup usando el metodo guardar_temperatura
        
        """
        temperatura_esperada = 17
        temperatura_de_la_fecha = self.BaseDeDatos.devolver_temperatura('20230812')        
        
        self.assertEqual(temperatura_esperada,temperatura_de_la_fecha)
        
    def test_max_temp_rango(self):
        """
        Prueba el metodo max_temp_rango de la clase
        Comprueba que la temperatura maxima obtenida sea la correcta en dos casos:
            En el rango completo
            En un rango reducido 
        """
        #Prueba con el rango entero
        grados_max = 30
        grados_obtenidos = self.BaseDeDatos.max_temp_rango('20230316', '20231109')
        self.assertEqual(grados_max,grados_obtenidos)
        
        #Rango reducido: (del 19 de julio a agosto 12, donde la temp_max = 17)
        grados_max = 17
        grados_obtenidos = self.BaseDeDatos.max_temp_rango('20230719', '20230812')
        self.assertEqual(grados_max,grados_obtenidos)
        
        
    def test_min_temp_rango(self):
        """
        Prueba el metodo min_temp_rango de la clase
        Comprueba que la temperatura minima obtenida sea la correcta en dos casos:
            En el rango completo
            En un rango reducido 
        """
        #rango completo
        grados_min = 0
        grados_obtenidos =  self.BaseDeDatos.min_temp_rango('20230316', '20231109')
        self.assertEqual(grados_min,grados_obtenidos)
        
        #rango acotado
        grados_min = 12
        grados_obtenidos =  self.BaseDeDatos.min_temp_rango('20230719', '20230812')
        self.assertEqual(grados_min,grados_obtenidos)
        
        
    def test_temp_extremos_rango(self):
        """
        Prueba el metodo temp_extremos_rango de la clase
        
        Comprueba que las temperaturas minima y maxima obtenidas sean las correctas en los casos:
            de rango con extremos incluidos en el registro
            de rango con extremos inexistentes en el rango
            de rango con una fecha existente y la otra no
        """
       
       # Con fechas existentes:
        tup_resultado = self.BaseDeDatos.temp_extremos_rango('20230316', '20231109')
        tup_esperada = (0,30)   
        self.assertEqual(tup_esperada,tup_resultado)
        
        # Con fechas no existentes (posterior a la ultima cargada y anterir a la primera):    
        tup_resultado = self.BaseDeDatos.temp_extremos_rango('20230310', '20231125')
        self.assertEqual(tup_esperada,tup_resultado)
        # Con fechas uno en rango y otra no 
        tup_esperada = (0,17)
        tup_resultado = self.BaseDeDatos.temp_extremos_rango('20230310', '20230812')
        self.assertEqual(tup_esperada,tup_resultado)    
        #-----
        tup_esperada = (12,30)
        tup_resultado = self.BaseDeDatos.temp_extremos_rango('20230719', '20231231')
        self.assertEqual(tup_esperada,tup_resultado)    
        
        
    def test_mostrar_temperaturas(self):
        """
        Test del metodo msotrar_temperaturas de la clase
        
        Se crean listas con los valores esperados y se comparan con las devueltas por el metodo
       
        """
        lista = [0,15,12,17,30]
        lista_obt = self.BaseDeDatos.mostrar_temperaturas('20230316', '20231109')
        self.assertEqual(lista, lista_obt)
        
        lista = [0,15,12,17]
        lista_obt = self.BaseDeDatos.mostrar_temperaturas('20230316', '20230815')
        self.assertEqual(lista, lista_obt)
        
        lista = [12,17,30]
        lista_obt = self.BaseDeDatos.mostrar_temperaturas('20230721', '20231109')
        self.assertEqual(lista, lista_obt)
        
        lista = [0,15,12,17,30]
        lista_obt = self.BaseDeDatos.mostrar_temperaturas('20230303', '20231129')
        self.assertEqual(lista, lista_obt)
        
        
    def test_borrar_temperatura(self):
        """
        Test del metodo borrar_temperatura de la clase
        
        Se comprueba que el metodo elimine correctamente los nodos con la clave indicada 
        y recorre la base de datos para comprobar que el nodo se haya removido efectivamente
        """
        #pruebo eliminar la raiz, tiene ambos hijos
        variable = True
        eliminado = self.BaseDeDatos.borrar_temperatura('20230719')
        for nodo in self.BaseDeDatos:
            # print(nodo.clave)
            if nodo == eliminado:
                variable = False
                break
        self.assertTrue(variable)
    
        #ahora elimino de la nueva raiz un nodo hoja
        variable = True
        eliminado = self.BaseDeDatos.borrar_temperatura('20230802')
        for nodo in self.BaseDeDatos:
            # print(nodo.clave)
            if nodo == eliminado:
                variable = False
                break
        self.assertTrue(variable)
        
        #Vuelvo a agregar la recientemente borrada para eliminar su nodo padre, y asi chequear el caso donde haya un hijo
        self.BaseDeDatos.guardar_temperatura('20230802', 12)
        variable = True
        eliminado = self.BaseDeDatos.borrar_temperatura('20230316')
        for nodo in self.BaseDeDatos:
            # print(nodo.clave)
            if nodo == eliminado:
                variable = False
                break
            self.assertTrue(variable)
            
            
    def test_mostrar_cantidad_muestras(self):
        """
        Test del metodo mostrar_cantidad_muestras de la clase
        
        Se verifica que el tamanio de la muestra sea el de la cantidad de muestras agregadas en el setup
        """
        
        tamanio_obtenido = self.BaseDeDatos.mostrar_cantidad_muestras()
        tamanio_conocido = 5 
        # print(f"conocido:{tamanio_conocido}")
        # print(f"funcion:{tamanio_obtenido}")
        self.assertEqual(tamanio_obtenido, tamanio_conocido)
    
if __name__ == "__main__":
    unittest.main()
        
        
