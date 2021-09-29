# 3. Pilsēta
 
# def get_city_year(p0=1000,perc=2,delta=50,p=1200):
#     year = 0
#     # need to check what happens in the first year
#     if p0*perc*0.01 + delta > 0:
#          while p0 < p:
#             year += 1
#             p0 = int(p0 + p0*perc*0.01 + delta) # doma pareiza, ka cilvēki daļskaitļos nepienāk
#             print(p0, "pēc", year, ".gada")
#     else:
#         year = -1
#     return year

def get_city_year(p0=1000,perc=2,delta=50,target=1200):
    gadi = 0
    # function without function will not appear outside
    def yearly_change(p0, perc, delta): 
        return p0 * (perc/100) + delta

    if yearly_change(p0, perc, delta) <= 0:
        return -1
    while p0 < target:
        p0 = p0 + yearly_change(p0, perc, delta)
        gadi += 1
    return gadi
 
result = get_city_year(1500,5,100,5000)
print("Gadu kad p tiks sasniegts =",result)
print("Gadu kad p tiks sasniegts =",get_city_year())

# functions are first class citizens meaning we can pass them around like other data
gcy = get_city_year # notice we do not call the function here just the reference
# gcy is just a shortcut to get_city_year , rather they both point to the same function
print(get_city_year) # this is the memory address of function
print(gcy) # this is the memory address of function
print(type(gcy), type(get_city_year))
print(gcy())
print(gcy(1500,5,100,5000))