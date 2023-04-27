# Alaternative to inheritance is composition

class GPS:
    def __init__(self, lat=56.67, lon=24.4):
        self.lat = lat
        self.lon = lon

class Auto:
    # remember default sequence types should be tuples not lists!
    def __init__(self, color="Black", gps_list=()):
        self.color = color
        self.gps_list = list(gps_list)  # use list if i need to add new GPS

    def add_gps(self, gps: GPS):
        self.gps_list.append(gps)
        return self
    
    def print_gps(self):
        print("Printing List of ALL GPS in car")	
        for gps in self.gps_list:
            print(gps.lat, gps.lon)
        return self
    

my_auto = Auto()
my_auto.print_gps()
my_auto.add_gps(GPS(56.67, 24.4))
my_auto.print_gps()
my_auto.add_gps(GPS(56.67, 24.45))
my_auto.print_gps()

# create a list of GPS objects
gps_list = [GPS(56.67, 24.4), GPS(56.67, 24.45), GPS(56.67, 24.5)]

# I pass the list of GPS objects to the constructor of Auto class
my_other_auto = Auto("Red", gps_list)
my_other_auto.print_gps()

import random
# the lat will be from O to 9
# the lon will be random from 1 to 90
# hopefully geographers will forgive me for this
random_gps_list = [GPS(n, random.randint(1,90)) for n in range(10)]

my_third_auto = Auto("Blue", random_gps_list)
my_third_auto.print_gps()