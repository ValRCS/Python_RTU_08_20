## 3.uzdevums
def get_city_year(p0, perc, delta, p):
    # often early return is useful for checking if exit condition is met
    if p0 >= p:
        return 0 # we already reached the goal - no years to wait
    years = 0
    while p0 <= p:
        prev = p0 # keep previous value
        p0 += p0 * (perc/100) + delta
        #print(p0)
        if p0 <= prev: # we need to check if we are making progress
            # years = -1
            # break
            return -1  # could return "Nevar sasniegt"
        years += 1       
    return years
 
print(get_city_year(1000,2,50,1200)) # -> 3
print(get_city_year(1000, 2, -50, 5000)) # -> -1 # samērā aktuāla problēma
print(get_city_year(1500, 5, 100, 5000)) # -> 15
print(get_city_year(1500000, 2.5, 10000, 2000000)) # -> 10
print(get_city_year(1000, -2, 30, 2000)) # -> -1
print(get_city_year(1000, -20, -5453, 1000)) # -> 0