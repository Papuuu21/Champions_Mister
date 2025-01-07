import pandas as pd
from utils.pts_equipos import pts_equipos


clasificados = [[0, '4ºGB', '1ºGB', 0, '||', 0, '3ºGB', '1ºGA', 0], [0, '2ºGB', '2ºGA', 0, '||', 0, '3ºGA', '4ºGA', 0]]

columnas = ['PTOS LA', 'LOCAL A', 'VISITANTE A', 'PTOS VA', '||', 'PTOS LB', 'LOCAL B',  'VISITANTE B', 'PTOS VB']
cuartos = pd.DataFrame(data= clasificados, index=[1,2], columns=columnas)
print(cuartos)

 #!Rtdos Jornada actualizados: BORRAR A LOS JUGADORES ELIMINADOS
palop, fale, tony, lope, ruso, coquina, papu, kike, gonzo, puche, kero, armada = pts_equipos()
resultados = {
    'Lope': lope, 'Palop': palop, 'Fale': fale, 'Kero': kero, 'Ruso': ruso, 'Tony': tony,
    'Puche': puche, 'Coquina': coquina, 'Kike': kike, 'Armada': armada, 'Papu': papu, 'Gonzo': gonzo
}

print(resultados)
