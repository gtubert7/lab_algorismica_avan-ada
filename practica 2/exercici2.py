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
    #Revisem que no haguem arribat ja a l'estacio
    while estacio_actual < stations[-1] and exists:
        #Revisem que tenim prou benzina per arribar com a minim a la benzinera més inmediata
        if stations[index_estacio_actual + 1] - estacio_actual > K:
            exists = False
        else:
            #Ens guardem el preu de la benzinera on estem
            preu_actual = prices[index_estacio_actual]
            #Busquem la propera benzinera més barata
            barata = prices[index_estacio_actual + 1]
            i = index_estacio_actual + 2
            index_estacio_actual += 1
            while i < len(prices) and stations[i] - estacio_actual <= K and barata >= preu_actual:
                if prices[i] < barata:
                    barata = prices[i]
                    index_estacio_actual = i
                i += 1
            #Mirem si el preu de la benzinera on volem anar es menor que on som ara
            if barata < preu_actual:
                #Si tenim menys litres del que ens cal:
                if litres_actuals < stations[index_estacio_actual] - estacio_actual:
                    #Emplenem la quantitat esctrictament necessaria per arribar a la següent
                    value += preu_actual*(stations[index_estacio_actual] - estacio_actual - litres_actuals)
                    litres_actuals = 0
                else:
                    #No cal emplenar
                    litres_actuals -= stations[index_estacio_actual] - estacio_actual
            #Si la benzinera que hem seleccionat es mes cara que l'actual
            else:
                #Omplim a la que estem fins al maxim
                value += preu_actual*(K-litres_actuals)
                #Arribem a la següent amb els litres que no hem gastat
                litres_actuals = K - stations[index_estacio_actual] + estacio_actual

            value = round(value, 2)
        
        estacio_actual = stations[index_estacio_actual]
        stops.append(estacio_actual)

    num_stops = len(stops)

    return exists, num_stops, stops, value

        