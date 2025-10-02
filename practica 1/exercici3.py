#Authors: Jaume Tomi, Guillem Tubert

#Exercici 3

def checkpoint(G, origin, destination, extra, holes_dct={}):
    """
    Params
    ======
    :G: Graf del qual en volem extreure el camí mínim. Ha de ser un objecte de la classe nx.Graph
    :origin: Índex del node orígen
    :destination: Índex del node destí
    :extra: Índex d'un node extra per on ha de passar el camí
    :holes_dct: Un diccionari del tipus {node: penalització}. Passar per cada node del diccionari té un cost diferent a 1.
    
    Returns
    =======
    :path: Una llista de nodes del camí més curt entre els nodes 'origin' i 'destination' que passa per 'extra'.
    :cost: Un enter amb el cost de recórrer el camí, incloent-hi les penalitzacions.
    """
    path, cost, dist, prev = dijkstra_aux(G, extra, destination, holes_dct)
    pathaux = []
    node = origin

    while node != extra:
        pathaux.append(node)
        node = prev[node]

    path = pathaux + path

    cost += dist[origin]
    if extra in holes_dct and extra != destination:
        cost += holes_dct[extra]
        if extra != origin:
            cost -= 1

    return path, cost