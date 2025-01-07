

import pandas as pd
import  streamlit as st
from PIL import Image

c_ini_gA = pd.read_excel('data/clasf_final_gA.xlsx')
c_ini_gB = pd.read_excel('data/clasf_final_gB.xlsx')
calendario = pd.read_excel('data/calendario_grupos.xlsx')
jor_actual = pd.read_excel('data/cuartos.xlsx')
jor_pasada = pd.read_excel('data/j10_actualizada.xlsx')

# Iniciar app con Streamlit
st.title('CHAMPIONS MISTER 🏆⚽')

st.header('----FASE FINAL----')
#* Cargar y mostrar la imagen al inicio
image = Image.open('data/Cuartos_CUADRO.png')
st.image(image, caption='Sorteo fase final')

st.header('----Fase de Grupos----')
st.subheader('Clasificación Final Grupos')
st.write('**Grupo A**')
st.dataframe(c_ini_gA)
st.write('**Grupo B**')
st.dataframe(c_ini_gB)

st.header('Resultados Cuartos de final')
st.dataframe(jor_actual)

st.header('Jornada Anterior')
st.dataframe(jor_pasada)

st.header('Calendario fase de grupos')
st.dataframe(calendario)





