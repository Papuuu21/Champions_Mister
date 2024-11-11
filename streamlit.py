

import pandas as pd
import  streamlit as st

c_ini_gA = pd.read_excel('data/clasf_jor9_gA.xlsx')
c_ini_gB = pd.read_excel('data/clasf_jor9_gB.xlsx')
calendario = pd.read_excel('data/calendario_grupos.xlsx')
jor_actual = pd.read_excel('data/jornada_10_inicial.xlsx')
jor_pasada = pd.read_excel('data/j9_actualizada.xlsx')

# Iniciar app con Streamlit
st.title('Torneo Futbolístico')

from PIL import Image

#* Cargar y mostrar la imagen al inicio
image = Image.open('data/Sorteo_posiciones_cuartos.jpg')
st.image(image, caption='Sorteo fase final')

st.header('----Fase de Grupos----')

st.subheader('Clasificación Jornada 7')
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





