def refill_prices_optim(K, stations, prices):
    """
    Repostatge òptim de vehicles amb costos. 
    
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
    
    exists = False    
    stops = []
    num_stops = len(stops)
    value = 0.0
    prices.append(0)
    index_estacio_actual = -1
    estacio_actual = 0
    stops = []
    value = 0.0
    litres_actuals = K

    exists = True
    while estacio_actual < stations[-1] and exists:
        if stations[index_estacio_actual + 1] - estacio_actual > K:
            exists = False
        else:
            preu_actual = prices[index_estacio_actual]
            barata = prices[index_estacio_actual + 1]
            i = index_estacio_actual + 2
            index_estacio_actual += 1
            #EN AQUEST WHILE NO HAURIA DE SER BARATA > PREU_ACTUAL (ESTRICTE)?
            while i < len(prices) and stations[i] - estacio_actual <= K and barata >= preu_actual:
                if prices[i] < barata:
                    barata = prices[i]
                    index_estacio_actual = i
                i += 1
            #I LLAVORS AQUI ANIRIA UN <= ??
            if barata < preu_actual:
                #Si tenim menys litres del que ens cal:
                if litres_actuals < stations[index_estacio_actual] - estacio_actual:
                    value += preu_actual*(stations[index_estacio_actual] - estacio_actual - litres_actuals)
                    litres_actuals = 0
                else:
                    litres_actuals -= stations[index_estacio_actual] - estacio_actual
            else:
                #CAL FER AIXO /// FET, potser per revisio
                value += preu_actual*(K-litres_actuals)
                litres_actuals = K - stations[index_estacio_actual] + estacio_actual

            value = round(value, 2)
        
        estacio_actual = stations[index_estacio_actual]
        stops.append(estacio_actual)

    num_stops = len(stops)

    return exists, num_stops, stops, value

    return exists, num_stops, stops, value
        