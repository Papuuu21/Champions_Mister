
import pandas as pd

def df_partidos(partidos):

    enfrentam2 = pd.DataFrame()
    for i, lista in enumerate(partidos):  #* Mostrar el numero de jornada delante de los partidos
        ser_jornada = pd.Series(lista, name = f'Jornada {i+1}') #* Crear una serie con cada jornada (CAMBIAR EL 1 POR EL 6 EN LOS DE VUELTA)
        enfrentam2[ser_jornada.name] = ser_jornada #* Anadir la serie al DF

    return enfrentam2