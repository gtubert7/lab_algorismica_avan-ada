from matplotlib import pyplot as plt
import networkx as nx
from maze import *

#Exercici 1

def bfs(G, origin):
    """
    Params
    ======    
    :G: Graf. Ha de ser un objecte de la classe nx.Graph
    :origin: Índex del node orígen
    
    Returns
    =======
    :visited: El conjunt de nodes visitats durant l'exploració BFS en l'ordre en que han estat explorats
    """
    visited = []
    visited_set = set()    

    bfs_aux(G, origin, visited, visited_set)

    return visited

def bfs_aux(G, node, visited, visited_set):
    if node not in visited_set:
        visited.append(node)
        visited_set.add(node)

        for neigh in node.neighbors:
            bfs_aux(G, node, visited, visited_set)