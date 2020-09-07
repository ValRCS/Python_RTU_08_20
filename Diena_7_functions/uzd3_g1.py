# https://github.com/Narusi/Python-Kurss/blob/master/Python_Uzdevums_Funkcijas.ipynb
def get_city_year(p0, perc, delta, p):
    years = 0
    while p0 < p and years <= 10_000:
        p0 += p0 * perc/100 + delta
        years += 1

    if years >= 10_000:
        years = -1

    return years


print(
    f'get_city_year(1000, 2, -50, 5000) -> {get_city_year(1000, 2, -50, 5000)}')
print(
    f'get_city_year(1500, 5, 100, 5000) -> {get_city_year(1500, 5, 100, 5000)}')
print(
    f'get_city_year(1500000, 2.5, 10000, 2000000) -> {get_city_year(1500000, 2.5, 10000, 2000000)}')
