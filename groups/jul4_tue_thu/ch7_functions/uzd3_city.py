#Pilsētā ir zināms skaits iedzīvotāju p0
#Katru gadu nāk klāt procentuāls skaits perc
#Katru gadu nāk klāt(vai aizbrauc) arī zināms skaits delta
#Mums ir jāzina, kad(ja vispār) pilsēta sasniegs iedzīvotāju skaitu p
#Uzrakstiet funkciju get_city_year(p0, perc, delta, p) kas atgriež gadus (pilnus) kad p tiks sasniegts.
def get_city_year(p0, perc, delta, p):
    years = 0
    while p0 < p:
        pieaugums = p0 * perc/100 + delta
        if round(pieaugums,4) <= 0: # trickly because floats are not precise
            return -1
        else:
            p0 += pieaugums
            years += 1
    return years

print(get_city_year(1000, 2, -50, 1200)) # -1
print(get_city_year(1000, 2, 50, 1200)) # 3

# this is tricky because initially our population increases, but then it stagnates and starts to decrease
print(get_city_year(1000, -2, 30, 2000)) # -1