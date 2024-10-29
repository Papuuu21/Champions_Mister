def completar_resultados(df, resultados):
    """
    Completa las columnas de resultados del DataFrame con los valores proporcionados.
    
    Args:
    df (pandas.DataFrame): DataFrame con las columnas 'RTDO L', 'RTDO V', 'RTDO L.1', 'RTDO V.1'
    resultados (dict): Diccionario con los resultados de cada jugador
    
    Returns:
    pandas.DataFrame: DataFrame con las columnas de resultados completadas
    """
    # Mapeo de jugadores a columnas y condiciones
    mapeo = {
        'Palop': ('VISITANTE', 'RTDO V'),
        'Fale': ('LOCAL', 'RTDO L'),
        'Lope': ('VISITANTE', 'RTDO V'),
        'Tony': ('LOCAL', 'RTDO L'),
        'Ruso': ('LOCAL', 'RTDO L'),
        'Kero': ('VISITANTE', 'RTDO V'),
        'Coquina': ('VISITANTE.1', 'RTDO V.1'),
        'Papu': ('LOCAL.1', 'RTDO L.1'),
        'Kike': ('VISITANTE.1', 'RTDO V.1'),
        'Gonzo': ('LOCAL.1', 'RTDO L.1'),
        'Puche': ('VISITANTE.1', 'RTDO V.1'),
        'Armada': ('LOCAL.1', 'RTDO L.1'),
    }
    
    for jugador, resultado in resultados.items():
        if jugador in mapeo:
            columna, resultado_columna = mapeo[jugador]
            df.loc[df[columna] == jugador, resultado_columna] = resultado
    
    return df

def completar_resultados2(df, resultados):
    """
    Completa las columnas de resultados del DataFrame con los valores proporcionados.
    
    Args:
    df (pandas.DataFrame): DataFrame con las columnas 'RTDO L', 'RTDO V', 'RTDO L.1', 'RTDO V.1'
    resultados (dict): Diccionario con los resultados de cada jugador
    
    Returns:
    pandas.DataFrame: DataFrame con las columnas de resultados completadas
    """
    # Mapeo de jugadores a columnas y condiciones
    mapeo = {
        'Palop': ('VISITANTE', 'RTDO V'),
        'Fale': ('LOCAL', 'RTDO L'),
        'Lope': ('VISITANTE', 'RTDO V'),
        'Tony': ('LOCAL', 'RTDO L'),
        'Ruso': ('LOCAL', 'RTDO L'),
        'Kero': ('VISITANTE', 'RTDO V'),
        'Coquina': ('VISITANTE.1', 'RTDO V.1'),
        'Papu': ('LOCAL.1', 'RTDO L.1'),
        'Kike': ('VISITANTE.1', 'RTDO V.1'),
        'Gonzo': ('LOCAL.1', 'RTDO L.1'),
        'Puche': ('VISITANTE.1', 'RTDO V.1'),
        'Armada': ('LOCAL.1', 'RTDO L.1'),
    }
    
    for jugador, resultado in resultados.items():
        if jugador in mapeo:
            columna, resultado_columna = mapeo[jugador]
            # Asegúrate de que la columna exista en el DataFrame
            if columna in df.columns and resultado_columna in df.columns:
                df.loc[df[columna] == jugador, resultado_columna] = resultado
            else:
                print(f"Columnas {columna} o {resultado_columna} no existen en el DataFrame.")
        else:
            print(f"Jugador {jugador} no encontrado en mapeo.")
    
    return df