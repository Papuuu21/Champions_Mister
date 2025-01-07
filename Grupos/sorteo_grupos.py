
import random as rd
import time as tm
from IPython.display import display, clear_output
import pandas as pd
from IPython.display import HTML
import ipywidgets as widgets

#* Lista de 12 participantes
PARTICIPANTES = ['Armada', 'Coquina', 'Diego', 'Fale', 'Gonzo', 'Kero', 'Kike', 'Lope', 'Palop', 'Papu', 'Ruso', 'Tony']

# Función que se ejecuta al hacer clic en el botón
def iniciar_sorteo(b):
    print("Sorteo iniciado...")
    sorteo_dinamico()
    
#* Reiniciar los grupos
grupo_A = []
grupo_B = []

#* Función que muestra la tabla en proceso
def mostrar_progreso():
    #* Crear DataFrame con los grupos (rellenar con espacios vacíos para mantener el formato)
    max_len = max(len(grupo_A), len(grupo_B))
    data = {
        "Grupo A": grupo_A + [""] * (max_len - len(grupo_A)),
        "Grupo B": grupo_B + [""] * (max_len - len(grupo_B))
    }
    df = pd.DataFrame(data)
    
    #* Mostrar la tabla con estilo futurista
    clear_output(wait=True)
    display(HTML(df.to_html(index=False, classes='futuristic-table')))
    print("Sorteo en progreso...")

# Función que realiza el sorteo con tabla dinámica
def sorteo_dinamico():
    #* Mezclar los participantes
    rd.shuffle(PARTICIPANTES)
    
    #* Limpiar los grupos
    grupo_A.clear()
    grupo_B.clear()

    #* Simular el sorteo con un retardo, actualizando la tabla en tiempo real
    for i, participante in enumerate(PARTICIPANTES):
        if i % 2 == 0:
            grupo_A.append(participante)
        else:
            grupo_B.append(participante)
        
        #* Mostrar el progreso de la tabla
        mostrar_progreso()
        
        #* Pausa de 1 segundo
        tm.sleep(2)
    
    #* Mostrar el resultado del sorteo
    df = mostrar_sorteo()
    
    #* Guardar el DataFrame en un archivo Excel
    df.to_excel("sorteo_grupos.xlsx", index=False)
    print("El sorteo ha finalizado y los grupos se han guardado en 'sorteo_grupos.xlsx'.")
    return df

#* Función para mostrar el sorteo
def mostrar_sorteo():
    clear_output(wait=True)
    #* Crear DataFrame con los grupos
    data = {
        "Grupo A": grupo_A,
        "Grupo B": grupo_B
    }
    df = pd.DataFrame(data)
    
    #* Mostrar la tabla con estilo futurista
    print("Grupos A y B:")
    display(HTML(df.to_html(index=False, classes='futuristic-table')))
    
    

#* Iniciar el sorteo dinámico
#sorteo_dinamico()

#* Estilo futurista para la tabla
display(HTML("""
<style>
.futuristic-table {
    font-family: 'Courier New', monospace;
    color: #00FFFF;
    background-color: #000000;
    border: 1px solid #00FFFF;
    border-collapse: collapse;
    width: 50%;
    margin-left: auto;
    margin-right: auto;
}
.futuristic-table th, .futuristic-table td {
    border: 1px solid #00FFFF;
    padding: 8px;
    text-align: center;
}
.futuristic-table th {
    background-color: #001f00;
}
</style>
"""))

# Crear el botón
boton_sorteo = widgets.Button(
    description="Iniciar Sorteo",
    disabled=False,
    button_style='danger',  # 'success', 'info', 'warning', 'danger' o ''
    tooltip='Haz clic para iniciar el sorteo',
    icon='check'  # (opcional) Agregar un icono de FontAwesome
)

# Asignar la función al evento de clic del botón
boton_sorteo.on_click(iniciar_sorteo)

# Mostrar el botón
display(boton_sorteo)

