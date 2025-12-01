def add_patch(im, patch):
    """
    Donada una imatge i un patch. Mostra la imatge amb el patch d'un color donat. Per defecte, vermell.
    
    Params
    ======
    :im: La imatge a la que volem afegit el patch
    :patch: Patch amb quatre coordenades. Format: [(i1,j1), (i2, j2)]
    
    Returns
    =======
    :im: Imatge amb els píxels del patch en vermell.
    """
    
    for i in range(patch[0][0], patch[1][0]+1):
        for j in range(patch[0][1], patch[1][1]+1):
            im[i][j] = [1,0,0]
    return im

def inferior_neighbors(mat, point):
    """
    Donada una matriu de mida H x W i punt, retorna els punts de la fila inferior adjacents al punt passat com a paràmetre.
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
    # EL TEU CODI AQUÍ
    if point[1] == 0:
        if point[1] == (mat.shape)[1] - 1:
            return mat[point[0] + 1, point[1]]
        else:
            return mat[point[0] + 1, point[1]:point[1] + 2]
    else:
        if point[1] == (mat.shape)[1] - 1:
            return mat[point[0] + 1, point[1] - 1:point[1] + 1]
        else:
            return mat[point[0] + 1, point[1] - 1:point[1] + 2]

def minimal_paths_alt(mat, a, b, sup = True):
    """
    Creació de tots els camins mínims usant programació dinàmica.
    Usa 'superior_neighbors' o 'inferior_neighbors' per trobar els veïns.
    Força que el camí mínim passi sempre pel patch.
    
    Params
    ======
    :mat: Matriu 2-Dimensional d'entrada (gradient) corresponent a una submatriu inferior o superior al patch
    :a: Extrem esquerre del patch
    :b: Extrem dret del patch
    :sup: És True si estem calculant els camins de la subimatge superior al patch
    
    Returns
    =======
    :ret: Matriu 2-Dimensional de la mateixa mida que 'mat' amb els camins mínims calculats.
    """
    
    # EL TEU CODI AQUÍ
    mida = mat.shape
    ret = np.full((mida[0], mida[1]), np.inf)

    if sup:
        for j in range(a - 1, b + 1):
            if 0 <= j < mida[1]:
                ret[mida[0] - 1, j] = mat[mida[0] - 1, j]
        for i in range(mida[0] - 2, -1, -1):
            start = max(0, a - 1 - (mida[0] - 1 - i))
            stop = min(mida[1], b + 1 + (mida[0] - 1 - i))
            for j in range(start, stop):
                ret[i, j] += min(inferior_neighbors(ret, (i, j)))
    else:
        for j in range(a - 1, b + 1):
            if 0 <= j < mida[1]:
                ret[0, j] = mat[0, j]
        for i in range(1, mida[0]):
            start = max(0, a - 1 - i)
            stop = min(mida[1], b + 1 + i)
            for j in range(start, stop):
                ret[i, j] += min(superior_neighbors(ret, (i, j)))

    return ret

def find_min_path_alt(mat, sup = True):
    """
    Donada una matriu, calcula el camí mínim sobre aquesta.
    
    Params
    ======
    :mat: Matriu de camins mínims de la subimatge superior o inferior al patch
    :sup: És True si estem calculant els camins de la subimatge superior al patch
    Returns
    =======
    :min_path: Una llista de tuples amb les coordenades (i,j) del camí mínim.
    """
    if sup:
        dim = mat.shape
        i = 0
        j = np.argmin((mat[i]))
        min_path = [(i, j)]
        while i < dim[0] - 1:
            veins = inferior_neighbors(mat, (i, j))
            if j > 0:
                min_path.append((i + 1, j - 1 + np.argmin(veins)))
                j = j - 1 + np.argmin(veins)
            else:
                min_path.append((i + 1, np.argmin(veins)))
                j = np.argmin(veins)
            i += 1
        return min_path
    else:
        return find_min_path(mat)

def remove_patch(im, patch):
    """
    Donada una imatge i un patch, n'elimina tots els punts interiors al patch.
    Useu la funció 'show_row' al finalitzar per mostrar una figura amb tres subfigures:
        - Imatge original
        - Imatge amb el patch de color vermell
        - Imatge resultant després d'eliminar el patch
    
    Params
    ======
    :im: Imatge original
    :patch: Patch amb dos parells de coordenades. 
            Format: [(i1,j1), (i2, j2)]. Sempre se satisfà que i1<i2, j1<j2.
            (i1, j1) és la coordenada superior esquerra del patch
            (i2, j2) és la coordenada inferior dreta del patch.
            Aquestes dues parelles s'han d'incloure com a part del patch.
    """
    
    # EL TEU CODI AQUÍ
    im_titles = [(im, 'Imatge original')]
    im_patch = add_patch(im.copy(), patch)
    im_titles.append((im_patch, 'Imatge amb el patch'))
    # Extrems laterals del patch
    a = patch[0][1]
    b = patch[1][1]
    # Ja esborrem el patch
    im3 = np.delete(im_patch[patch[0][0]:patch[1][0] + 1], np.s_[a:b + 1], axis = 1)
    # Subimatge superior al patch
    im1 = im_patch[0:patch[0][0]]
    # Subimatge inferior al patch
    im2 = im_patch[patch[1][0] + 1:]
    num_iter = b - a + 1
    for _ in range(num_iter):
        # Calculem per separat els camins mínims de cada subimatge
        mat1 = minimal_paths_alt(get_gradient(im1), a, b, True)
        mat2 = minimal_paths_alt(get_gradient(im2), a, b, False)
        path1 = find_min_path_alt(mat1, True)
        path2 = find_min_path_alt(mat2, False)
        im1 = delete_path(im1, path1)
        im2 = delete_path(im2, path2)
        b -= 1
    # Apilem les tres imatges
    im_final = np.vstack([im1, im3, im2])
    im_titles.append((im_final, 'Imatge final'))
    show_row(im_titles)