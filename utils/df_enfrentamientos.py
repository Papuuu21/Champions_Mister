

import pandas as pd
from utils.partidos_str_vs import partidos_str

#* Enfrentamientos de ida o de  vuelta:
def df_ida_o_vuelta(ida_vuelta, jor_inicial = 1): #* 1º param: si es ida o vuelta, 2º param: en que jornada empieza la ida o vuelta
    enfrentam = pd.DataFrame()
    for i, lista in enumerate(ida_vuelta):  #* Mostrar el numero de jornada delante de los partidos
        lista_str = partidos_str(lista)
        ser_jornada = pd.Series(lista_str, name = f'Jornada {i+jor_inicial}') #* Crear una serie con cada jornada
        enfrentam[ser_jornada.name] = ser_jornada #* Anadir la serie al DF
        
    return enfrentam