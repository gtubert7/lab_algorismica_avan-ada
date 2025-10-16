def refill_prices(K, stations, prices):
    """
    Repostatge no òptim de vehicles amb costos.
    
    Params
    ======
    :K: dipòsit del vehicle
    :stations: llista de benzineres. L'últim element és el destí.
    :prices: Llista de preus. Té un element menys que 'stations'.
    
    Returns
    =======
    :exists: Booleà True/False depenent de si existeix o no solució al problema.
    :num_stops: Número de benzineres a les que hem de parar.
    :stops: Quilòmetres de les benzineres on fem parada.
    :value: Cost del trajecte.
    """
    index_estacio_actual = 0
    barata = float("inf")
    estacio_actual = 0
    exists = False    
    stops = []
    num_stops = len(stops)
    value = 0.0
    
    while estacio_actual < stations[-1] and not exists:
        i = index_estacio_actual
        exists = False
        while i < len(prices) and stations[i] - estacio_actual <= K:
            exists = True
            if prices[i] < barata:
                barata = prices[i]
                index_estacio_actual = i
            i += 1
       
        
        value += prices[index_estacio_actual]*(stations[index_estacio_actual] - estacio_actual)
        estacio_actual = stations[index_estacio_actual]

        stops.append(estacio_actual)

    num_stops = len(stops)



    return exists, num_stops, stops, value