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
        print("Printing GPS")	
        for gps in self.gps_list:
            print(gps.lat, gps.lon)
        return self