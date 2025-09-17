import random as rd

posiciones_jugadores = ['1GA', '2GA', '3GA', '4GA', '1GB', '2GB', '3GB', '4GB']

lado_cuadro = ['1A', '2A', '3A', '4A', '1B', '2B', '3B', '4B']

emparejamientos = {}
rd.shuffle(lado_cuadro)
valores_unicos = rd.sample(posiciones_jugadores, len(lado_cuadro))
for lado, valor in zip(lado_cuadro, valores_unicos):
    emparejamientos[lado] = valor
print(emparejamientos)

