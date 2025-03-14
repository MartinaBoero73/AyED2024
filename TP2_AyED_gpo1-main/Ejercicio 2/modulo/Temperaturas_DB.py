# -*- coding: utf-8 -*-
"""
Created on Mon May 29 10:52:50 2023

@author: anibal y Martina
"""
from modulo.AVL import AVL
    
   
class Temperaturas_DB:
    
    def __init__(self):
        """
        Constructor de la clase Temperaturas_DB

        """
        self.registro = AVL()
        
    def __iter__(self):
        """
        permite iterar sobre los nodos en inorden

        """
        return self.registro.raiz.__iter__()
        
    def guardar_temperatura(self, fecha, temperatura):
        """
        agrega al registro una temperatura asociada a la fecha

        Parameters
        ----------
        fecha : str en formato aaaammdd, clave del nodo
        temperatura : carga util del nodo asociado a esa fecha

        Returns
        -------
        None.

        """
        self.registro.agregar(fecha,temperatura)
     
        
    def devolver_temperatura(self,fecha): 
        """
        devuelve la medida de temperatura en un afecha determinada

        Parameters
        ----------
        fecha : clave del nodo cuya carga util se desea obtener

        Returns
        -------
        temperatura asociada a esa fecha, None si no existe tal fecha en el registro

        """
        return self.registro.obtener(fecha)
        
    
    def max_temp_rango(self,fecha1, fecha2): 
        """
        devuelve la temperatura maxima en el rango entre fecha1  y fecha2

        Parameters
        ----------
        fecha1 : clave menor del rango
        fecha2 : clave mayor del rango

        Returns
        -------
        temperatura_max : temperatura maxima registrada en el rango, None si no hay fecha registrada en el rango

        """
       
        if fecha1>=fecha2:
            return None
        
        temperatura_max = -2000
        
        for nodo in iter(self.registro.raiz):
            if nodo.clave<fecha1:
                continue
            elif nodo.clave > fecha2:
                break
            elif nodo.clave>=fecha1:
                # print(nodo.clave)
                temperatura_nueva = self.devolver_temperatura(nodo.clave)
                if temperatura_nueva>temperatura_max:
                    temperatura_max = temperatura_nueva
                
        if temperatura_max == -2000:
            return None
        
        return temperatura_max
    
    def min_temp_rango(self,fecha1, fecha2): 
        """
        devuelve la temperatura minimo en el rango entre fecha1  y fecha2

        Parameters
        ----------
        fecha1 : clave menor del rango
        fecha2 : clave mayor del rango

        Returns
        -------
        temperatura_min : temperatura minima registrada en el rango, None si no hay fecha registrada en el rango

        """
        if fecha1>=fecha2:
            return None
        
        
        temperatura_min = 2000
        
        for nodo in iter(self.registro.raiz):
            if nodo.clave<fecha1:
                continue
            elif nodo.clave > fecha2:
                break
            elif nodo.clave>=fecha1:
                # print(nodo.clave)
                temperatura_nueva = self.devolver_temperatura(nodo.clave)
                if temperatura_nueva<temperatura_min:
                    temperatura_min = temperatura_nueva
                
        if temperatura_min == 2000:
            return None
        
        return temperatura_min
    
    def temp_extremos_rango(self,fecha1, fecha2):
        """
        devuelve una tupla de temperaturas minima y maxima en el rango entre fecha1  y fecha2

        Parameters
        ----------
        fecha1 : clave menor del rango
        fecha2 : clave mayor del rango

        Returns
        -------
        tupla con elementos:
            temperatura_min : temperatura minima registrada en el rango, None si no hay fecha registrada en el rango
            temperatura_max : temperatura maxima registrada en el rango, None si no hay fecha registrada en el rango
       

        """
        temperatura_min = self.min_temp_rango(fecha1, fecha2)
        temperatura_max = self.max_temp_rango(fecha1, fecha2)
        return temperatura_min,temperatura_max
        
    def borrar_temperatura(self,fecha): 
        """
        recibe una fecha y elimina del árbol la medición correspondiente a esa fecha.
        

        Parameters
        ----------
        fecha : clave del nodo a eliminar

        Returns
        -------
        # eliminado : dato eliminado

        """
        self.registro.eliminar(fecha)
        return fecha
    
    def mostrar_temperaturas(self,fecha1, fecha2): 
        """
        muestra por consola un listado de las mediciones de temperatura en el rango recibido por parámetro, ordenado por fechas

        Parameters
        ----------
        fecha1 : clave menor del rango
        fecha2 : clave mayor del rango

        Returns
        -------
        lista : list con las temperaturas del rango

        """
        " "
        lista = []        
        #Sabemos que no es muy eficiente debido a que recorre todo el arbol, pero con las implementaciones realizadas para evitar esto, no logramos concretarlo de otra manera.
        for nodo in iter(self.registro.raiz):
            if nodo.clave<fecha1:
                continue
            elif nodo.clave > fecha2:
                break
            elif nodo.clave>=fecha1:
                temperatura = self.devolver_temperatura(nodo.clave)
                lista.append(temperatura)
                
        return lista        
        # print ('listado de mediciones en un rango',lista)
        
    def mostrar_cantidad_muestras(self): 
        "muestra por consola la cantidad de muestras de la BD."
        
        longitud = self.registro.longitud()
        return longitud
        # print ('la cantidad de muestras es de:', longitud)
        


