

import pandas as pd
import  streamlit as st

c_ini_gA = pd.read_excel('data/clasf_jor5_gA.xlsx')
c_ini_gB = pd.read_excel('data/clasf_jor5_gB.xlsx')
calendario = pd.read_excel('data/calendario_grupos.xlsx')
jor_actual = pd.read_excel('data/jornada_6_inicial.xlsx')
jor_pasada = pd.read_excel('data/j5_actualizada.xlsx')

# Iniciar app con Streamlit
st.title('Torneo Futbolístico')

st.header('----Fase de Grupos----')

st.subheader('Clasificación Jornada 4')
st.write('**Grupo A**')
st.dataframe(c_ini_gA)

st.write('**Grupo B**')
st.dataframe(c_ini_gB)

st.header('Jornada Actual')
st.dataframe(jor_actual)

st.header('Jornada Anterior')
st.dataframe(jor_pasada)

st.header('Calendario General')
st.dataframe(calendario)





