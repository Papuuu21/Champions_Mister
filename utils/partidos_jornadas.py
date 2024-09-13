
import pandas as pd
from utils.descomp_tupla_columnas import descomponer_tupla

def partidos_jornadas(df_partidos):

    df_partidos_jornada = pd.DataFrame()
    #* Aplicando la función a la columna 'datos' y creando nuevas columnas
    df_partidos_jornada[['LOCAL', 'VISITANTE']] = df_partidos['Jornada 1'].apply(descomponer_tupla) #* Usamos la función apply() para aplicar una función a una columna de un dataframe
    df_partidos_jornada[['RTDO V']] = 0 #* Añadimos las cols rtdo de cada equipo

    #* Con la insert() podemos añadir una columna donde queramos (0 = indice, 'nom_col', 0 = Valor añdido (pueden ser listas...))
    df_partidos_jornada.insert(0, 'RTDO L', 0) 

    #* Eliminando la columna original del df para ir teniendo claro que hemos usado
    df_partidos = df_partidos.drop('Jornada 1', axis=1)

    return df_partidos_jornada