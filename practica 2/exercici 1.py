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
    index_estacio_actual = -1
    estacio_actual = 0
    stops = []
    value = 0.0
    
    exists = True
    #Revisem que no haguem arribat ja a l'estacio
    while estacio_actual < stations[-1] and exists:
        #Si la següen estacio està més lluny que on podem arribar
        if stations[index_estacio_actual + 1] - estacio_actual > K:
            exists = False
        #Si el desti esta a l'abast del següent trajecte
        elif stations[-1] - estacio_actual <= K:
            index_estacio_actual = -1
        else:
            #Primer busquem la següent estació més barata a l'abast
            index_estacio_actual += 1
            barata = prices[index_estacio_actual]
            i = index_estacio_actual + 1
            while i < len(prices) and stations[i] - estacio_actual <= K:
                if prices[i] < barata:
                    barata = prices[i]
                    index_estacio_actual = i
                i += 1
            #Calculem el preu
            value += prices[index_estacio_actual]*(stations[index_estacio_actual] - estacio_actual)
            value = round(value, 1)
        
        estacio_actual = stations[index_estacio_actual]
        stops.append(estacio_actual)

    num_stops = len(stops)

    return exists, num_stops, stops, value