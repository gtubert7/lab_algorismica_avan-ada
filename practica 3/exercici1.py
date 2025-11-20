def superior_neighbors(mat, point):
    """
    Donada una matriu de mida H x W i punt, retorna els punts de la fila superior adjacents al punt passat com a paràmetre.
    Cal tenir en compte els següents casos. Considerant que el punt té coordenades (i,j):
        - Si el punt té coordenada j=0, vol dir que estem agafant un punt del marge esquerre de la imatge. Només s'han de retornar DOS veïns.
        - Si el punt té coordenada j=(W-1), vol dir que estem agafant un punt del marge dret de la imatge. Només s'han de retornar DOS veïns.
        - En la resta de casos, es retornen els tres veïns superiors.
        
    Params
    ======
    :mat: Una matriu 2-Dimensional
    :point: Un sol punt amb el format (i,j)
    
    Returns
    =======
    :neighbors: Una llista de dos o tres elements en funció de cada cas.
    """
    
    neighbors = np.array([])
    
    # EL TEU CODI AQUÍ
    '''
    if point[0] == 0:
        return neighbors
    
    neighbors[0] = point[0] -1

    if point[1] == 0:
        neighbors[1]
    '''

    return mat[point[0] - 1, point[1] - 1:point[1] + 2]
    return neighbors


def minimal_paths(mat):
    """
    Creació de tots els camins mínims usant programació dinàmica.
    Cal usar la funció 'superior_neighbors' per trobar els veïns.
    
    Params
    ======
    :mat: Matriu 2-Dimensional d'entrada (gradient)
    
    Returns
    =======
    :ret: Matriu 2-Dimensional de la mateixa mida que 'mat' amb els camins mínims calculats.
    """
    
    ret = mat.copy()
    
    # EL TEU CODI AQUÍ
    for fila in ret[1:]:
        for item in fila:
            veins = superior_neighbors(item)
            item = min([item + vei for vei in veins])

    return ret
