# # # # # # # # # # # # # # # # # Python Class
# # # # # # # # # # # # # # # # # Classes -> combine related data(properties)
# # # # # # # # # # # # # # # # # Classes -> combine related funcionality(methods)
# # # # # # # # # # # # # # # # # Objects - instances of class
# # # # # # # # # # # # # # # # # Classes: blueprints
# # # # # # # # # # # # # # # # # Objects: concrete realization of those blueprints
# # # # # # # # # # # # # # # # # https://docs.python.org/3/tutorial/classes.html

# print(type(5))  # even int is a class

# # # # # # # # # # # # # # # # # how to store and process data about garage
# my_garage = ["paint can", "old papers", "rotting potatoes"]
# my_garage_d = {"paints": ["white", "black"], "food": "potatoes"}

# # # # # # # # # # # # # # # # # empty class definition
# # # # # # # # # # # # # 

class EmptyClass: #EmptyClass is just a name I made up, Classes start with Capital letter
    pass #pass is empty instruction


# # # # # # # # # # # # # # # # # # # # # i create an  based on class blueprint

# empty_class_instance_object = EmptyClass() # creating an object
# print(type(empty_class_instance_object))
# print(empty_class_instance_object)  # shows location in memory by default
# # # # # # # # # # # # # # # # # # # # # not great OOP style but i can add to an existing object
# empty_class_instance_object.paint = ["red", "blue"] # i can add arbitrary properties
# empty_class_instance_object.papers = ["Diena"]
# print(empty_class_instance_object.paint)

# # # # # # # # # # # # # # # # # print(empty_class_instance_object)
# # # # # # # # # # # # # # # # # # empty_class_instance_object
# empty_2 = EmptyClass() # so different object based on same EmptyClass
# empty_2.painter = "Picasso"
# empty_2.paint = "Guasha"
# print(empty_2.painter, empty_2.paint)
# print(empty_2.paint, empty_class_instance_object.paint)

# # # # # # # # # # # # # # # # # the simplest empty class definition

# # # # # # # # # # # # # # # # color = "Global color"
# # # # # no_house_sorry = House() # cant create object before class definition

class House:
# # # # # # # #     # class method example meaning method we can use without any objects created
# # # # # # # #     # a library could be created by grouping class methods
    @classmethod # this works even when no objects are made from House class
    def add(cls, a, b):
        print(a,b,a+b)
        # i can also access class properties
        print(cls.all_house_prop, cls.chimney)
        return a+b

# #     # regular method
    def mult(self, a, b):
        return a*b  #not self since we need something

    all_house_prop = "Brick" # class property generally meant to be shared among instances
    chimney = "metal"
# # # # # # # # # # # #     # do not share lists, dictionaries other mutable structures in class properties
    def print_house_prop(self):  # self refers to concrete object - this is other languages
        print(f"This house is built from {self.all_house_prop} and its chimney is from {self.chimney}")

# # # # # # # # # #     # so __init__ has to be exact name for constructor to be called
# # # # # # # # # #     # __init__ is so called double under - dunder method
    def __init__(self, color="green", nails=0): # constructor method called upon creation of object
# # # # #         # we add everything that we want done when we first create object from our class blueprints
        print("Starting House construction - constructor method is called")
        # self.color = color # create a new class property/attribute
        self.set_color(color) # this lets us performe extra validation
        self.nails = nails
        print(f"Initialized class instance with {self.color=} {self.nails=} {self.all_house_prop=}")
        self.print_house_prop()  # i can call methods from class definition
        print("INIT DONE *******")

# # # # # # # # # #     # regular methods, so method is a function declared in class definition
    def build_house(self):
        print(f"Building a house of {self.all_house_prop}")
        print(f"It's color will be {self.color}")
        print(f"Using {self.nails} nails")
        print("House built")
        return self  # if method has nothign good to return then return self will let call the same object methods again

    def simple_print(self):
        print(f"Oh {self.color=} {self.nails=}")
        return self # this lets us chain our methods

# # so called setter method set_color is arbitrary name
    def set_color(self, new_color):
        # some verification on sane color here maybe
        # you could place if statements here
        self.color = new_color
        print(f"Changed color to {self.color}")
        return self

    def set_nails(self, new_nails):
        self.nails = new_nails
        print(f"Changed nails to {self.nails}")
        return self

    def get_nails(self):
        # some verification logic
        return self.nails



