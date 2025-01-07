import pandas as pd
from utils.pts_equipos import pts_equipos


clasificados = [[0, 'ARMADA', 'PAPU', 0, '||', 0, 'PUCHE', 'KERO', 0], [0, 'GONZO', 'PALOP', 0, '||', 0, 'LOPE', 'RUSO', 0]]

columnas = ['PTOS LA', 'LOCAL A', 'VISITANTE A', 'PTOS VA', '||', 'PTOS LB', 'LOCAL B',  'VISITANTE B', 'PTOS VB']
cuartos = pd.DataFrame(data= clasificados, index=[1,2], columns=columnas)
print(cuartos)

