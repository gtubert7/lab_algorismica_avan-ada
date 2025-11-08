from collections import defaultdict

def compute_frequency(text):
    """
    Params
    ======
    :text: El text que volem codificar
    
    Returns
    =======
    :dct: Un diccionari amb el nombre de cops que apareix cada simbol en el text d'entrada. Per exemple: {'A': 3, 'B': 2, 'C': 1}
    """
    dct = {}
    
    for letter in text:
        if letter in dct:
            dct[letter] += 1
        else:
            dct[letter] = 1

    return dct


def assign_codes(text, counts):   
    """
    Aquesta funció construeix el diccionari de conversió de lletres a símbols '.' i '-'.
    
    Params
    ======
    :text: El text que volem convertir
    :counts: El diccionari de freqüències que ens retorna la funció compute_frequency
    
    Returns
    =======
    :codes: El diccionari de conversió. Per exemple: {'C': '--', 'B': '-.', 'A': '.'}
    """
    
    codes = {}

    nodes_list = []

    #Afegim els nodes a la llista
    for key in counts.keys():
        node = Node(key, counts[key])
        nodes_list.append((counts[key], node))
  
    while len(nodes_list) >= 2:
        #POTSER CAL MIRAR COM TROBEM EL MINIM ELEMENT
        node_esq = nodes_list.pop(nodes_list.index(min(nodes_list, key = lambda node: node[0])))[1]
        node_dreta = nodes_list.pop(nodes_list.index(min(nodes_list, key = lambda node: node[0])))[1]

        #Fem el node pare
        suma = node_esq.value + node_dreta.value
        node_suma = Node(suma, suma, node_esq, node_dreta)

        node_esq.set_code("-")
        node_dreta.set_code(".")

        nodes_list.append((suma, node_suma))

    #Fem un dfs per l'arbre amb la intencio de assignar un codi a cada lletra
    dfs_aux(max(nodes_list, key = lambda node: node[0])[1], counts, codes)

    return codes

def dfs_aux(node, counts, codes, codi = ""):
    if node == None:
        return

    if node.node in counts:
        codes[node.node] = codi

    dfs_aux(node.left, counts, codes, codi + "-")
    dfs_aux(node.right, counts, codes, codi + ".")