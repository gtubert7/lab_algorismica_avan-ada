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
    #Formem la llista on anirem afegint els nodes accessibles
    visited = [origin]
    #Formem un conjunt per a poder saber a quins nodes hem accedit amb cost O(1)
    visited_set = set()
    visited_set.add(origin)
    
    i = 0
    #Afegim a la llista els nodes a mesura que els trobem. Els visitem també a mesura que els trobem (per aixó anem incrementant i)
    while i < len(visited):
        for neigh in G.neighbors(visited[i]):
            if neigh not in visited_set:
                visited.append(neigh)
                visited_set.add(neigh)
        i+= 1

    return visited