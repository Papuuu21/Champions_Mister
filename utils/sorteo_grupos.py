
import random as rd
import pandas as pd
import time as tm
import reflex as rx


#* Funcion sorteo de fase de grupos:
def sorteo_grupos(equipos):
    grupo_1 = []
    grupo_2 = []

    rd.shuffle(equipos)
    
    for equipo in equipos:
        idx = equipos.index(equipo)
        if idx % 2 != 0:
            grupo_1 += [equipo]
            
        else:
            grupo_2 += [equipo] 
        
    return grupo_1, grupo_2


