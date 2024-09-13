
from utils.invertir_tuplas import invertir_tupla


def vuelta_gr(ida):
    #* Reordenar cada tupla en cada lista
    listas_reordenadas = [
        [invertir_tupla(tupla) for tupla in lista]
        for lista in ida
    ]
    return listas_reordenadas