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
    
    #Revisem cada lletra de text
    for letter in text:
        #Si ja la hem trobat abans, sumem 1 a la seva frequencia
        if letter in dct:
            dct[letter] += 1
        #Si encara no l'haviem trobat, l'afegim al diccionari amb frequencia 1
        else:
            dct[letter] = 1

    return dct


import heapq

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
    #Fem un heap per a poder extreure l'element minim amb major facilitat
    heapq.heapify(nodes_list)
    #Afegim cada grup (freq, lletra, node) a la llista de nodes
    for key in counts.keys():
        node = Node(key, counts[key])
        heapq.heappush(nodes_list, (counts[key], key, node))

    while len(nodes_list) >= 2:
        #Extraiem els nodes mes petits i els assignem a la dreta i l'esquerra
        node_esq = heapq.heappop(nodes_list)[2]
        node_dreta = heapq.heappop(nodes_list)[2]

        #Fem el seu node suma, assignant-li nodes fills
        suma = node_esq.value + node_dreta.value
        nom_suma = node_esq.node + node_dreta.node
        node_suma = Node(nom_suma, suma, node_esq, node_dreta)

        #Afegim el node de la suma a la llista
        heapq.heappush(nodes_list, (suma, nom_suma, node_suma))
    
    #Fem una exploracio de profunditat per donar a cada lletra el seu codi
    dfs_aux(nodes_list[0][2], counts, codes)

    return codes


def dfs_aux(node, counts, codes, codi = ""):
    '''
    Aquesta funció assigna una cadena de "-" i "." als elements d'un arbre i modifica el parametre codes per omplir-lo amb les equivalencies de codi.

    Params
    ======
    :node: Node pare de l'arbre
    :counts: El diccionari de freqüències que ens retorna la funció compute_frequency    
    :codes: El diccionari de conversió de caracters a cadenes de "-" i "."
    :codi: Cadena de "-" i "." que variara per cada node 
    '''
    #Condicio de parada
    if node == None:
        return

    #Si aquest node representa una lletra (i no una suma de frequencies de lletres)
    if node.node in counts:
        #Afegim el codi al diccionari
        codes[node.node] = codi

    #Explorem per l'esquerra i la dreta
    dfs_aux(node.left, counts, codes, codi + "-")
    dfs_aux(node.right, counts, codes, codi + ".")


def encode(text, diccionari):
    """
    Donat un text a codificar i un diccionari de conversió, codifica el text.
    
    Params
    ======
    :text: El text que volem codificar
    :diccionari: El diccionari de conversió que farem servir
    
    Returns
    =======
    :code: Una representació del text usant només els caràcters '.' i '-'
    """
    code = ""
    #Revisem el text lletra a lletra i fem la conversio
    for letter in text:
        code += diccionari[letter]

    return code


def decode(text, diccionari):
    """
    Donat un text a decodificar i un diccionari de conversió, decodifica el text.
    
    Params
    ======
    :text: El text que volem decodificar (caràcters '.' i '-')
    :diccionari: El diccionari de conversió que hem fet servir per codificar
    
    Returns
    =======
    :code: El text resultant de la decodificació.
    """
    #Construim un diccionari amb parelles clau-valor de (codi, lletra) (l'invers del diccionari passat per parametre, que ve amb format (lletra, codi))
    code_dict = {diccionari[key]: key for key in diccionari}
    #Mentre el codi que estem llegint no representi cap lletra, l'anirem guardant aqui
    cache = ""
    #Descodificat
    code = ""
    
    #Revisem el text caracter a caracter
    for letter in text:
        #Afegim el caracter al cache
        cache += letter

        #Si el cache es correspon amb un simbol del diccionari, afegim la descodificacio al output i buidem el cache
        if cache in code_dict:
            code += code_dict[cache]
            cache = ""
        

    return code