

def actualizar_clasificacion(df, columna_1x2, clasificacion):
  """
  Actualiza una clasificación de equipos basada en los resultados de partidos.

  Args:
    df: DataFrame con los resultados de los partidos.
    columna_1x2: Nombre de la columna en df que contiene los resultados (1, X, 2).
    clasificación: Clasificación anterior a la jornada.

  Returns:
    DataFrame con la clasificación actualizada.

  Nota: 
    Cada vez que se activa la función realiza la suma según los datos de los argumentos de la función
  """

  #* Iterar sobre los partidos por cada fila y por cada columna:
  for _, fila in df.iterrows(): #* pone una _ para que esa variable no se tenga en cuenta porque no se va a usar
    ganador = fila[columna_1x2] #* Obtine el 1X2 de cada fila
    equipo_local = fila['LOCAL']  #* Obtiene el equipo local de cada fila
    equipo_visitante = fila['VISITANTE']  #* Obtiene el equipo visitante de cada fila

    #* Actualizar la clasificación según el resultado:
    if ganador == '1':
      clasificacion.loc[clasificacion['Equipos'] == equipo_local, 'Puntos'] += 3
      clasificacion.loc[clasificacion['Equipos'] == equipo_local, 'G'] += 1
      clasificacion.loc[clasificacion['Equipos'] == equipo_visitante, 'P'] += 1
    elif ganador == 'X':
      clasificacion.loc[clasificacion['Equipos'] == equipo_local, 'Puntos'] += 1
      clasificacion.loc[clasificacion['Equipos'] == equipo_local, 'E'] += 1
      clasificacion.loc[clasificacion['Equipos'] == equipo_visitante, 'Puntos'] += 1
      clasificacion.loc[clasificacion['Equipos'] == equipo_visitante, 'E'] += 1
    else:
      clasificacion.loc[clasificacion['Equipos'] == equipo_local, 'P'] += 1
      clasificacion.loc[clasificacion['Equipos'] == equipo_visitante, 'Puntos'] += 3
      clasificacion.loc[clasificacion['Equipos'] == equipo_visitante, 'G'] += 1

    # Actualizar el número de partidos jugados
    clasificacion.loc[clasificacion['Equipos'] == equipo_local, 'PJ'] += 1
    clasificacion.loc[clasificacion['Equipos'] == equipo_visitante, 'PJ'] += 1

  # Ordenar la clasificación por puntos de forma descendente
  clasificacion = clasificacion.sort_values('Puntos', ascending=False)
  clasificacion = clasificacion.reset_index(drop=True)
  
  return clasificacion