def get_city_year(p0: int, perc: float, delta: int, p: int) -> int:
    """
    :param p0: pilsētā ir zināms skaits iedzīvotāju
    :param perc: katru gadu nāk klāt procentuāls skaits
    :param delta: katru gadu nāk klāt(vai aizbrauc) arī zināms skaits
    :param p: mērķis (pilsēta gaidmais iedzīvotāju skaitu)
    :return: gadi (pilnie), kad p tiks sasniegts;
             0 - ja mērķis jau ir sasniegts ( p == p0);
             -1 - ja p nevar sasniegt (populācijas mērķis ir mazāks par sākuma populāciju,
                bet populācijas pieaugums ir pozitīvs vai otrādi);
             None - ja ikgadējās izmaiņas NAV (pieaugums ir 0, STAGNĀCIJA);
    """
    # Sākuma jāapstradā izņemumi
    if p == p0:
        return 0  # ja mērķis jau ir sasniegts
 
    perc /= 100  # pārveidojām float (procentos)
    pieaugums = int(perc * p0) + delta  # sākotnējs pieaugums
    if not pieaugums:
        return None  # ja ikgadējās izmaiņas NAV (pieaugums ir 0), stagnācija
 
    if (p0 > p and pieaugums > 0) or (p0 < p and pieaugums < 0):
        # ja p nevar sasniegt (populācijas mērķis ir mazāks par sākuma populāciju,
        # bet populācijas pieaugums ir pozitīvs vai otrādi)
        return -1
 
    # Nav izņēmumu, main Loop
    year_counter = 0
    #if p < p0:
    #    p0, p = p, p0  # Mainām ar vietam p un p0, ja mērķis ir mazaks par sakuma polulāciju
    if p > p0:
        while p0 < p:  # Ja mērķis ir lielaks par sakumā polulāciju
            year_counter += 1
            p0 += int(p0 * perc + delta)  # Ikgadejs cilveku pieaugums var but +/- natuŗālais skaitlis (vesels)
            print(p0)
    else:
        while p0 > p:  # Ja mērķis ir mazāks par sakumā polulāciju
            year_counter += 1
            p0 += int(p0 * perc + delta)
    return year_counter

print(get_city_year(1000,2,50,1200))
print(get_city_year(1000, 2, -50, 5000))
print(get_city_year(1500, 5, 100, 5000))
print(get_city_year(1500000, 2.5, 10000, 2000000))
print(get_city_year(1000, -2.5, -30, 500))
print(get_city_year(1000, 5, -50, 1200))

print(get_city_year(1000, -4, 50, 2000))  # FIXME case where growth stops later on