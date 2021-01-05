def get_city_year(p0, perc, delta=50, p=10_000):
    all_p0 = []
    while p0 < p:
        newp = p0 + p0 * perc / 100 + delta
        if newp <= p0:
            print("Demographics not good!")
            return -1
        p0 = newp
        all_p0.append(int(p0))
        p0 = all_p0[-1]
    result = len(all_p0)
    print(all_p0)
    return result

print(get_city_year(1000, 2, -50, 5000))
print(get_city_year(1500, 5, 100, 5000))
print(get_city_year(1500, 0, 0, 5000))

