# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 11:43:30 2023

@author: Anibal y Martina
"""
import random

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
        
        if self.tamanio == 0:
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
       
        if self.tamanio == 0:
            self.cabeza = n1
            self.cola=n1
            
        else:
            n1.anterior=self.cola
            self.cola.siguiente=n1
            self.cola=n1
        
        self.tamanio+=1
        
   
        
    def insertar(self,item,posicion):
        """
        Inserta un elemento en una posicion a eleccion de la lista
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
        extrae el dato alojado en la posicion pasada por parametro.
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
        Realiza una copia de la lista elemento a elemento y devuelve la copia.
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
        Recibe una lista como argumento y retorna la lista actual con la lista pasada como parámetro concatenada al final de la primera
        Parametros
        ----------
        Lista :  una lista doblemente enlazada
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
        lista3 = self.copiar()
        return lista3.concatenar(Lista)
  
    
    def invertir(self):
        """
        Almaceno los datos de la cabeza y la cola para no perderlos, luego creo una variable [temp]oral 
        que almacene la cabeza y procedo a cambiar sus anteriores y los siguientes y avanzando en la lista hasta invertirla completamente.
        Luego redefino cabeza y cola invirtiendo las almacenadas.
        
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
        Ordena los elementos de la lista de "menor a mayor". La lista se ordena sobre sí misma con un algoritmo de insercion
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
            
            
            
class ColaDoble:
    def __init__(self):
        self.items = ListaDobleEnlazada()
        
    def tamanio(self):
        return self.items.tamanio

    def __str__(self):
        return str(self.items)

    def esta_vacia(self):
        return self.items.esta_vacia() 

    def agregarArriba (self, item):
        self.items.agregar_al_inicio(item)
        
    def agregarAbajo (self, item):
        self.items.agregar_al_final(item)
        
    def removerArriba (self):
        return self.items.extraer(0)
    
    def removerAbajo (self):
        return self.items.extraer()
    
    def concatenar (self, lista2):
        self.items.concatenar(lista2)
     
    def copiar (self):
        return self.items.copiar()


class Carta:
    def __init__(self, valor, palo):
       self.valor=valor
       self.palo=palo
       
       
    def __gt__ (self, nuevacarta):
        
        valor1=self.valor
        valor2=nuevacarta.valor
        
        valoresNum = {
            'J' : 11,
            'Q' : 12,
            'K' : 13,
            'A' : 14
            }
        if type(self.valor) == str:
            valor1 = valoresNum[self.valor]
        
        if type(nuevacarta.valor) == str:
            valor2 = valoresNum[nuevacarta.valor]   
            
            
        return valor1>valor2
        
    
    def __eq__ (self, nuevacarta):
        
        valor1=self.valor
        valor2=nuevacarta.valor
        
        valoresNum = {
            'J' : 11,
            'Q' : 12,
            'K' : 13,
            'A' : 14
            }
        if type(self.valor) == str:
            valor1 = valoresNum[self.valor]
        
        if type(nuevacarta.valor) == str:
            valor2 = valoresNum[nuevacarta.valor]   
            
            
        return valor1==valor2

    def __str__(self):
       return str(str(self.valor) + self.palo)
   
    def __repr__(self):
       """adentro de una lista"""
       return str(str(self.valor) + self.palo)    
   

class JuegoGuerra:
    
    def __init__(self,random_seed = 0):
        self.seed = random_seed
        
        self.mazo = ColaDoble()
        self.mazoJ1 =  ColaDoble()
        self.mazoJ2 =  ColaDoble()
        self.turnos_jugados = 0
        
        self.ganador = ''
        self.empate = False
       
        
    def inicializar_mazo (self): 
        valores =  [2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 ,'J','Q','K','A']
        palos = ['♠', '♥', '♦', '♣'] 
        cartas=[]
        for i in range(len(valores)):
            for j in range(len(palos)):
                carta = Carta(valores[i],palos[j])
                cartas.append(carta) 
        print (cartas)
      
         
        random.seed(self.seed) 
        random.shuffle(cartas)
        print (cartas)
        for i in range(len(cartas)):
            self.mazo.agregarArriba(cartas[i])
        print (self.mazo)
            
    def repartir (self):
        contador = 0
        while (self.mazo.tamanio()!= 0):
            carta_a_repartir = self.mazo.removerArriba()
            if (contador%2 == 0):
                self.mazoJ1.agregarArriba(carta_a_repartir)
            else:
                self.mazoJ2.agregarArriba(carta_a_repartir)
            contador += 1
        

        
    def jugar(self):
        
        carta1 = self.mazoJ1.removerArriba()
        carta2 = self.mazoJ2.removerArriba()
      
      
        if  carta1 > carta2:
            self.mostrar_por_consola(carta1,carta2)
            self.mazoJ1.agregarAbajo(carta1)
            self.mazoJ1.agregarAbajo(carta2)
          
        elif carta1 < carta2:
            self.mostrar_por_consola(carta1,carta2)
            self.mazoJ2.agregarAbajo(carta1)
            self.mazoJ2.agregarAbajo(carta2)
  
        else:
            self.guerra(carta1,carta2)    
            
        self.turnos_jugados +=1
                
                
    def mostrar_por_consola(self,carta1,carta2):
        print("--------------------------------------------")
        print("Turno: ", self.turnos_jugados)
        
        
        print('\n',"Jugador 1: ")
        cont1= self.mazoJ1.tamanio()
        while cont1 !=0:
            print("-X", end = '')
            cont1 -= 1
            
        print('\n','\n',carta1, carta2, '\n')
        
        
        print("Jugador 2: ")
        cont2= self.mazoJ2.tamanio()
        while cont2 !=0:
            print("-X", end = '')
            cont2 -= 1
        print('\n', "--------------------------------------------")
        print('\n','\n')
        
        
    def guerra(self, carta1, carta2):
        
       print("--------------------------------------------")
       print("-------------**** Guerra!! ****-------------")
      
       print("Turno: ",self.turnos_jugados)

       lista = ColaDoble()
       lista.agregarAbajo(carta1)
       lista.agregarAbajo(carta2)
       
       
       salir = False
       
       while carta1 == carta2:
           for i in range (3): 
               if self.mazoJ1.tamanio() > 0 and self.mazoJ2.tamanio() > 0 :
                   lista.agregarAbajo(self.mazoJ1.removerArriba())
                   lista.agregarAbajo(self.mazoJ2.removerArriba())
               if self.mazoJ1.tamanio() == 0: 
                   self.ganador = 'jugador 2'
                   salir = True
                   break
               if self.mazoJ2.tamanio() == 0: 
                   self.ganador = 'jugador 1'
                   salir = True
                   break
           if salir == True:
               break
           
           carta1= self.mazoJ1.removerArriba()
           carta2= self.mazoJ2.removerArriba()
           lista.agregarAbajo(carta1)
           lista.agregarAbajo(carta2)
        
       copialista = lista.copiar() 
     
          
       print('\n',"Jugador 1: ")
       cont1= self.mazoJ1.tamanio()
       while cont1 != 0:
           print("-X", end = '')
           cont1 -= 1 
    
        
       #PARA MOSTRAR LA LISTA DE LAS CARTAS EN MESA
       print ('\n')
        
       print (copialista.extraer(0), '' , end = '')
       print (copialista.extraer(0),'', end = '')

       while (copialista.tamanio > 0):
           
           contador = 1
           while copialista.tamanio != 0 and contador <= 6 :
               copialista.extraer(0)
               print('- X ', end = '')
               contador += 1
           if (copialista.tamanio > 0):
               print (copialista.extraer(0),'', end = '')
               print (copialista.extraer(0),'', end = '')
           

           
       print('\n', '\n' , "Jugador 2: ")
       cont2= self.mazoJ2.tamanio()
       while cont2 !=0:
           print("-X", end = '')
           cont2 -= 1
       print ('\n')


       # Agregar las cartas en mesa al mazo del jugador ganador
       if  carta1 > carta2 :
           if self.mazoJ1.tamanio() > 0:
               self.mazoJ1.concatenar(lista)
           else: 
               self.mazoJ1 = lista
         
       elif carta1 < carta2 :
           if self.mazoJ2.tamanio() > 0:
               self.mazoJ2.concatenar(lista)
           else:
               self.mazoJ2 = lista
      
       
    def iniciar_juego (self):
        self.inicializar_mazo()
        self.repartir()
       
        
        while self.ganador == '' and self.turnos_jugados<=10000:
            self.jugar()
           
            if self.mazoJ1.tamanio() == 0:
                self.ganador = 'jugador 2'
            if self.mazoJ2.tamanio() == 0:
                self.ganador = 'jugador 1'
            
            
            
        print ('\n')    
        print("-----------------------------------------------------------")
        if self.turnos_jugados == 10001:
            self.empate = True
            print("                   *****empate*****                       ")
        elif self.ganador == 'jugador 1':
            print("                   ***** jugador 1 gana la partida *****             ")
        elif self.ganador == 'jugador 2':
            print("                   ***** jugador 2 gana la partida *****             ")
    
