
def comparar_max_pts(clasificacion_anterior, pts_jor):

    clasificacion_anterior['Pts.Jorn'] = pts_jor
    if (clasificacion_anterior['Pts.Jorn'] >= clasificacion_anterior['Max.pts']).all():
        clasificacion_anterior['Max.pts'] = pts_jor

    return clasificacion_anterior