


def ver_1x2(df):
    #* Comparando los resultados y asiganamos en formato quiniela quien gana a la col 1X2:
    if df.loc[0, 'RTDO L'] > df.loc[0, 'RTDO V']:
        df['1X2'] = 1
    elif df.loc[0, 'RTDO L'] < df.loc[0, 'RTDO V']:
        df['1X2'] = 2
    else:
        df['1X2'] = 'X'

    return df