# # # # # # # # # no houses yet, so this is class method
# print(House.add(5,11)) # could be useful for library
# # # # print(House.mult(43,52)) # not possible since this is not a static class method

# new_house = House()  # I create a new object from House class blueprint, 
# print(new_house.mult(5,1541)) # this is a regular method
# # # # # # # # # in above line __init__ will be called if one exists
# print(new_house.all_house_prop)  # I can access class property from object
# print(new_house.chimney) # I can access another class property from object as well
# new_house.print_house_prop() #i can access something inside object through method
# print("This particular house is built from", new_house.all_house_prop)  # direct access to property
# print("This house chimney is made from", new_house.chimney)

# another_house = House() # so each time we creat a new object __init__ is called for that object
# print(another_house.chimney)
# another_house.print_house_prop()
# another_house.all_house_prop = "Straw"
# another_house.print_house_prop()  # the objects properties will be different now
# new_house.print_house_prop()
# new_house.chimney = "Fireproof bricks"
# new_house.print_house_prop()

# # # # # # # # # two different objects from same class blueprint now have different properties
# # # # # # # # print(new_house.all_house_prop, another_house.all_house_prop) 

# # # # # # # # # third object from same blueprint / class definition
# my_house = House(color="red", nails=9_000) # creaing new object, in other class instance
# print(my_house.color, my_house.nails)
# # my_house.color = "blue" # i can change the color of my house
# # # # # # # print(my_house.all_house_prop)
# # # my_house.build_house()

# ## METHOD CHAINING
# # if method returns self then we can chain methods
# my_house.build_house().build_house().build_house().print_house_prop()  #possible because of return self
# # # # # # # # # # # # my_house.all_house_prop = "Clay" # not very OOP style to mutate
# # # # # # # # # # # # print(my_house.all_house_prop)
# # # # # # # # # # # # my_house.build_house() # i am calling a method, notice no self needed
# # summer_house = House(nails=500) # another object instance of same House class
# # summer_house.set_color("yellow").set_nails(1000).build_house().simple_print() 
# # # this above works because of return self in all methods
# # # # # # my_house.simple_print()
# # # # # # # summer_house.build_house()
# # # # # # # third_house = House(color='red') # so self is not mentioned
# # # # # # # print("Color", my_house.color)
# # # # # # # # # third_house.build_house()
# # # # # # # # # my_house.set_color("Orange")
# # # # # # # # # print("Type", my_house.all_house_prop)
# # # # # # # # # my_house.build_house()
# # # # # # # # # # # # # # # # # # # # # i've created an object my_house based on House class blueprints
# # # # # # # # # # # # # # print(type(my_house))
# # # # # # # # # my_house.simple_print() # calling object's method

# # # # # # # friends_house = House(color="blue", nails=1_000) # so new object based on same template
# # # # # # # print(friends_house.color)
# # # # # # # friends_house.simple_print().set_color("Violet").simple_print() # this works because simple_print return self
# # # # # # # # # # class methods can return self if they have nothing useful to return

# # # # # # # # # # # # # my_house.simple_print()
# # # # # # # # # # # # # my_house.set_color("red")
# # # # # # # # # # # # # my_house.simple_print()

# # # # # # # # # # # # # # # # def inside class defines method (so function which is called by class or object)


class Garage:
    g_name = "just a garage" # not needed better to use sparingly we can run in some weird effects
# # # # # # # #     # classes constructor method called when we make a new object instance from this class
# # # # # # # #     # dunder syntax __init__
    def __init__(self, 
                 color="green", 
                 nails=0, 
                 name="My garage", 
                 nail_color="metal", 
                 secret="gold"):
        self.color = color
        self.nails = nails
        self.name = name
        self._nail_color = nail_color # convention of private do not touch properties
        self.__secret_stash = secret # private property whose name is mangled to outside
        print(f"Initialized class instance with {self.color=} {self.nails=} {self.name=}")

# # # # # # # # #     # will be useful when we want to print our object
    def __str__(self): # this is responsible for string representation for print etc
        return f"Garage name: {self.name} color {self.color} nails: {self.nails} secret: {self.__secret_stash}"
    
    def __add__(self, other): # + operator overloading in other languages
        # return self.nails + other.nails
        new_color = self.color+"_"+other.color  # TODO make your color mixer
        new_nails = self.nails + other.nails
        return Garage(color=new_color, nails=new_nails) # i create new instance  with new attributes

    def __eq__(self, other): # so == will work
        # we come up our own logic for object comparison
        return self.color == other.color and self.nails == other.nails # not a full comparison

