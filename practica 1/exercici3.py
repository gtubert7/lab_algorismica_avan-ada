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
    path = []
    cost = 0
    
    path_primer, cost_primer = holes(G, origin, extra, holes_dct)
    path_segon, cost_segon = holes (G, extra, destination, holes_dct)

    path = path_primer + path_segon
    cost = cost_primer + cost_segon
    
    return path, cost