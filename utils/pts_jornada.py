def pts_por_jornada(df1, num_grupo = 1):
    #* Copiamos el DF de los partidos a uno llamado rtdos_jor1 para añadirle los puntos de cada equipo
    rtdos_gr = df1
    
    if num_grupo == 1:

        #* SEPARAMOS POR LOCAL Y VISITANTE PARA CREAR UNA LISTA DE LOS RSTDOS POR AMBOS TIPOS:
        #* Locales:
        ruso = int(input('Pts Jornada 1 Ruso: '))
        coquina = int(input('Pts Jornada 1 Coquina: '))
        papu = int(input('Pts Jornada 1 Papu: '))
        pts_local_gr1 = [ruso, coquina, papu]
        rtdos_gr['RTDO L'] = pts_local_gr1 #* Añadimos los puntos de cada local

        #* Visitantes:
        kike = int(input('Pts Jornada 1 Kike: '))
        gonzo = int(input('Pts Jornada 1 Gonzo: '))
        fale = int(input('Pts Jornada 1 Fale: '))
        pts_visitante_gr1 = [kike, gonzo, fale]
        rtdos_gr['RTDO V'] = pts_visitante_gr1 #* Añadimos los puntos de cada visitante

        #* Hacemos una lista con los puntos de la jornada para usarla en la comparación de max. pts
        pts_jornada_gr = [ruso, coquina, papu, fale, gonzo, kike] #* En orden que vayan en la clasificación
    else:
        #* Locales:
        tony = int(input('Pts Jornada 1 Tony: '))
        palop = int(input('Pts Jornada 1 Palop: '))
        lope = int(input('Pts Jornada 1 Lope: '))
        pts_local_gr2 = [tony, palop, lope]
        rtdos_gr['RTDO L'] = pts_local_gr2 #* Añadimos los puntos de cada local


        #* Visitantes:
        diego = int(input('Pts Jornada 1 Diego: '))
        kero = int(input('Pts Jornada 1 kero: '))
        armada = int(input('Pts Jornada 1 Armada: '))
        pts_visitante_gr2 = [diego, kero, armada]
        rtdos_gr['RTDO V'] = pts_visitante_gr2 #* Añadimos los puntos de cada visitante

        #* Hacemos una lista con los puntos de la jornada para usarla en la comparación de max. pts
        pts_jornada_gr = [tony, palop, lope, diego, kero, armada] #* En orden que vayan en la clasificación

    return rtdos_gr, pts_jornada_gr