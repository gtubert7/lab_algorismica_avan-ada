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
    N = 50

    im_titles = [(im, 'Imatge original'), (get_gradient(im), "Gradient")]
    mat = minimal_paths(get_gradient(im), patch)
    mat[patch[0][0]:patch[1][0], patch[0][1]:patch[1][1]]
    path = find_min_path(mat)
    im_path = im.copy()
    im_path = add_min_path(im_path, path)
    im_titles.append((im_path, 'Primer camí a eliminar'))
    im = delete_path(im, path)
    for _ in range(N - 1):
        mat = minimal_paths(get_gradient(im), patch)
        mat[patch[0][0]:patch[1][0], patch[0][1]:patch[1][1]]
        path = find_min_path(mat)
        im = delete_path(im, path)
    im_titles.append((im, 'Imatge final'))
    show_row(im_titles)

    pass

def minimal_paths(mat, patch):
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
    for i in range(1, len(ret)):
        for j in range(len(ret[i])):
            if patch[0][0] < i < patch[1][0] and patch[0][1] < j < patch[1][1]:
                ret[i, j] = -1
            else:
                ret[i, j] += min(superior_neighbors(ret, (i, j)))

    return ret