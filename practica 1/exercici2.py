# Autors: Guillem Tubert i Jaume Tomi
import heapq
def dijkstra_aux(G, origin, destination, holes_dct={}):
    """
    Params
    ======
    :G: Graf del qual en volem extreure el camí mínim. Ha de ser un objecte de la classe nx.Graph
    :origin: Índex del node orígen
    :destination: Índex del node destí
    :holes_dct: Un diccionari del tipus {node: penalització}. Passar per cada node del diccionari té un cost diferent a 1.
    
    Returns
    =======
    :path: Una llista de nodes del camí més curt entre els nodes 'origin' i 'destination' (ambdós inclosos).
    :cost: Un enter amb el cost de recórrer el camí, incloent-hi les penalitzacions.
    :dist: Un diccionari del tipus {node: distància mínima des de l'origen}.
    :prev: Un diccionari del tipus {node: node anterior en el camí òptim}.
    """
    
    path = []
    cua_p = []
    heapq.heapify(cua_p)
    # Guardarem els nodes visitats en un conjunt per no fer més comprovacions de les necessàries.
    visited = set()

    # Inicialitzem els diccionaris de distàncies i dels nodes anteriors en el camí.
    dist = {origin: 0}
    prev = {}
    for node in G.nodes():
        if node != origin:
            dist[node] = float("inf")
        heapq.heappush(cua_p, (dist[node], node))

    # Mentre hi hagi elements a la cua seguim amb el càlcul.
    while cua_p:
        u = heapq.heappop(cua_p)
        visited.add(u[1])
        for vei in G.neighbors(u[1]):
            if vei not in visited:
                # Calculem el cost alternatiu per arribar al veí.
                alt = u[0]
                if vei in holes_dct:
                    alt += holes_dct[vei]
                else:
                    alt += 1
                # Si era millor, actualitzem i inserim a la cua prioritària (repetim elements, s'acabarà buidant la cua igualment).
                if alt < dist[vei]:
                    dist[vei] = alt
                    prev[vei] = u[1]
                    heapq.heappush(cua_p, (dist[vei], vei))
    
    cost = dist[destination]
    # Construcció del camí de cost mínim a partir de la destinació i del diccionari dels nodes anteriors en el camí.
    node_aux = prev[destination]
    path.append(destination)
    while node_aux != origin:
        path.append(node_aux)
        node_aux = prev[node_aux]
    path.append(origin)
    path = path[::-1]
    
    return path, cost, dist, prev

def holes(G, origin, destination, holes_dct={}):
    """
    Params
    ======
    :G: Graf del qual en volem extreure el camí mínim. Ha de ser un objecte de la classe nx.Graph
    :origin: Índex del node orígen
    :destination: Índex del node destí
    :holes_dct: Un diccionari del tipus {node: penalització}. Passar per cada node del diccionari té un cost diferent a 1.
    
    Returns
    =======
    :path: Una llista de nodes del camí més curt entre els nodes 'origin' i 'destination' (ambdós inclosos).
    :cost: Un enter amb el cost de recórrer el camí, incloent-hi les penalitzacions.
    """
    # Suposem que existeix un camí entre l'origen i el destí.
    # Cridem a la funció auxiliar que calcula el camí de cost mínim però retorna més informació de la que demanem.
    path, cost = dijkstra_aux(G, origin, destination, holes_dct)[0:2]
    
    return path, cost