

import pandas as pd
import  streamlit as st
from PIL import Image

c_ini_gA = pd.read_excel('data/clasificacion_inicial_A.xlsx')
c_ini_gB = pd.read_excel('data/clasificacion_inicial_B.xlsx')
calendario = pd.read_excel('data/calendario_grupos.xlsx')
jor_actual = pd.read_excel('data/jornada_1_inicial.xlsx')
#jor_pasada = pd.read_excel('data/j10_actualizada.xlsx')

# Iniciar app con Streamlit
st.title('CHAMPIONS MISTER 🏆⚽')

# st.header('----FASE FINAL----')
# #* Cargar y mostrar la imagen al inicio
# image = Image.open('data/cuartos.jpg')
# st.image(image, caption='Cuartos')

st.header('----Fase de Grupos----')
st.subheader('Clasificación Jornada 1 Grupos')
st.write('**Grupo A**')
st.dataframe(c_ini_gA)
st.write('**Grupo B**')
st.dataframe(c_ini_gB)

st.header('Resultados Jornada 1')
st.dataframe(jor_actual)

#st.header('Jornada Anterior')
#st.dataframe(jor_pasada)

st.header('Calendario fase de grupos')
st.dataframe(calendario)





