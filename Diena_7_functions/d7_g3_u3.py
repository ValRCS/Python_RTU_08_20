

def get_city_year(p0, perc, delta, p):
    years = 1
    while True:
        citizen_amount = int(p0 + (p0 * perc/100) + delta) # also math.floor when import math first
        if citizen_amount <= p0:
            return -1
        elif citizen_amount < p:
            p0 = citizen_amount
            print(f"After {years} years population is {p0}")
            years += 1
        else:
            return years

 
 
print(get_city_year(1000, 2, 50, 1200))
print(get_city_year(1000, 2, -50, 5000))
# print(get_city_year(1500, 5, 100, 5000))
# print(get_city_year(1500000, 2.5, 10000, 2000000))

print(get_city_year(1000, 10, -20, 5000))