# # # # # # # # #     # i could just live with __str__ no need for simple_print anymore
    def simple_print(self): # so this name i just made up myself
        print(f"Oh {self.name=} {self.color=} {self.nails=}")
        return self

    def add_nails(self, new_nails=1):
        # here could be code for checking validity of new nails
        self.nails += new_nails
        return self
    
# # # # # #     # so i can control how secret is to be given out
    def get_secret(self):
        print("Internal method for getting secret")
        # here i could check if secret should be given out and how
        return self.__secret_stash

    def set_secret(self, new_secret):
        self.__secret_stash = new_secret
        return self # for chaining

    def set_nails(self, new_nail_count=0):
        self.nails = new_nail_count
        return self

#     @classmethod # decorator
#     def add(cls, a ,b):
#         """
#         add method just for fun, has nothing to do with other Garage class properties
#         in real life we would try to avoid this
#         """
#         print("just a utility for adding", a, b, a+b)
#         print(f"Also I can see class properites such as {cls.g_name}")
#         return a+b

# # # # # #     # OOP getters method
    def get_current_nails(self):
        # formatting, data sanitation, so on
        return self.nails
# # # # # # # # # # # end of our class definition, that is end of our blueprint

# Garage.add(30,15) # this is a class method

simple_garage = Garage()
print(simple_garage) # without __str__ definition not very useful
print(simple_garage._nail_color)  # accesible property still, just means meant for internal use
try:
    print(simple_garage.__secret_stash) # this name has been mangled/sort of hidden
except AttributeError as e:
    print(e)
    print("Secret is hidden")
# # # turns out __secret_stash is private property, hidden vai name mangling
print(simple_garage.get_secret())  # getter method
# i can change secret with setter set_secret
simple_garage.set_secret("silver")
print(simple_garage.get_secret())  # getter method
simple_garage.simple_print()
simple_garage.add_nails(15)
simple_garage.add_nails(12)
simple_garage.add_nails() # adds a single nail because default value is 1

# simple_garage.simple_print()
print(simple_garage)  # will look nice with __str__ defined
# # # # # # # # # # # # print(simple_garage.__secret_stash) # so __property is renamed using name mangling
# # # # # # # # # # # print(simple_garage.get_secret()) # using getter to obtain private information

# # # # # # # # # print(simple_garage.g_name)
# # # # # # # # # simple_garage.g_name = "Mana garāža"
# # # # # # # # # print(simple_garage.g_name)
# # # # # # # # # # # # # # to avoid always initalize by hand constructors were created

# # # # # # # # # # # # # # # # create new objects based on class definition
homer_garage = Garage(color="yellow", nails=33, name="Homer's garage")
flanders_garage = Garage(color="blue", nails=55, name="Property of Flanders")
print(homer_garage) #this works because we wrote our own __str__ method
print(flanders_garage)
mutant_garage = homer_garage + flanders_garage # we created our own __add__ method
mut_garage = homer_garage.__add__(flanders_garage) # same as above
print(mutant_garage)
print(mut_garage)
print("Two objects have same contents? ", mut_garage == mutant_garage) # we defined our garage __eq__ should be True
print("Two objects have same address in memory - are actually same object?", mut_garage is mutant_garage) # two different objects , so False
print("Valdis".__add__("ssss")) # this is how we can add strings to strings usually we would use +

## Full list of dunder methods
# https://docs.python.org/3/reference/datamodel.html#special-method-names
# # # # # # # # # # garage_obj_1 = Garage()
# # # # # # # # # # garage_obj_2 = Garage()
# # # # # # # # # # print("Objects have same contents based on our __eq__ method", garage_obj_1 == garage_obj_2) # to compare we'd need to define our __eq__ method
# # # # # # # # # # print("Objects are actually same in memory?", garage_obj_1 is garage_obj_2) # main thing that garage object reside in diffent memory location
# # # # # # # # # # # # # # # # two different objects from the same blueprint(class defintion)
# # # # # # # # print(id(homer_garage), id(flanders_garage))
# # # # # # # # # # # # # # print(homer_garage)
# # # # # # # # # print(homer_garage._nail_color) # means for internal use but not private
# # # # # # # # # # # so with return self i can chain the calls on the smae object

