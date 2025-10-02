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
    """
    
    path = []
    cua_p = []
    heapq.heapify(cua_p)
    visited = set()

    dist = {origin: 0}

    prev = {}
    for node in G.nodes():
        if node != origin:
            dist[node] = float("inf")
        heapq.heappush(cua_p, (dist[node], node))

    
    while cua_p:
        u = heapq.heappop(cua_p)
        visited.add(u[1])
        for vei in G.neighbors(u[1]):
            if vei not in visited:
                alt = u[0]
                if vei in holes_dct:
                    alt += holes_dct[vei]
                else:
                    alt += 1
                if alt < dist[vei]:
                    dist[vei] = alt
                    prev[vei] = u[1]
                    heapq.heappush(cua_p, (dist[vei], vei))
    
    cost = dist[destination]
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
    
    path, cost = dijkstra_aux(G, origin, destination, holes_dct)[0:2]
    
    return path, cost
