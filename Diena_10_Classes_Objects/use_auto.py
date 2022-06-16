import auto
from auto import Auto # if i just need Auto from auto.py module

new_car = auto.Auto()
new_car.add_gps(auto.GPS(33,42))
new_car.print_gps()

also_car = Auto()