# mutant_garage.simple_print().add_nails(77).simple_print().set_nails(500).add_nails(10).simple_print()
homer_garage.add_nails(50).add_nails(170).simple_print() # so return self lets me chain methods
# # # # # # homer_garage.set_secret("secret_stash").simple_print()
# # # # # # print(homer_garage.get_secret())
# # # # # # # # # # # # # # # print(homer_garage.__secret_stash) # so __variables get name mangled
# # # # # # # # # # # # # # # print(homer_garage.g_name)
# # # # # # # # # # # # # # # print(Garage.g_name) 
# # # # # # # # # # # # # # # # homer_garage.simple_print()
# # # # # # # # # # # # # # # # flanders_garage.simple_print()


millhouse_garage = Garage(color="purple", nails=100, name="Millhouse's garage")
millhouse_garage.simple_print()
# # # # # I can chain those methods which return self
# # # # millhouse_garage.add_nails(750).simple_print().add_nails(200).simple_print()
# # # # print(millhouse_garage)

# # # # millhouse_garage.add(4,14)

# # # # # # # # # # # # # # # homer_garage.g_name = "Homer's garage"
# # # # # # # # # # # # # # # homer_garage.simple_print()
# # # # # # # # # # # # # # # print(Garage.g_name) 
# # # # # # # # # # # # # # # print(homer_garage)
# # # # # # # # # # # # # # # super_garage = homer_garage + flanders_garage
# # # # # # # # # # # # # # # print(super_garage)
# # # simpsons_house = House(color="yellow")
# # # print(simpsons_house.color)
# # # # # # # # # # # # # # # simpsons_house.simple_print()
# # # # # # # # print(simpsons_house)
# # # # # # # # print(str(simpsons_house)) # i wouldneed to create __str__ method for House as well
# # # # # # # # # # # # # # # # print(homer_garage.nails)
# # # # # # # # # # # # # # # # print(homer_garage.get_current_nails())
# # # # # # # # # # # # # # # # print(homer_garage.nails)

# # # # # # # # # # # # # # # # millhouse_garage.nails
# # # # # # # # # # # # # # # # millhouse_garage.add_nails(7)
# # # # # # # # # # # # # # # # millhouse_garage.add_nails(17)
# # # # # # # # # # # # # # # # millhouse_garage.simple_print()
# # # # # # # # # # # millhouse_garage.add_nails(10).add_nails(25).simple_print()
# # # # # # # # # # # # # # # # millhouse_garage.add_nails(5).simple_print()
# # # # # # # # # # # millhouse_garage.set_nails(-50).add_nails(10).simple_print()

# # # # # # # # # # # # # # # # # # homer_garage.paints = ["white", "black"]
# # # # # # # # # # # # # # # # # # homer_garage.foods = "eaten"
# # # # # # # # # # # # # # # # # # print(homer_garage.paints)
# # # # # # # # # # # # # # # # # # print(homer_garage.foods)

# # # # # # # # # # # # principle of inheritance
# # # # # # # # # # # # # # # # # # FancyGarage will inherit everything from Garage

# # # # # # # # # # # # # # # # inheritance
class FancyGarage(Garage): # so I say that this class blueprints use all methods and attributes from Garage class
# #     # Class Attributes
    gtype = "Fancy"  # gtype could be any other name
    total_travel = 0

# # # # # # # # # # # #     # constructor method, called when we created object from this class
# # # # # # # # # # # # if i am not happy with parent constructor, notice the single tuple
# # # # # # # # # # # # we do not put lists as default values to avoid trouble
    def __init__(self, cars=("Buggati",), wines=("Rioja","Temparillo"), color="Gold",name="Garage"):
# #         # I call my parent class constructor
# #         # Python 3.x+ we call our parent class constructor
        super().__init__(color, nails=2000, name=name) # so this will call Garage constructor
        # self.color = color  # for color this would work, but we would have no nails!!
        self.cars = list(cars) # converting to list since I want to mutate
        self.wines = list(wines)
        print("Fancy Garage Created")
        self.pretty_print()

# # # # # # # # # # # #     # we have to give self argument for all methods inside classes
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

new_fancy_garage = FancyGarage(name="Cool name")
# print(new_fancy_garage) # so everything from Garage works! we inherited all methods and attributes
print(new_fancy_garage.set_secret("silver").set_nails(55).simple_print().get_secret())
new_fancy_garage.drive(100).drive(200).drive(300).pretty_print()
print(new_fancy_garage.total_travel)  # something new from FancyGarage

