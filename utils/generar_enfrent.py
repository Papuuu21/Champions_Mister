

def generar_enfrentamientos(grupo):
    num_jugadores = len(grupo)
    
    if num_jugadores % 2 != 0:
        grupo.append('Descanso')  #* Añadir un descanso si el número de jugadores es impar

    num_jornadas = len(grupo) - 1
    mitad = num_jugadores // 2
    
    ida = []

    for i in range(num_jornadas): #* Cuando recorres indices no tienes porque usar ese indice
        jornada = []
        for j in range(mitad):
            jugador1 = grupo[j]
            jugador2 = grupo[num_jugadores - j - 1]
            jornada.append((jugador1, jugador2))
        
        ida.append(jornada)
        
        #* Rotar los jugadores (excepto el primero)
        grupo.insert(1, grupo.pop())
    
    return ida
