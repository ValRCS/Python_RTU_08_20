# Python Class
# Classes -> combine related data(properties)
# Classes -> combine related funcionality(methods)
# Objects - instances of class
# Classes: blueprints
# Objects: concrete realization of those blueprints
# https://docs.python.org/3/tutorial/classes.html

# how to store and process data about garage
my_garage = ["paint can", "old papers", "rotting potatoes"]
my_garage_d = {"paints": ["white", "black"], "food": "potatoes"}

# the simplest empty class definition


class Garage:
    g_name = "just a garage"

    def __init__(self, color="green"):
        self.color = color
        print(f"Initialized class instance with {self.color=}")

    def simple_print(self):
        print(f"Oh {self.g_name=} {self.color=}")


# create new objects based on class definition
homer_garage = Garage()
flanders_garage = Garage()
# two different objects from the same blueprint(class defintion)
print(id(homer_garage), id(flanders_garage))

homer_garage.paints = ["white", "black"]
homer_garage.foods = "eaten"
print(homer_garage.paints)
print(homer_garage.foods)


class FancyGarage(Garage):
    # Class Attribute
    gtype = "Fancy"
    # constructor method, called when we created object from this class
    total_travel = 0

    def __init__(self, cars, wines, color="Gold"):
        super().__init__(color)  # Python 3.x+ we call our parent class constructor
        self.cars = cars
        self.wines = wines

    # we have to give self argument for all methods inside classes
    def pretty_print(self):
        print(f"{self.gtype=}, {self.cars=}, {self.wines=}, {self.total_travel=}")

    def drive(self, distance):
        print(f"Driving {self.cars} a distance of {distance}")
        self.total_travel += distance
        return self  # Allows chaining of objects

    def get_longest_wine(self):
        wines_length = sorted(self.wines, reverse=True)
        return wines_length[0]


burns_garage = FancyGarage("Bentley", ["Rioja", "Temparillo", "Riesling"])
crusty_garage = FancyGarage("Rolls", ["Cabernet"])


print(burns_garage.cars)
print(burns_garage.wines)
burns_garage.gtype = "Rich"
burns_garage.pretty_print()
crusty_garage.pretty_print()


crusty_garage.drive(60)
crusty_garage.drive(160)
crusty_garage.drive(20)
crusty_garage.pretty_print()
print(burns_garage.get_longest_wine())
print(crusty_garage.get_longest_wine())
burns_garage.drive(100).drive(150).drive(80).pretty_print()
wilma_garage = Garage("pink")
wilma_garage.simple_print()
burns_garage.simple_print()
brockman_garage = FancyGarage("Ferrari", "Chuck Wine")
comic_guy_garage = FancyGarage("Ferrari", "Chuck Wine", "Bright Red")
comic_guy_garage.simple_print()  # can use Garage method
comic_guy_garage.pretty_print()  # can use Fancy Garage method
