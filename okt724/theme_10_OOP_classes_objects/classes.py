# Python supports object-oriented programming (OOP) and classes.
# Classes are used to create new objects and define their properties and methods.
# The main idea is to combine data and functionality and wrap it inside a class.
# we use that class as blueprint to create new objects - instances of that class.

# where would this be useful?

# let's say I want to create a program that manages a garage
# garage has a name, some tools, some cars, some employees
# how would we store this information?

# we could use a list, but that is not very descriptive

# better would be to use dictionary

# example
# my_garage = {
#     "name": "My Garage",
#     "tools": ["hammer", "screwdriver", "wrench"],
#     "cars": ["BMW", "Audi", "Mercedes"],
#     "employees": ["John", "Jane", "Joe"],
#     "prices": [100, 120, 125] # those would represent hourly wages
# }

# let's say I want to add a new car to the garage
# i could do it by hand
# my_garage["cars"].append("Toyota") # but that is not very descriptive
# # i need to know two things, that I have a key called "cars" and that I need to append to it
# # what if I forget that I have a key called "cars" and I try to append to a key that doesn't exist?
# # let's say I want to calculate how much would 6 hours of work cost me from John
# # i would need to know that I have a key called "prices" and that I need to multiply the price by 6
# # what if I forget that I have a key called "prices" and I try to multiply by a key that doesn't exist?

# # i could have made a function that does that for me
# def add_car(garage, car):
#     garage["cars"].append(car)

# def calculate_price(garage, employee, hours):
#     price = garage["prices"][garage["employees"].index(employee)]
#     return price * hours

# print(my_garage)
# add_car(my_garage, "Toyota")
# print(my_garage)
# print(calculate_price(my_garage, "John", 6))


# this works, but functions have a tendency to slip away from the data they are supposed to work with

# instead we have object-oriented programming
# we can create a class that represents a garage


class SuperSimpleGarage:
    pass # this is empty class, it doesn't do anything

# simple_garage = SuperSimpleGarage() # this creates an instance of the class SuperSimpleGarage
# print(simple_garage) # <__main__.SuperSimpleGarage object at 0x7f8d3b5c4b50>
# # i could add some properties to the object
# simple_garage.name = "Žaņa garāža"
# print(simple_garage.name) # Žaņa garāža
# this is a bit of pain, because I need to know what properties the object has

# let's make a real Garage - it will be individual garage with its own name, tools, cars, employees and prices

class Garage:
    # __init__ is a special method that is called when an object is created
    # self is a reference to the object itself (not class!)
    def __init__(self, name, cars=None, tools=None, nails=0):
        self.name = name
        # we will pass on the default values for cars and tools and nails
        self.cars = cars
        self.tools = tools
        self.nails = nails
        print("Object garage created with name", self.name)

    # let's create a method (function that is part of the class) that adds a car to the garage
    def add_car(self, car):
        if self.cars is None: # if cars is None, we will create an empty list
            self.cars = []
        self.cars.append(car)

    # let's create a method that will print my car collection
    def print_cars(self):
        if self.cars is None:
            print("No cars in the garage")
        else:
            print("Cars in the garage", self.cars)

# let's create our first garage
my_garage = Garage("Mana garāža") # Object garage created with name Mana garāža
neighbor_garage = Garage("Kaimiņa garāža") # Object garage created with name Kaimiņa garāža
# i can print these properties
print(my_garage.name) # Mana garāža
print(neighbor_garage.name) # Kaimiņa garāža

# let's print my car collection
my_garage.print_cars() # No cars in the garage
# let's add a Golf to my garage
my_garage.add_car("Golf")
my_garage.print_cars() # Cars in the garage ['Golf']
# let's add a BMW to my garage
my_garage.add_car("BMW")
my_garage.print_cars() # Cars in the garage ['Golf', 'BMW']

# how about our Neighbor's garage?
neighbor_garage.print_cars() # No cars in the garage
# let's add a Mercedes to Neighbor's garage
neighbor_garage.add_car("Mercedes")
neighbor_garage.print_cars() # Cars in the garage ['Mercedes']

# we have two objects that are instances of the class Garage
# both have some data and some methods that work with that data
