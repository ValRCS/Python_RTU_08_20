# Pilsēta
 
# Pilsētā ir zināms skaits iedzīvotāju p0
# Katru gadu nāk klāt procentuāls skaits perc
# Katru gadu nāk klāt(vai aizbrauc) arī zināms skaits delta
# Mums ir jāzina, kad(ja vispār) pilsēta sasniegs iedzīvotāju skaitu p
# Uzrakstiet funkciju get_city_year(p0, perc, delta, p) kas atgriež gadus (pilnus) kad p tiks sasniegts.
# Ja p nevar sasniegt, tad atgriežam -1
# PS. Ievērojam, ka padodam perc kā procentu kas jāpārvērš decimāl skaitlī.
 
# def get_city_year(p0, percentage, delta, target_pop, debug=False):
#     year_to_target = 1
#     while p0 < target_pop :
#         citizens_next_year = p0 + p0 * percentage * 0.01 + delta 
#         if round(citizens_next_year - p0, 2) <= 0:   
#             return -1
#         elif target_pop - citizens_next_year > 0: 
#             p0 = citizens_next_year
#             year_to_target += 1
#         else:
#             return year_to_target
#         if debug:
#             print(f"Year: {year_to_target}, citizens: {p0}")
        
# Mums ir jāzina, kad(ja vispār) pilsēta sasniegs iedzīvotāju skaitu p
 
# Uzrakstiet funkciju get_city_year(p0, perc, delta, p) kas atgriež gadus (pilnus) kad p tiks sasniegts.
 
# Ja p nevar sasniegt, tad atgriežam -1
 
 
def get_city_year(p0, perc, delta, p):
    population = p0
    years_to_p = 0
    year_1 = (p0 + p0*perc/100 + delta) - p0
    if p0 == p: # stagnation
        return  0
    if (p - p0  > 0 and year_1 < 0 ) or ( p - p0  < 0 and year_1 > 0): # not posible
        return -1
    if p0 < p: # growth
        while population < p:
            years_to_p+=1
            population = (population + (int)(population*perc/100) + delta) 
 
    elif p0 > p: # reduction
         while population > p:
            years_to_p+=1
            population = (population +  (int)(population*perc/100) + delta) 
   
    return years_to_p
 
print( get_city_year(1000, 2, 50, 1200))
print(get_city_year(1000, 2, -50, 5000))
print(get_city_year(1500, 5, 100, 5000) )
print(get_city_year(1500000, 2.5, 10000, 2000000))
print(get_city_year(1000, -1.5, 1, 800))
print(get_city_year(1000, 2, -50, 5000)) # -> -1 # samērā aktuāla problēma
print(get_city_year(1500, 5, 100, 5000)) # -> 15
print(get_city_year(1500000, 2.5, 10000, 2000000)) #  -> 10
# print(get_city_year(1000, -2, 30, 2000, debug=True))
print(get_city_year(1000, -1, -20, 500)) 
# tricky one FIXME 
# print(get_city_year(1000, -2, 30, 2000)) # -> -1