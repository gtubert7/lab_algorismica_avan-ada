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
    # EL TEU CODI AQUÍ
    if point[1] == 0:
        if point[1] == (mat.shape)[1] - 1:
            return mat[point[0] - 1, point[1]]
        else:
            return mat[point[0] - 1, point[1]:point[1] + 2]
    else:
        if point[1] == (mat.shape)[1] - 1:
            return mat[point[0] - 1, point[1] - 1:point[1] + 1]
        else:
            return mat[point[0] - 1, point[1] - 1:point[1] + 2]

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
    for i in range(1, len(ret)):
        for j in range(len(ret[i])):
            ret[i, j] += min(superior_neighbors(ret, (i, j)))

    return ret


def find_min_path(mat):
    """
    Donada una matriu, calcula el camí mínim sobre aquesta. L'algorisme ha de començar per la part inferior i buscar el següents punts.
    
    Params
    ======
    :mat: Matriu de camins mínims
    
    Returns
    =======
    :min_path: Una llista de tuples amb les coordenades (i,j) del camí mínim. La primera coordenada ha d'anar decrementant sempre en 1.
               Exemple. Suposant que una imatge té d'alçada 341 píxels, un possible camí seria: [(340, 120), (339, 121), (338,120), ..., (0, 151)] 
    """
    
    # EL TEU CODI AQUÍ
    dim = mat.shape
    i = dim[0] - 1
    j = np.argmin((mat[i]))
    min_path = [(i, j)]
    while i > 0:
        veins = superior_neighbors(mat, (i, j))
        if j > 0:
            min_path.append((i - 1, j - 1 + np.argmin(veins)))
            j = j - 1 + np.argmin(veins)
        else:
            min_path.append((i - 1, np.argmin(veins)))
            j = np.argmin(veins)
        i -= 1
    
    return min_path



def delete_path(im, path):
    """
    Donat una imatge i un camí, elimina els pixels de la imatge que pertanyen del camí.
    Podeu usar la següent instrucció per inicialitzar la imatge. Això crea una imatge amb tots els valors a zero.
    
    im_new = np.zeros((im.shape[0], im.shape[1]-1, im.shape[2]))
    
    Params
    ======
    :im: Una imatge de mida H x W x 3
    :path: Un camí sobre la imatge. 
    
    Returns
    =======
    :im_new: Una nova imatge de mida H x (W-1) x 3 amb el camí eliminat
    """
    
    im_new = np.zeros((im.shape[0], im.shape[1]-1, im.shape[2]))
    
    # EL TEU CODI AQUÍ
    for i, j in path:
        im_new[i, 0:j, :] = im[i, 0:j, :]
        im_new[i, j:, :] = im[i, (j + 1):, :]
    
    return im_new


def reduce_image(im, N=100):    
    """
    Implementació de l'algorisme Seam Carving. 
    Useu la funció 'show_row' al finalitzar per mostrar una figura amb tres subfigures:
        - Imatge original
        - Primer camí que s'elimina
        - Imatge resultant després de N iteracions
    
    Params
    ======
    :im: Imatge que volem reduir
    :N: Nombre de cops que repetirem l'algorisme
    """
    
    # EL TEU CODI AQUÍ
    im_titles = [(im, 'Imatge original')]
    mat = minimal_paths(get_gradient(im))
    path = find_min_path(mat)
    im_path = im.copy()
    im_path = add_min_path(im_path, path)
    im_titles.append((im_path, 'Primer camí a eliminar'))
    im = delete_path(im, path)
    for _ in range(N - 1):
        mat = minimal_paths(get_gradient(im))
        path = find_min_path(mat)
        im = delete_path(im, path)
    im_titles.append((im, 'Imatge final'))
    show_row(im_titles)