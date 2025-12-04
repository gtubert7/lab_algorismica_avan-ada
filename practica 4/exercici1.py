###
# LES VOSTRES FUNCIONS EXTRES AQUÍ
###

def satisfies(grid, x, y, num, top, bottom, left, right):
    """
    Donat un tauler, un punt amb coordenades (x,y) i un nombre 'num', comprova si és possible assignar-lo a la posició (x,y) 
    donades les restriccions del problema.
    
    Params
    ------
    :grid: Una matriu de numpy
    :x,y: Un punt de la matriu on volem posar el nombre 'num'
    :num: Un nombre enter
    :top, bottom, left, right: Els nombres de fora del tauler de la part superior, inferior, esquerra i dreta, respectivament.
    
    Returns
    -------
    :b: Un boleà True/False depenent de si el nombre 'num' pot ser col·locat a la casella (x,y) o no.
    """
    
    # EL TEU CODI AQUÍ

    # Comprovació fila i columna
    if num in grid[x] or num in grid[:, y]:
        return False
    
    # Comprovació top 
    max = 0
    num_visibles = 0
    for i in range(len(top)):
        if grid[i, y] > max:
            max = grid[i, y]
            num_visibles += 1
            if num_visibles > top[y]:
                return False
    # Comprovació bottom
    max = 0
    num_visibles = 0
    for i in range(len(bottom) - 1, -1, -1):
        if grid[i, y] > max:
            max = grid[i, y]
            num_visibles += 1
            if num_visibles > bottom[y]:
                return False
    # Comprovació left
    max = 0
    num_visibles = 0
    for j in range(len(left)):
        if grid[x, j] > max:
            max = grid[i, y]
            num_visibles += 1
            if num_visibles > left[x]:
                return False
    # Comprovació right
    max = 0
    num_visibles = 0
    for j in range(len(right) - 1, -1, -1):
        if grid[x, j] > max:
            max = grid[i, y]
            num_visibles += 1
            if num_visibles > right[x]:
                return False
    
    return True
    

def skyscrapper_backtracking(grid, top, bottom, left, right):  
    """
    Funció que implementa l'algorisme de backtracking
    
    Params
    ------
    :grid: Una matriu de tipus numpy
    :top, bottom, left, right: Els nombres de fora del tauler de la part superior, inferior, esquerra i dreta, respectivament.
    
    Returns
    -------
    :grid: La matriu plena amb la solució correcta o bé False en cas que no tingui solució.    
    """
    
    # NO esborreu aquestes dues línies, serveien per saber quants cops es crida aquesta funció
    # ----------------------------------------------------------------------------------------
    global num_recursive_calls 
    num_recursive_calls += 1
    # ----------------------------------------------------------------------------------------
    
    # EL TEU CODI AQUÍ
    if not (grid == 0).any():
        return grid
    llista_x, llista_y = np.where(grid == 0)
    # TODO: canviar política
    x = llista_x[0]
    y = llista_y[0]
    # TODO: canviar política
    for num in [i for i in range(1, len(grid) + 1)]:
        if satisfies(grid, x, y, num, top, bottom, left, right):
            grid[x, y] = num
            ok = skyscrapper_backtracking(grid, top, bottom, left, right)
            if ok:
                return ok
    
    return False
    
def skyscrapper(top, bottom, left, right):
    """
    Funció principal del problema. Rep quatre llistes corresponents als nombres que hi ha fora del tauler.
    
    Params
    ------
    :top, bottom, left, right: Els nombres de fora del tauler de la part superior, inferior, esquerra i dreta, respectivament.
    """
    
    # Inicialitzem una matriu de zeros
    grid = np.zeros((len(left), len(top)), dtype='int')
    
    # Cridem a la funció que soluciona el problema mitjançant backtracking
    sol = skyscrapper_backtracking(grid, top, bottom, left, right)   
    
    # Mostrem el resultat en el cas que trobem una solució o mostrem un error en cas contrari.
    if sol:
        print(format_sky(np.array(sol), top, bottom, left, right))
    else:
        print('No solution found')