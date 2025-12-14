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
    
    grid[x, y] = num
    # Comprovació top
    if 1 < top[y] < len(grid):
        # Comprovacio rara
        if top[y] + num - len(grid) > x + 1:
            grid[x, y] = 0
            return False
        max = 0
        num_visibles = 0
        zeros_entremig = 0
        zeros_acum = 0
        for i in range(len(top)):
            if grid[i, y] == 0:
                zeros_acum += 1
            else:
                zeros_entremig += zeros_acum
                zeros_acum = 0
            if grid[i, y] > max:
                max = grid[i, y]
                num_visibles += 1
                if num_visibles > top[y]:
                    grid[x, y] = 0
                    return False
        if len(grid) - max + zeros_entremig < top[y] - num_visibles:
            grid[x, y] = 0
            return False
    # Comprovació bottom
    if 1 < bottom[y] < len(grid):
        if len(grid) - (bottom[y] + num - len(grid)) < x:
            grid[x, y] = 0
            return False
        max = 0
        num_visibles = 0
        zeros_entremig = 0
        zeros_acum = 0
        for i in range(len(bottom) - 1, -1, -1):
            if grid[i, y] == 0:
                zeros_acum += 1
            else:
                zeros_entremig += zeros_acum
                zeros_acum = 0
            if grid[i, y] > max:
                max = grid[i, y]
                num_visibles += 1
                if num_visibles > bottom[y] and x == len(grid) - 1:
                    grid[x, y] = 0
                    return False
        if len(grid) - max + zeros_entremig < bottom[y] - num_visibles:
            grid[x, y] = 0
            return False
    # Comprovació left
    if 1 < left[x] < len(grid):
        if left[x] + num - len(grid) > y + 1:
            grid[x, y] = 0
            return False
        max = 0
        num_visibles = 0
        zeros_entremig = 0
        zeros_acum = 0
        for j in range(len(left)):
            if grid[x, j] == 0:
                zeros_acum += 1
            else:
                zeros_entremig += zeros_acum
                zeros_acum = 0
            if grid[x, j] > max:
                max = grid[x, j]
                num_visibles += 1
                if num_visibles > left[x]:
                    grid[x, y] = 0
                    return False
        if len(grid) - max + zeros_entremig < left[x] - num_visibles:
            grid[x, y] = 0
            return False
    # Comprovació right
    if 1 < right[x] < len(grid):
        if len(grid) - (right[x] + num - len(grid)) < y:
            grid[x, y] = 0
            return False
        max = 0
        num_visibles = 0
        zeros_entremig = 0
        zeros_acum = 0
        for j in range(len(right) - 1, -1, -1):
            if grid[x, j] == 0:
                zeros_acum += 1
            else:
                zeros_entremig += zeros_acum
                zeros_acum = 0
            if grid[x, j] > max:
                max = grid[x, j]
                num_visibles += 1
                if num_visibles > right[x] and y == len(grid) - 1:
                    grid[x, y] = 0
                    return False
        if len(grid) - max + zeros_entremig < right[x] - num_visibles:
            grid[x, y] = 0
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
        return list(grid)
    llista_x, llista_y = np.where(grid == 0)
    # TODO: canviar política
    x = llista_x[0]
    y = llista_y[0]
    # TODO: canviar política
    for num in range(1, len(grid) + 1):
        if satisfies(grid, x, y, num, top, bottom, left, right):
            # L'operació grid[x, y] = num es fa a satisfies() si se satisfan les condicions.
            ok = skyscrapper_backtracking(grid, top, bottom, left, right)
            if ok:
                return ok
            grid[x, y] = 0
    
    return False

def preinicialitza(grid, top, bottom, left, right):
    # Comprovem top
    for j in range(len(top)):
        if top[j] == 1:
            if grid[0, j] == 0:
                if not satisfies(grid, 0, j, len(grid), top, bottom, left, right):
                    return False
            elif grid[0, j] != len(grid):
                return False
        elif top[j] == len(grid):
            for k in range(len(grid)):
                if grid[k, j] == 0:
                    if not satisfies(grid, k, j, k + 1, top, bottom, left, right):
                        return False
                elif grid[k, j] != k + 1:
                    return False
    # Comprovem bottom
    for j in range(len(bottom)):
        if bottom[j] == 1:
            if grid[len(grid) - 1, j] == 0:
                if not satisfies(grid, len(grid) - 1, j, len(grid), top, bottom, left, right):
                    return False
            elif grid[len(grid) - 1, j] != len(grid):
                return False
        elif bottom[j] == len(grid):
            for k in range(len(grid)):
                if grid[k, j] == 0:
                    if not satisfies(grid, k, j, len(grid) - k, top, bottom, left, right):
                        return False
                elif grid[k, j] != len(grid) - k:
                    return False
    # Comprovem left
    for i in range(len(left)):
        if left[i] == 1:
            if grid[i, 0] == 0:
                if not satisfies(grid, i, 0, len(grid), top, bottom, left, right):
                    return False
            elif grid[i, 0] != len(grid):
                return False
        elif left[i] == len(grid):
            for k in range(len(grid)):
                if grid[i, k] == 0:
                    if not satisfies(grid, i, k, k + 1, top, bottom, left, right):
                        return False
                elif grid[i, k] != k + 1:
                    return False
    # Comprovem right
    for i in range(len(right)):
        if right[i] == 1:
            if grid[i, len(grid) - 1] == 0:
                if not satisfies(grid, i, len(grid) - 1, len(grid), top, bottom, left, right):
                    return False
            elif grid[i, len(grid) - 1] != len(grid):
                return False
        elif right[i] == len(grid):
            for k in range(len(grid)):
                if grid[i, k] == 0:
                    if not satisfies(grid, i, k, len(grid) - k, top, bottom, left, right):
                        return False
                elif grid[i, k] != len(grid) - k:
                    return False
    return True

def skyscrapper(top, bottom, left, right):
    """
    Funció principal del problema. Rep quatre llistes corresponents als nombres que hi ha fora del tauler.
    
    Params
    ------
    :top, bottom, left, right: Els nombres de fora del tauler de la part superior, inferior, esquerra i dreta, respectivament.
    """
    
    # Inicialitzem una matriu de zeros
    grid = np.zeros((len(left), len(top)), dtype='int')

    # Codi afegit: preinicialització
    if not preinicialitza(grid, top, bottom, left, right):
        print('No solution found')
        return
    
    # Cridem a la funció que soluciona el problema mitjançant backtracking
    sol = skyscrapper_backtracking(grid, top, bottom, left, right)   
    
    # Mostrem el resultat en el cas que trobem una solució o mostrem un error en cas contrari.
    if sol:
        print(format_sky(np.array(sol), top, bottom, left, right))
    else:
        print('No solution found')