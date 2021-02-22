def get_city_year(p0, perc, delta, p):
    years = 1
    curr = p0 + p0 * (0.01 * perc) + delta
    if curr <= p0: # remember == would imply stagnation
        return -1
    else:
        while curr < p:
            curr = curr + curr * (0.01 * perc) + delta
            years += 1
        return years
 
 
print(get_city_year(1000, 2, -50, 5000))
print(get_city_year(1500, 5, 100, 5000))
print(get_city_year(1500000, 2.5, 10000, 2000000))
print(get_city_year(1000, 2, -20, 2000))