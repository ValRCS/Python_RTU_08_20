# def get_city_year(p0,perc,delta,presult, max_years=100):
#     i = 1
#   #  return result
#     while i<=max_years:
#         result = int(p0 + (p0 * (perc / 100)) + delta)
#         if result>=presult:
#             return(f"\nCity will reach desired population in {i} years and at {i}.year city will have {result} inhabitants")
#         else:
#             print(f"After {i} years since beginging of population control there will be {p0}+{p0}*{perc/100}+{delta}={result} inhabitants")
#             p0=result
#             i+=1
#     print(f"\nCity would not reach population of {presult}  in next 50 years!")
 

# print(get_city_year (1000,2,50,1200))
# # print(get_city_year(1000,2,100,10799))

# Uzd #3 - Pilsēta
def get_city_year(p0, perc, delta, p):  
  perc *= 0.01
  
  if p0 == p:
    return 0 # "Pilsētā jau ir "+str(p)+" iedzīvotāji!"
    
  elif p0 < p:   #tiek prognozēts iedzīvotāju pieaugums 
    # ja pieaugums negatīvs vai nulle, nevarēs sasniegt p
    # if p0*perc+delta<=0:
    #   return "Plānotais iedzīvotāju skaits "+str(p)+" nekad netiks sasniegts!"
    # ja pieaugums pozitīvs
    g = 0
    while p0 < p:

      new_pop = int(p0 + p0*perc + delta)
      if new_pop <= p0: # we reached an equilibrium before reaching p
          return -1
      p0 = new_pop
      g += 1
    return g
    
  else:   #tiek prognozēts iedzīvotāju skaita samazinājums
    # ja pieaugums pozitīvs vai nulle, nevarēs sasniegt p
    # if p0*perc+delta>=0:
    #   return -1
    # ja pieaugums negatīvs
    g = 0
    while p0 > p:
      new_pop = int(p0 + p0*perc + delta)
      if new_pop >= p0: # we reached an equilibrium before reaching p
          return -1
      p0 = new_pop
      g += 1
    return "Iedzīvotāju skaits līdz "+str(p)+" būs samazināsies pēc "+str(g)+" gadiem."
    

print(f"get_city_year(100,2,50,1200) -> {get_city_year(1000,2,50,1200)}")
print(f"get_city_year(1000,2,-50,5000) -> {get_city_year(1000, 2, -50, 5000)}")
print(f"get_city_year(1500,5,100,5000) -> {get_city_year(1500, 5, 100, 5000)}")
print(f"get_city_year(1500000,2.5,10000,2000000) -> {get_city_year(1500000, 2.5, 10000, 2000000)}")

print(f"get_city_year(1000, -2, 30, 2000) -> {get_city_year(1000, -2, 30, 2000)}")

print(f"get_city_year(1000, -2, 30, 500) -> {get_city_year(1000, -2, 30, 500)}")
print(f"get_city_year(1000, -2, 10, 950) -> {get_city_year(1000, -2, 10, 950)}")
print(f"get_city_year(1000, -2, -10, 450) -> {get_city_year(1000, -2, -10, 450)}")