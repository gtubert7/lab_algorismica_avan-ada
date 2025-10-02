import itertools

def checkpoints_list(G, origin, destination, extras, holes_dct={}):
    """
    Params
    ======
    :G: Graf del qual en volem extreure el camí mínim. Ha de ser un objecte de la classe nx.Graph
    :origin: Índex del node orígen
    :destination: Índex del node destí
    :extras: Llista d'índexs de nodes per on ha de passar el camí.
    :holes_dct: Un diccionari del tipus {node: penalització}. Passar per cada node del diccionari té un cost diferent a 1.
    
    Returns
    =======
    :path: Una llista de nodes del camí més curt entre els nodes 'origin' i 'destination' que passa per tots els nodes 'extras'.
    :cost: Un enter amb el cost de recórrer el camí, incloent-hi les penalitzacions.
    """
    
    path = []
    cost = 0
    
    valors = {}

    valors[origin] = dijkstra_aux(G, origin, extras[0], holes_dct)

    for i in range(len(extras) - 1):
        valors[extras[i]] = dijkstra_aux(G, extras[i], extras[i+1], holes_dct) 
    valors[extras[-1]] = dijkstra_aux(G, extras[-1], destination, holes_dct)

   

    cost_min = float("inf")
    permutacio_min = ()
    
    for permutacio in itertools.permutations(extras):
        sum = 0
        cost = valors[origin][2][permutacio[0]]
        if origin in holes_dct:
            cost += holes_dct[origin]
        sum += cost

        for i in range(len(permutacio) - 1):
            sum += valors[permutacio[i]][2][permutacio[i+1]]
        sum += valors[permutacio[-1]][2][destination]

        if sum < cost_min:
            cost_min = sum
            permutacio_min = permutacio
    cost = cost_min
    
    path.append(origin)
    node_aux = valors[permutacio_min[0]][3][origin]
    while node_aux != permutacio_min[0]:
        path.append(node_aux)
        node_aux = valors[permutacio_min[0]][3][node_aux]

    for i in range(len(permutacio) - 1):
        path.append(permutacio_min[i])
        node_aux = valors[permutacio_min[i + 1]][3][permutacio_min[i]]
        while node_aux != permutacio_min[i + 1]:
            path.append(node_aux)
            node_aux = valors[permutacio_min[i + 1]][3][node_aux]

    path_aux = [destination]

    node_aux = valors[permutacio_min[-1]][3][destination]
    while node_aux != permutacio_min[-1]:
        path_aux.append(node_aux)
        node_aux = valors[permutacio_min[-1]][3][node_aux]
    
    path_aux.append(permutacio_min[-1])

    path.extend(path_aux[::-1])

    return path, cost