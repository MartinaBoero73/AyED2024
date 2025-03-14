# -*- coding: utf-8 -*-
"""
Created on Mon May  1 19:28:11 2023

@author: anibal y martina
"""
from modulos.juego_guerra import *


if __name__ == '__main__':

    semilla = 190
    juego = JuegoGuerra(semilla)
    juego.iniciar_juego()