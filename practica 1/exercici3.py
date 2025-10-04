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
    # Suposem que existeix un camí entre l'origen i el destí i el node extra.
    # Utilitzem la funció Dijkstra amb extra com a origen i destination com a destí.
    path, cost, dist, prev = dijkstra_aux(G, extra, destination, holes_dct)
    # Construïm el subcamí que va des de l'origen fins al node extra.
    pathaux = []
    node = origin
    while node != extra:
        pathaux.append(node)
        node = prev[node]
    # Ajuntem els dos camins.
    path = pathaux + path

    # Recalculem el cost 
    cost += dist[origin]
    if extra in holes_dct:
        cost += holes_dct[extra]
        # Si l'extra no era cap dels extrems, restem 1 al cost perquè ja li hem aplicat la penalització.
        if extra != origin and extra != destination:
            cost -= 1

    return path, cost