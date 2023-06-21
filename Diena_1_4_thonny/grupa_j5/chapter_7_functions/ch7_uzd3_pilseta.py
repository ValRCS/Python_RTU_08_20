# Pilsētā kurā ir 'p0' iedzīvotāju, katru gadu nāk klāt 'perc'% iedzīvotāji, 
#   kā arī nāk klāt vai aizbrauc 'delta' iedzīvotāji,
#   kad, ja vispār, pilsēta sasniegs 'p' skaitu iedzīvotāju?
 
# def get_city_year(p0,perc,delta,p, debug=False):
#     if p0 > p0+(p0 * perc*0.01)+delta:                     #Pārbaudam vai ir vērts aizņemt atmiņu
#         print("Your city's population is decreasing")      #Ja nav tad informējam lietotāju
#         return -1                                          #un atgriežam prasīto rezultātu
#     year = 0                                               #Ja populācija aug tad uzsākam gadu atskaiti
#     while p0 < p:                                           #Atveram Loopu
#         inc_pop_percent = p0 * (0.01 * perc)                #Noskaidrojam augošo procentu skaitu
#         current_population = p0                             #Saglabājam tagadējo populācijas skaitu
#         current_population += inc_pop_percent+delta         #Aprēķinam un saglabājam jauno populācijas skaitu
#         p0 = current_population   
#         if debug:
#             print(f"Current pop {current_population}")                          #jaunu procentu aprēķināšanai
#         year += 1     
#     if debug:                                      #Pieskaitam veiksmīgo gadu
#         print("Good work, your city is growing!")              #Kad vēlamais rezultāts sasniegts informējam lietotāju
#     return year                                             #Un atgriežam gadu skaitu
 
def get_city_year(p0, perc, delta, p, debug=False):
    """
    Calculates the year when the city population reaches p
    p0 - initial population
    perc - percentage increase
    delta - people coming/leaving
    p - target population
    debug - prints debug messages if True
    returns year when p is reached
    returns -1 if p is never reached
    """
    year = 0
    while p0 < p:
        increase = p0 * (perc / 100) + delta
        if debug:
            print(f"Year {year} Increase {increase}")
        # turns out floating point numbers are not precise
        # we could have practially zero increase
        if round(increase,4) <= 0:
            # so called early return
            return -1
        # possibly current population should be rounded down
        p0 += increase
        year += 1
        if debug:
            print(f"Year {year} Current pop {p0}")

    return year
 
result = get_city_year(1000, 2, -50, 5000)
 
 
print(get_city_year(1000,2,-50,5000))
print(get_city_year(1500,5,100,5000))
print(get_city_year(1500000,2.5,10000,2000000))
print(get_city_year(1000, -2, 30, 2000, debug=True))

# TODO make a function that handles target population being smaller
#  than initial population