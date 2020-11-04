# # Python Class
# # Classes -> combine related data(properties)
# # Classes -> combine related funcionality(methods)
# # Objects - instances of class
# # Classes: blueprints
# # Objects: concrete realization of those blueprints
# # https://docs.python.org/3/tutorial/classes.html

# # how to store and process data about garage
my_garage = ["paint can", "old papers", "rotting potatoes"]
my_garage_d = {"paints": ["white", "black"], "food": "potatoes"}

# # empty class definition


# class EmptyClass:
#     pass


# # # i create an  based on class blueprint

# empty_class_instance_object = EmptyClass()
# empty_class_instance_object.paint = ["red", "blue"]
# empty_class_instance_object.papers = ["Diena"]
# print(empty_class_instance_object.paint)
# print(empty_class_instance_object)
# empty_2 = EmptyClass()
# empty_2.painter = "Picasso"
# empty_2.paint = "Guasha"
# print(empty_2.paint, empty_class_instance_object.paint)

# # the simplest empty class definition

# color = "Global color"


class House:
    def __init__(self, color="green", nails=0):
        self.color = color
        self.nails = nails
        print(f"Initialized class instance with {self.color=} {self.nails=}")

    def simple_print(self):
        print(f"Oh {self.color=} {self.nails=}")
        return self

    def set_color(self, new_color):
        # some verification on sane color here maybe
        self.color = new_color
        print(f"Changed color to {self.color}")


# my_house = House() # creaing new object, in other class instance
# i've created an object my_house based on House class blueprints
# print(type(my_house))
# my_house.simple_print()

# friends_house = House(color="blue", nails=1_000)
# friends_house.simple_print()
# print(my_house.color)
# my_house.set_color("red")
# my_house.simple_print()

# def inside class defines method (so function which is called by class or object)


class Garage:
    g_name = "just a garage" # better to sparingly we can run in some weird effects

    # classes constructor method called when we make a new object instance from this class
    # dunder syntax __init__
    def __init__(self, color="green", nails=0):
        self.color = color
        self.nails = nails
        print(f"Initialized class instance with {self.color=} {self.nails=}")

    def __str__(self): # this is responsible for string representation
        return f"My garage {self.color} with nails: {self.nails} and name: {self.g_name}"

    def __repr__(self):
        return f"My garage {self.color} and name: {self.g_name}"

    def __add__(self, other):
        # return self.nails + other.nails
        new_color = self.color+"_"+other.color
        new_nails = self.nails + other.nails
        return Garage(new_color, new_nails)


    def simple_print(self):
        print(f"Oh {self.g_name=} {self.color=} {self.nails=}")
        return self

    def add_nails(self, new_nails=1):
        self.nails += new_nails
        return self

    def set_nails(self, new_nail_count=0):
        self.nails = new_nail_count
        return self

    # OOP getters method
    def get_current_nails(self):
        # formatting, data sanitation, so on
        return self.nails+1000


# create new objects based on class definition
homer_garage = Garage(nails=33)
flanders_garage = Garage(nails=55)
# two different objects from the same blueprint(class defintion)
print(id(homer_garage), id(flanders_garage))
print(homer_garage.g_name)
print(Garage.g_name) 
# homer_garage.simple_print()
# flanders_garage.simple_print()
millhouse_garage = Garage(color="purple")
millhouse_garage.simple_print()

homer_garage.g_name = "Homer's garage"
homer_garage.simple_print()
print(Garage.g_name) 
print(homer_garage)
super_garage = homer_garage + flanders_garage
print(super_garage)
# simpsons_house = House(color="yellow")
# print(simpsons_house.color)
# simpsons_house.simple_print()
# print(str(simpsons_house))
# print(homer_garage.nails)
# print(homer_garage.get_current_nails())
# print(homer_garage.nails)

# millhouse_garage.nails
# millhouse_garage.add_nails(7)
# millhouse_garage.add_nails(17)
# millhouse_garage.simple_print()
# millhouse_garage.add_nails(10).add_nails(25).simple_print()
# millhouse_garage.add_nails(5).simple_print()
# millhouse_garage.set_nails(-50).add_nails(10).simple_print()

# # # homer_garage.paints = ["white", "black"]
# # # homer_garage.foods = "eaten"
# # # print(homer_garage.paints)
# # # print(homer_garage.foods)

# # # FancyGarage will inherit everything from Garage

# inheritance
class FancyGarage(Garage): # so I say that this class blueprints use all methods and attributes from Garage class
    # Class Attribute
    gtype = "Fancy"
    # constructor method, called when we created object from this class
    total_travel = 0

    def __init__(self, cars, wines, color="Gold"):
        # I call my parent class constructor
        # Python 3.x+ we call our parent class constructor
        super().__init__(color, nails=2000)
        # self.color = color  # for color this would work, but we would have no nails!!
        self.cars = cars
        self.wines = wines
        print("Fancy Garage Created")
        self.pretty_print()

    # we have to give self argument for all methods inside classes
    def pretty_print(self):
        print(f"{self.gtype=}, {self.cars=}, {self.wines=}, {self.total_travel=}")
        return self

    def drive(self, distance):
        print(f"Driving {self.cars} a distance of {distance}")
        self.total_travel += distance
        return self  # Allows chaining of objects

    def get_longest_wine(self):
        wines_length = sorted(self.wines, key=len, reverse=True)
        return wines_length[0]


burns_garage = FancyGarage("Bentley", ["Rioja", "Temparillo", "Riesling"])
crusty_garage = FancyGarage("Rolls", ["Cabernet", "Cheap Wine"], "Bright Red")

# burns_garage.pretty_print()
burns_garage.add_nails(10).drive(20).drive(30).pretty_print().simple_print()
burns_garage.add_nails(50).drive(70).pretty_print()
# print(burns_garage.get_longest_wine())

# kent_garage = FancyGarage("Ferrari", wines="Cheap Wine",color="aquamarine")
# kent_garage.pretty_print()

# # print(burns_garage.cars)
# # print(burns_garage.wines)
# # burns_garage.gtype = "Rich"
# # burns_garage.pretty_print()
# # crusty_garage.pretty_print()


# # # crusty_garage.drive(60)
# # # crusty_garage.drive(160)
# # # crusty_garage.drive(20)
# # # crusty_garage.pretty_print()
# # # print(burns_garage.get_longest_wine())
# # # print(crusty_garage.get_longest_wine())
# # burns_garage.drive(100).drive(150).drive(80).pretty_print()
# # crusty_garage.drive(10).drive(25).pretty_print()
# # wilma_garage = Garage("pink")
# # wilma_garage.simple_print()
# # burns_garage.simple_print()
# # brockman_garage = FancyGarage("Ferrari", "Chuck Wine")
# # comic_guy_garage = FancyGarage("Ferrari", "Chuck Wine", "Bright Red")
# # comic_guy_garage.simple_print()  # can use Garage method
# # comic_guy_garage.pretty_print()  # can use Fancy Garage method
