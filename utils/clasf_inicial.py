
import pandas as pd

def clasificacion_inicial(grupo):
    puesto = pd.DataFrame(list(range(1, 7)), columns = ['Pos.'])
    #* Definir las columnas
    columnas = ['Puntos', 'Nºs 1º', 'Max.pts', 'G', 'P', 'E', 'PJ']
    #* Valor predeterminado para cada celda (puedes cambiar esto a cualquier valor)
    valor_predeterminado = 0
    #pts = pd.DataFrame([0, 0, 0, 0, 0, 0], columns = ['Puntos'])
    equipos = pd.DataFrame(grupo, columns=['Equipos'])

    #* Crear un DataFrame lleno con el valor predeterminado
    df = pd.DataFrame(valor_predeterminado, index=range(len(grupo)), columns=columnas)

    #* Concatenamos todos los df para crear la clasificacion con los datos necesarios:
    df = pd.concat([equipos, df, puesto], axis = 1)
    clasificacion_df = df.set_index('Pos.', drop=True, append=False, inplace=False)

    #* Aplicar estilo para centrar el contenido
    #clasificacion_df = df.style.set_properties(**{'text-align': 'center'})

    return clasificacion_df