burns_garage = FancyGarage(["Bentley"], ["Rioja", "Temparillo", "Riesling"], color="Gray",name="Mr. Burn's Garage")
crusty_garage = FancyGarage(["Rolls","Ferrari"], ["Cabernet", "Cheap Wine"], "Bright Red", name="Crusty's Garage")

# print(burns_garage)  # __str__ comes from Garage definition
# burns_garage.pretty_print()  # method from FancyGarage class definition
# burns_garage.add_nails(10).drive(20).drive(30).pretty_print().simple_print()
# burns_garage.add_nails(50).drive(70).pretty_print().simple_print().pretty_print()
# # # # # # # # print(burns_garage.get_longest_wine())

# kent_garage = FancyGarage(["Ferrari"], wines=["Cheap Wine"],color="aquamarine")
# kent_garage.pretty_print()

# kent_garage.add(65,100)

# # # # # # # # # # # # # # # # # print(burns_garage.cars)
# # # # # # # # # # # # # # # # # print(burns_garage.wines)
# # # # # # # # # # # # # # # # # burns_garage.gtype = "Rich"
# # # # # # # # # # # # # # # # # burns_garage.pretty_print()
# # # # # # # # # # # # # # # # # crusty_garage.pretty_print()


# # # # # # # # # # # # # # # # # # crusty_garage.drive(60)
# # # # # # # # # # # # # # # # # # crusty_garage.drive(160)
# # # # # # # # # # # # # # # # # # crusty_garage.drive(20)
# # # # # # # # # # # # # # # # # # crusty_garage.pretty_print()
# # # # # # # # # # # # # # # # # # print(burns_garage.get_longest_wine())
# # # # # # # # # # # # # # # # # # print(crusty_garage.get_longest_wine())
# # # # # # # # # # # # # # # # # burns_garage.drive(100).drive(150).drive(80).pretty_print()
# # # # # # # # # # # # # # # # # crusty_garage.drive(10).drive(25).pretty_print()
# # # # # # # # # # # # # # # # # wilma_garage = Garage("pink")
# # # # # # # # # # # # # # # # # wilma_garage.simple_print()
# # # # # # # # # # # # # # # # # burns_garage.simple_print()
# # # # # # # # # # # # # # # # # brockman_garage = FancyGarage("Ferrari", "Chuck Wine")
# # # # # # # # # # # # # # # # # comic_guy_garage = FancyGarage("Ferrari", "Chuck Wine", "Bright Red")
# # # # # # # # # # # # # # # # # comic_guy_garage.simple_print()  # can use Garage method
# # # # # # # # # # # # # # # # # comic_guy_garage.pretty_print()  # can use Fancy Garage method

# class SimpleGarage(Garage):
#     # so __init__ from original Garage is used and everything else from Garage plus
#     # plus we just add a new method so really it is Garage + one new method
#     def count_my_nails(self):
#         return self.nails

# maggies_garage = SimpleGarage(name="Maggie's Garage") # so we can use Garage constructor
# maggies_garage.add_nails(33).simple_print()
# print(maggies_garage.count_my_nails())

# class GPS:
#     def __init__(self, lat=56.67, lon=24.4):
#         self.lat = lat
#         self.lon = lon

# class Auto:
#     # remember default sequence types should be tuples not lists!
#     def __init__(self, color="Black", gps_list=()):
#         self.color = color
#         self.gps_list = list(gps_list)  # use list if i need to add new GPS

#     def add_gps(self, gps: GPS):
#         self.gps_list.append(gps)
#         return self
    
#     def print_gps(self):
#         print("Printing GPS")	
#         for gps in self.gps_list:
#             print(gps.lat, gps.lon)
#         return self
    
# toyota = Auto("Red", (GPS(56.67, 24.4), GPS(58.67, 34.4)))

# print(toyota.gps_list[0].lat, toyota.gps_list[1].lat)
# toyota.add_gps(GPS(66.67, 14.4)).print_gps()

# toyota.add_gps(GPS(86.67, 24.4)).add_gps(GPS(8.67, 34.4)).print_gps()

# vw = Auto()
# vw.print_gps()
# my_new_gps = GPS(56.67, 24.4)
# vw.add_gps(my_new_gps).print_gps()