

def partidos_str(g1):
    #* Conversión de las tuplas a str de los enfrentamientos:
    partidos_str = []
    for x in g1:
        partido = x[0], 'vs', x[1]
        partido = f'{x[0]} VS {x[1]}'
        partidos_str.append(partido)

    return partidos_str