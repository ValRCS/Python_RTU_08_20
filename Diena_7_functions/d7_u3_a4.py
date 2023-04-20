# 3.Uzdevums
def get_city_year(p0, perc, delta, p):
    years = 0
    while p0 < p:
        p0 += p0 * perc / 100 + delta
        years += 1
        # TODO fix this not complete solution
        # issue is that 100 is an arbitrary number
        if years > 100:  # Pārbaudīsim, vai gadu skaits nav pārāk liels, lai izvairītos no bezgalīgās cikla problēmas.
            return -1
    return years

result1 = get_city_year(1000, 2, -50, 5000)
print(result1)  # -1
 
result2 = get_city_year(1500, 5, 100, 5000)
print(result2)  # 15
 
result3 = get_city_year(1500000, 2.5, 10000, 2000000)
print(result3)  # 10

result4 = get_city_year(1000, 1, 0, 2000)
print(result4)  
# rule of 72 wikipedia: https://en.wikipedia.org/wiki/Rule_of_72


result5 = get_city_year(1000, 0.01, 0, 2000)
print(result5)  

# careful with negative percentage and positive delta
result6 = get_city_year(1000, -2, 30, 2000)
print(result6)