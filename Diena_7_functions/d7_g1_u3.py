def get_city_year(p0,perc,delta,p):
    year = 1
    dec_perc = perc/100
    while True:
        pop_year = p0 + p0*dec_perc+delta
        if pop_year <= p0:
            return -1
        elif pop_year < p:
            year += 1
            p0 = pop_year
        else:
            return year



# def get_city_year(p0, perc, delta, p):
 
#     def in_a_year(p_current): #so that less mess in the function itself
#         return p_current + (p_current*0.01*perc) + delta
    
#     years = 1
#     p_next = in_a_year(p0)
    
#     if p_next <= p0: #meaning population is not growing at all
#         return -1
#     else:
#         while p_next < p:
#             years += 1
#             p_next = in_a_year(p_next)    
#         return years
 
print(get_city_year(1000, 2, -50, 5000))
print(get_city_year(1500, 5, 100, 5000))
print(get_city_year(1500000, 2.5, 10000, 2000000))