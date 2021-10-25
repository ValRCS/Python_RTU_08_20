#3 Pilsēta
def get_city_year(p0, perc, delta, p, verbose=False):
    year = 1
    while True:
        population = int(p0 + (p0 * perc/100) + delta) # every year we have exact number of people
        if verbose:
            print(f"New pop: {population} previous pop {p0}")
        if population <= p0:
            return -1  #so called early return
        elif population < p:
            p0 = population
            year += 1
        else: # means our current population >= p our target population
            return year
 
print(get_city_year(1000, 2, 50, 1200)) 
print(get_city_year(1000, 2, -50, 5000))
print(get_city_year(1500, 5, 100, 5000))
print(get_city_year(1500000, 2.5, 10000, 2000000))
print(get_city_year(1_000_000, 0, 0, 2000000))
print(get_city_year(1_000, -2, 25, 2000, verbose=True)) # hard test because initially we gain some people
