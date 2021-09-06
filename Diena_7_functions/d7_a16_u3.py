# def get_city_year(p0, perc, delta, p):
#     i = 0
#     while p > p0:
#         formula = p0 * (perc * 0.01) + delta
#         if delta > formula:
#             print(-1)
#             return -1 # so called early return
#         else:
#             p0 = p0 + formula
#             i += 1
#     print(i)
#     return i

def get_city_year(p0, perc, delta, p):
    if p < p0:
        p, p0 = p0, p # swap
    count = 1
    perc = perc / 100
    new_population = p0 + p0 * perc + delta
    if new_population > p0:
        while p0 < p:
            p0 = p0 + p0 * perc + delta
            if p0 >= p:
                break
            else:
                count += 1
    else:
        count = -1
    return count

print(get_city_year(1000, 2, -50, 5000))
print(get_city_year(1500, 5, 100, 5000))
print(get_city_year(1500000, 2.5, 10000, 2000000))
print(get_city_year(1000, 0, 0, 2000))
print(get_city_year(1000, 2, -50, 970)) # this would be special case