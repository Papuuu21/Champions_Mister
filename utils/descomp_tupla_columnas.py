
import pandas as pd

def descomponer_tupla(tupla):
    return pd.Series(tupla, index=['columna1', 'columna2']) 