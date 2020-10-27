def get_city_year(p0,perc,delta,target):
    years = 0
    if p0 * (perc/100) + delta <= 0:
        return -1

    while p0 < target:
        p0 = p0 + p0 * (perc/100) + delta
        years += 1
    return years
 
# a = int(input("Input current population:"))
# b = float(input("Input percentage increase:"))
# c = int(input("Input delta:"))
# d = int(input("Input future population:"))
# print(get_city_year(a,b,c,d))
print(get_city_year(1000, 2, -50, 5000))
print(get_city_year(1500, 5, 100, 5000))
print(get_city_year(1500000, 2.5, 10000, 2000000))