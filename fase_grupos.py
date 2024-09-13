import streamlit as st
import pandas as pd


# Iniciar app con Streamlit
st.title('Torneo Futbolístico')

st.header('----Fase de Grupos----')

st.subheader('Clasificación Inicial')
st.write('**Grupo A**')
st.dataframe(pd.read_excel('data/clasificacion_inicial_A.xlsx'))

st.write('**Grupo B**')
st.dataframe(pd.read_excel('data/clasificacion_inicial_B.xlsx'))

st.header('Calendario General')
st.dataframe(pd.read_excel('data/calendario_grupos.xlsx'))

st.header('Jornada Actual')
st.dataframe(pd.read_excel('data/jornada_1.xlsx'))

