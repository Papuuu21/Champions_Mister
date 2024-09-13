

#! FASE DE GRUPOS DESDE EL SORTEO HASTA LOS PTS DE LA JORNADA 1: (EJEMPLO COMPLETO DE LA FASE DE GRUPOS)
#* Importamos las librerias necesarias:
import random as rd

import time as tm

from utils.sorteo_grupos import  sorteo_grupos
from utils.clasf_inicial import clasificacion_inicial
from utils.generar_enfrent import generar_enfrentamientos
from utils.vuelta_grupos import vuelta_gr
from utils.df_enfrentamientos import df_ida_o_vuelta
from utils.enfrentamientos_sinVS import df_partidos
from utils.partidos_jornadas import partidos_jornadas
from utils.pts_jornada import pts_por_jornada
from utils.comparar_max_pts import comparar_max_pts
from utils.ver_ganador import ver_1x2
from utils.actualizar_clasf import actualizar_clasificacion

import pandas as pd
import streamlit as st


# Definir participantes
PARTICIPANTES = ['Armada', 'Coquina', 'Diego', 'Fale', 'Gonzo', 'Kero', 'Kike', 'Lope', 'Palop', 'Papu', 'Ruso', 'Tony']

# Iniciar app con Streamlit
st.title('Torneo Futbolístico')

# Sortear los grupos
st.header('Sorteo de Grupos')
if st.button('Iniciar Sorteo'):
    grupos = sorteo_grupos(PARTICIPANTES)
    grupo1, grupo2 = grupos[0], grupos[1]
    df_g1 = pd.DataFrame(grupo1, columns = ['GRUPO A'])
    df_g2 = pd.DataFrame(grupo2, columns = ['GRUPO B'])
    df_g = pd.concat([df_g1, df_g2], axis = 1)
    st.dataframe(df_g)

    # Mostrar la clasificación inicial de los grupos
    clasificacion_inicial_g1 = clasificacion_inicial(grupo1)
    clasificacion_inicial_g2 = clasificacion_inicial(grupo2)

    st.subheader('Clasificación Inicial')
    st.write('**Grupo 1**')
    st.dataframe(pd.DataFrame(clasificacion_inicial_g1))

    st.write('**Grupo 2**')
    st.dataframe(pd.DataFrame(clasificacion_inicial_g2))

    # Generar los partidos de ida para el Grupo 1
    #* ENFRENTAMIENTOS DEL GRUPO 1:
    #* Generar partidos de ida y de vuelta del grupo 1:
    ida_gr1 = generar_enfrentamientos(grupo1) #* Generar partidos de ida
    vuelta_gr1 = vuelta_gr(ida_gr1) #* Generar partidos de vuelta

    #* Crear DF de los partidos de ida y de vuelta:
    df_ida_gr1 = df_ida_o_vuelta(ida_gr1)  #* Generar DF de los partidos de ida
    df_vuelta_gr1 = df_ida_o_vuelta(vuelta_gr1, 6) #* El 6 indica el inicio de la jornada de los partidos de vuelta
    idx_gr1 = 'GRUPO 1'
    calendario_gr1 = pd.concat([df_ida_gr1, df_vuelta_gr1], axis = 1) #* Crear dataframe con todos los partidos de ida y vuelta gr1
    calendario_gr1['GRUPO'] = idx_gr1
    calendario_gr1.set_index('GRUPO', drop=True, append=False, inplace=True) #* Cambiar el indice del DF para distinguir los grupos al juntarlos
    #print(calendario_gr1) #* Usar para VISUALIZAR LOS PARTIDOS DE IDA Y VUELTA DEL GRUPO 1

    #* ENFRENTAMIENTOS DEL GRUPO 2:
    #* Generar partidos de ida y de vuelta del grupo 2:
    ida_gr2 = generar_enfrentamientos(grupo2) #* Generar partidos de ida
    vuelta_gr2 = vuelta_gr(ida_gr2) #* Generar partidos de vuelta

    #* Crear DF de los partidos de ida y de vuelta:
    df_ida_gr2 = df_ida_o_vuelta(ida_gr2)  #* Generar DF de los partidos de ida
    df_vuelta_gr2 = df_ida_o_vuelta(vuelta_gr2, 6) #* El 6 indica el inicio de la jornada de los partidos de vuelta
    idx_gr2 = 'GRUPO 2'
    calendario_gr2 = pd.concat([df_ida_gr2, df_vuelta_gr2], axis = 1) #* Crear dataframe con todos los partidos de ida y vuelta gr2
    calendario_gr2['GRUPO'] = idx_gr2
    calendario_gr2.set_index('GRUPO', drop=True, append=False, inplace=True) #* Cambiar el indice del DF para distinguir los grupos al juntarlos
    #print(calendario_gr2) #* Usar para VISUALIZAR LOS PARTIDOS DE IDA Y VUELTA DEL GRUPO 2

    #* CALENDARIO AMBOS GRUPOS:
    calendario_grupos = pd.concat([calendario_gr1, calendario_gr2], axis = 0)
    #print(calendario_grupos)

    # Mostrar el calendario general
    st.header('Calendario General')
    st.dataframe(calendario_grupos)

    #* PARTIDOS DE LA JORNADA 1:
    ida_g1 = df_partidos(ida_gr1)
    ida_g2 = df_partidos(ida_gr2)
    gr1_jor1 = partidos_jornadas(ida_g1)
    gr2_jor1 = partidos_jornadas(ida_g2)
    jornada_actual = pd.concat([gr1_jor1, gr2_jor1], axis = 0)
    st.header('Jornada Actual')
    st.dataframe(jornada_actual)

# Footer
st.write('Creado con ❤️ por el Comité del Torneo')

