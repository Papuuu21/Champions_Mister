import streamlit as st
import pandas as pd

c_ini_gA = pd.read_excel('data/clasificacion_inicial_A.xlsx')
c_ini_gB = pd.read_excel('data/clasificacion_inicial_B.xlsx')
calendario = pd.read_excel('data/calendario_grupos.xlsx')
jor_actual = pd.read_excel('data/jornada_1.xlsx')
# Iniciar app con Streamlit
st.title('Torneo Futbolístico')

st.header('----Fase de Grupos----')

st.subheader('Clasificación Inicial')
st.write('**Grupo A**')
st.dataframe(c_ini_gA)

st.write('**Grupo B**')
st.dataframe(c_ini_gB)

st.header('Calendario General')
st.dataframe(calendario)

st.header('Jornada Actual')
st.dataframe(jor_actual)

