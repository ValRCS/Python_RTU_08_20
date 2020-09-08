# janis idea
def get_city_year(p0, perc, delta, p):
    i = 0
    if p0 >= p:
        return 0
    result = p0 + (p0 * (perc/100)) + delta
    if result < p0:
        return -1
    else:
        while p0 < p:
            i += 1
            result = p0 + (p0 * (perc/100)) + delta
            p0 = result
        return i


def main():
    print(get_city_year(1000, 2, -50, 1200))
    print(get_city_year(1000, 2, 50, 1200))
    print(get_city_year(1500, 5, 100, 5000))
    print(get_city_year(1_500_000, 2.5, 10_000, 2_000_000))
    print(get_city_year(2_500_000, 2.5, 10_000, 2_000_000))


if __name__ == "__main__":
    main()
