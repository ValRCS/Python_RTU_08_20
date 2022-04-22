# def get_city_year(p0, perc, delta, p):
#     i=0
#     p1=p0
#     while p0<p and p0>=p1:
#          p0=p0+(p0*perc/100)+delta
#          i+=1
#     if p0>=p1:
#         return i
#     else:
#         return -1

# 3. Pilsēta
 
def get_city_year(p0 : int, perc : int, delta : int, p: int) -> int:
    G = lambda p0, fperc, delta : int(p0 + p0 * fperc + delta)
    fperc = perc / 100.0
    population_after_year_1 = G(p0,fperc,delta)
    years = 1
    total = population_after_year_1
    if p > p0:
        if population_after_year_1 <= p0:
            return -1
        else:
            while(total<p):
                # print(f"After {years} population is increased to {total}")
                total = G(total,fperc,delta)
                years += 1
    if p < p0:
        if population_after_year_1 >= p0:
            return -1
        else:
            while(total>p):
                # print(f"After {years} population is decreased to {total}")
                total = G(total,fperc,delta)
                years += 1
    return years

print(get_city_year(1500000, 2.5, 10000, 2000000))
print(get_city_year(1000, 2, -50, 5000))
print(get_city_year(1500, 5, 100, 5000))
print(get_city_year(1000,2,50,1200) )
print(get_city_year(1000,0,0,1200) )
print(get_city_year(1000,-3,40,2000) ) # TODO handle slowing growth into negative numbers