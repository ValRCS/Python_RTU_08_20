def get_city_year(p0, perc, delta, p):
    result = p0 + p0*(perc/100) + delta
    years = 1
    if result <= p0:
        years = -1
    else:
        while result <= p:
            result = result + result * (perc/100) + delta
            years += 1
            print(years)
    return years
 
print(get_city_year(1500, 5, 100, 5000))
# print(get_city_year(1000, 2, -50, 5000)) 
# print(get_city_year(1500000, 2.5, 10000, 2000000))
print(get_city_year(1000, 0, 0, 1200))