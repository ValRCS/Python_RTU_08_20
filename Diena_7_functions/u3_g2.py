def get_city_year(p0, perc, delta, p):
    totalYears = 0
    yearCal = p0
    # print("______________________IN______________________")
    while True:
        totalYears+=1
        yearCal = round(yearCal + yearCal * (perc/100) + delta)
        # print(f"{yearCal} ==> {temp} || Goal:[{p}]")
        if yearCal >= p:
            # print("______________________OUT______________________")
            return totalYears
        if p0 > yearCal:
            # print("______________________OUT______________________")
            return -1
 
print(get_city_year(1000, 2, -50, 5000))  
print(get_city_year(1500, 5, 100, 5000)) 
print(get_city_year(1500000, 2.5, 10000, 2000000))


# def get_city_year(p0,perc,delta,p):
#     it0 = p0
#     it = p0
#     year = 0
#     while it < p:
#         it = round(it0*(1+perc/100)+delta)
#         if it<p0:
#             print(f"Iedzīvotāju skaitu {p} nesasniegs")
#             break
#         year += 1
#         print(f"{it0} + {it0} * {perc} + {delta} => {it} pēc {year}.gada")
#         it0 = it


# get_city_year(1000, 5, 50, 2000)