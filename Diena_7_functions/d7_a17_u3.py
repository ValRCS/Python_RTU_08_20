# def get_city_year(p0,percent,delta,p_aim):   
#     population_grow = p0
#     year = 0

#     while population_grow <=p_aim:
#         population_grow=population_grow+percent*population_grow/100+delta
#         year += 1
#         # print("es dzivo te", population_grow)
#         if population_grow <= p0: # stagnation is no good either
#             # print("es samazinos")
#             return -1
            
#     return year

# recursive solution (function calls itself)
# def get_city_year(p0, perc, delta, p):
    
#     if p0*perc/100 + delta <= 0:
#         return -1 
 
#     if p0+p0*perc/100+delta < p:
#         years =  get_city_year(p0+p0*perc/100+delta, perc, delta, p)+1
#     else: 
#         years = 1
        
#     return years

def get_city_year(p0, perc, delta, p):
    def _get_years():
        years = 0
        # assumption: population can be float, otherwise ceil or floor needed
        population = p0
        while population <= p:
            population += population * (perc / 100) + delta
            years += 1
            #print(f">>> year {years}: pop: {population}")
        return years
 
    if (p0 * (perc / 100)) + delta <= 0:
        return -1
    else:
        return _get_years()
 
# test
talsi = get_city_year(1000, 2, -50, 5000)
ape = get_city_year(1500, 5, 100, 5000)
warsaw = get_city_year(1500000, 2.5, 10000, 2000000)
 
print(f"talsi: {talsi}")
print(f"ape: {ape}")
print(f"warsaw: {warsaw}")
 
print(get_city_year(1500, 5, 100, 5000))
print(get_city_year(1000, 2, -50, 5000) )
print(get_city_year(1500, 5, 100, 5000))
print(get_city_year(1500000, 2.5, 10000, 2000000))
print(get_city_year(1000,0,0, 2000)) # edge case stagnation