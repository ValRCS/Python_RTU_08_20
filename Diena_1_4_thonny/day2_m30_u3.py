precision = 2
t_celsium = float(input('Temperature in Celsius?\n'))
t_farenheit = round(32 + t_celsium * (9/5), precision)
print(f'Celsium {t_celsium} = farenheit {t_farenheit}')