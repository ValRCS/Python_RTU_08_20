def get_city_year(p0:int, perc, delta:int, p:int, verbose=False, precision=2) -> int: 
    years = 0
    growth_rate = perc / 100  # pārvērš procentus decimāl skaitlī

    while p0 < p:
        new_population = p0 + p0 * growth_rate + delta  # nākamā gada iedzīvotāju skaitu

        years += 1

        if round(new_population, precision) <= round(p0, precision):  # p nevar sasniegt, paliek sliktāk vai stagnē
            if verbose:
                print("Population can't reach the target population")
                print(f"Previous Population: {p0}, Current {new_population} Target population: {p}")
            return -1

        p0 = new_population # varam droši piešķirt jauno populāciju

    return years
 
 
print(get_city_year(1000, 2, -50, 5000))
print(get_city_year(1500, 5, 100, 5000))
print(get_city_year(1500000, 2.5, 10000, 2000000))

# let's test with negative percentage values
print(get_city_year(1000, -2, -50, 5000))
print(get_city_year(1000, -2, 30, 5000, verbose=True))
print(get_city_year(1000,2,50,1200, verbose=True)) # 3