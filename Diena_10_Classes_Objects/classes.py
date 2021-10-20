# # # # # # # # # # Python Class
# # # # # # # # # # Classes -> combine related data(properties)
# # # # # # # # # # Classes -> combine related funcionality(methods)
# # # # # # # # # # Objects - instances of class
# # # # # # # # # # Classes: blueprints
# # # # # # # # # # Objects: concrete realization of those blueprints
# # # # # # # # # # https://docs.python.org/3/tutorial/classes.html

# # # # # # # # # # how to store and process data about garage
# # # # # # # my_garage = ["paint can", "old papers", "rotting potatoes"]
# # # # # # # my_garage_d = {"paints": ["white", "black"], "food": "potatoes"}

# # # # # # # # # # empty class definition
# # # # # # 

class EmptyClass: #EmptyClass is just a name I made up, Classes start with Capital letter
    pass #pass is empty instruction


# # # # # # # # # # # # # # i create an  based on class blueprint

# empty_class_instance_object = EmptyClass() # creating an object
# print(type(empty_class_instance_object))
# # # # # # # # not great OOP style but i can add to an existing object
# empty_class_instance_object.paint = ["red", "blue"] # i can add arbitrary properties
# # # empty_class_instance_object.papers = ["Diena"]
# print(empty_class_instance_object.paint)

# # # # # print(empty_class_instance_object)
# # # # # # empty_class_instance_object
# empty_2 = EmptyClass() # so different object based on same EmptyClass
# empty_2.painter = "Picasso"
# empty_2.paint = "Guasha"
# print(empty_2.paint, empty_class_instance_object.paint)

# # # # # # # # # # the simplest empty class definition

# # # # # # # # # color = "Global color"


class House:
#     # class method example meaning method we can use without any objects created
#     # a library could be created by grouping class methods
#     @classmethod
#     def add(cls, a, b):
#         print(a,b,a+b, cls.all_house_prop)
#         return a+b

    all_house_prop = "Brick" # class property generally meant to be shared among instances
# # # # #     # do not share lists, dictionaries other mutable structures in class properties
    def print_house_prop(self):
        print(f"This house is built from {self.all_house_prop}")

# # #     # so __init__ has to be exact name for constructor to be called
# # #     # __init__ is so called double under - dunder method
    def __init__(self, color="green", nails=0): # constructor method called upon creation of object
#         # we add everything that we want done when we first create object from our class blueprints
        # self.color = color
        self.set_color(color) # this lets us performe extra validation
        self.nails = nails
        print(f"Initialized class instance with {self.color=} {self.nails=} {self.all_house_prop=}")

# # #     # regular methods, so method is a function declared in class definition
    def build_house(self):
        print(f"Building a house of {self.all_house_prop}")
        print(f"It's color will be {self.color}")
        return self

    def simple_print(self):
        print(f"Oh {self.color=} {self.nails=}")
        return self # this lets us chain our methods

    def set_color(self, new_color):
        # some verification on sane color here maybe
        self.color = new_color
        print(f"Changed color to {self.color}")
        return self




# # no houses yet, so this is class method
# print(House.add(5,11))

new_house = House()  # I create a new object from House class blueprint
new_house.print_house_prop()
print("This particular house is built from", new_house.all_house_prop)

another_house = House() # so each time we creat a new object __init__ is called for that object
another_house.print_house_prop()
another_house.all_house_prop = "Straw"
another_house.print_house_prop()
new_house.print_house_prop()

my_house = House() # creaing new object, in other class instance
print(my_house.color, my_house.nails)
# # print(my_house.all_house_prop)
# # my_house.build_house()
# # my_house.all_house_prop = "Clay" # not very OOP style to mutate
# # print(my_house.all_house_prop)
# # my_house.build_house() # i am calling a method, notice no self needed
summer_house = House(nails=500) # another object instance of same House class
summer_house.build_house()
third_house = House(color='red') # so self is not mentioned
print("Color", my_house.color)
# # third_house.build_house()
# # my_house.set_color("Orange")
# # print("Type", my_house.all_house_prop)
# # my_house.build_house()
# # # # # # # # # # # # # # i've created an object my_house based on House class blueprints
# # # # # # # print(type(my_house))
# # my_house.simple_print() # calling object's method

friends_house = House(color="blue", nails=1_000) # so new object based on same template
print(friends_house.color)
friends_house.simple_print().set_color("Violet").simple_print() # this works because simple_print return self
# # # class methods can return self if they have nothing useful to return

# # # # # # my_house.simple_print()
# # # # # # my_house.set_color("red")
# # # # # # my_house.simple_print()

# # # # # # # # # def inside class defines method (so function which is called by class or object)


class Garage:
    g_name = "just a garage" # not needed better to use sparingly we can run in some weird effects
# # # #     # classes constructor method called when we make a new object instance from this class
# # # #     # dunder syntax __init__
    def __init__(self, color="green", nails=0, name="My garage", nail_color="metal", secret="gold"):
        self.color = color
        self.nails = nails
        self.name = name
        self._nail_color = nail_color # convention of private do not touch properties
        self.__secret_stash = secret # private property whose name is mangled to outside
        print(f"Initialized class instance with {self.color=} {self.nails=} {self.name=}")

# #     # will be useful when we want to print our object
    def __str__(self): # this is responsible for string representation for print etc
        return f"Garage name: {self.name} color {self.color} nails: {self.nails} secret: {self.__secret_stash}"
    
    def __add__(self, other): # + operator overloading in other languages
        # return self.nails + other.nails
        new_color = self.color+"_"+other.color  # TODO make your color mixer
        new_nails = self.nails + other.nails
        return Garage(color=new_color, nails=new_nails) # i create new instance  with new attributes

    def __eq__(self, other): # so == will work
        # we come up some logic for object comparison
        return self.color == other.color and self.nails == other.nails # not a full comparison

# # #     # i could just live with __str__ no need for simple_print anymore
    def simple_print(self): # so this name i just made up myself
        print(f"Oh {self.name=} {self.color=} {self.nails=}")
        return self

    def add_nails(self, new_nails=1):
        # here could be code for checking validity of new nails
        self.nails += new_nails
        return self
    
    # so i can control how secret is to be given out
    def get_secret(self):
        # here i could check if secret should be given out and how
        return self.__secret_stash

    def set_secret(self, new_secret):
        self.__secret_stash = new_secret
        return self # for chaining

    def set_nails(self, new_nail_count=0):
        self.nails = new_nail_count
        return self

    def add(self, a ,b):
        print("just a utility for adding", a, b, a+b)
        return a+b

# #     # OOP getters method
    def get_current_nails(self):
        # formatting, data sanitation, so on
        return self.nails
# # # # end of our class definition, that is end of our blueprint


simple_garage = Garage()
print(simple_garage) # without __str__ definition not very useful
# print(simple_garage.__secret_stash) # this name has been m angled/sort of hidden
print(simple_garage.get_secret())
# # simple_garage.simple_print()
# # simple_garage.add_nails(15)
# # simple_garage.simple_print()
# # # print(simple_garage)
# # # # # print(simple_garage.__secret_stash) # so __property is renamed using name mangling
# # # # print(simple_garage.get_secret()) # using getter to obtain private information

# # print(simple_garage.g_name)
# # simple_garage.g_name = "Mana garāža"
# # print(simple_garage.g_name)
# # # # # # # to avoid always initalize by hand constructors were created

# # # # # # # # # create new objects based on class definition
homer_garage = Garage(color="yellow", nails=33)
flanders_garage = Garage(color="blue", nails=55, name="Property of Flanders")
print(homer_garage) #this works because we wrote our own __str__ method
print(flanders_garage)
mutant_garage = homer_garage + flanders_garage # we created our own __add__ method
mut_garage = homer_garage.__add__(flanders_garage) # same as above
print(mutant_garage)
print(mut_garage)
print(mut_garage == mutant_garage) # we defined our garage __eq__ should be True
print(mut_garage is mutant_garage) # two different objects , so False


# # # garage_obj_1 = Garage()
# # # garage_obj_2 = Garage()
# # # print("Objects have same contents based on our __eq__ method", garage_obj_1 == garage_obj_2) # to compare we'd need to define our __eq__ method
# # # print("Objects are actually same in memory?", garage_obj_1 is garage_obj_2) # main thing that garage object reside in diffent memory location
# # # # # # # # # two different objects from the same blueprint(class defintion)
# print(id(homer_garage), id(flanders_garage))
# # # # # # # print(homer_garage)
# # print(homer_garage._nail_color) # means for internal use but not private
# # # # so with return self i can chain the calls on the smae object

# mutant_garage.simple_print().add_nails(77).simple_print().set_nails(500).add_nails(10).simple_print()
homer_garage.add_nails(50).add_nails(170).simple_print() # so return self lets me chain methods
# # # # # # # # print(homer_garage.__secret_stash) # so __variables get name mangled
# # # # # # # # print(homer_garage.g_name)
# # # # # # # # print(Garage.g_name) 
# # # # # # # # # homer_garage.simple_print()
# # # # # # # # # flanders_garage.simple_print()
# millhouse_garage = Garage(color="purple")
# millhouse_garage.simple_print()
# print(millhouse_garage)

# # # # # # # # homer_garage.g_name = "Homer's garage"
# # # # # # # # homer_garage.simple_print()
# # # # # # # # print(Garage.g_name) 
# # # # # # # # print(homer_garage)
# # # # # # # # super_garage = homer_garage + flanders_garage
# # # # # # # # print(super_garage)
# simpsons_house = House(color="yellow")
# print(simpsons_house.color)
# # # # # # # # # simpsons_house.simple_print()
# print(simpsons_house)
# print(str(simpsons_house)) # i wouldneed to create __str__ method for House as well
# # # # # # # # # print(homer_garage.nails)
# # # # # # # # # print(homer_garage.get_current_nails())
# # # # # # # # # print(homer_garage.nails)

# # # # # # # # # millhouse_garage.nails
# # # # # # # # # millhouse_garage.add_nails(7)
# # # # # # # # # millhouse_garage.add_nails(17)
# # # # # # # # # millhouse_garage.simple_print()
# # # # millhouse_garage.add_nails(10).add_nails(25).simple_print()
# # # # # # # # # millhouse_garage.add_nails(5).simple_print()
# # # # millhouse_garage.set_nails(-50).add_nails(10).simple_print()

# # # # # # # # # # # homer_garage.paints = ["white", "black"]
# # # # # # # # # # # homer_garage.foods = "eaten"
# # # # # # # # # # # print(homer_garage.paints)
# # # # # # # # # # # print(homer_garage.foods)

# # # # # principle of inheritance
# # # # # # # # # # # FancyGarage will inherit everything from Garage

# # # # # # # # # inheritance
class FancyGarage(Garage): # so I say that this class blueprints use all methods and attributes from Garage class
#     # Class Attributes
    gtype = "Fancy"
    total_travel = 0

# # # # #     # constructor method, called when we created object from this class
# # # # # if i am not happy with parent constructor, notice the single tuple
# # # # # we do not put lists as default values to avoid trouble
    def __init__(self, cars=("Buggati",), wines=("Rioja","Temparillo"), color="Gold",name="Garage"):
#         # I call my parent class constructor
#         # Python 3.x+ we call our parent class constructor
        super().__init__(color, nails=2000, name=name) # so this will call Garage constructor
        # self.color = color  # for color this would work, but we would have no nails!!
        self.cars = list(cars) # converting to list since I want to mutate
        self.wines = list(wines)
        print("Fancy Garage Created")
        self.pretty_print()

# # # # #     # we have to give self argument for all methods inside classes
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

new_fancy_garage = FancyGarage()
print(new_fancy_garage)
print(new_fancy_garage.set_secret("silver").set_nails(55).simple_print().get_secret())
print(new_fancy_garage.total_travel)  # something new from FancyGarage

burns_garage = FancyGarage(["Bentley"], ["Rioja", "Temparillo", "Riesling"], color="Gray",name="Mr. Burn's Garage")
crusty_garage = FancyGarage(["Rolls"], ["Cabernet", "Cheap Wine"], "Bright Red", name="Crusty's Garage")

print(burns_garage)  # __str__ comes from Garage definition
burns_garage.pretty_print()
burns_garage.add_nails(10).drive(20).drive(30).pretty_print().simple_print()
burns_garage.add_nails(50).drive(70).pretty_print().simple_print().pretty_print()
# # print(burns_garage.get_longest_wine())

kent_garage = FancyGarage(["Ferrari"], wines=["Cheap Wine"],color="aquamarine")
kent_garage.pretty_print()

kent_garage.add(65,100)

# # # # # # # # # # print(burns_garage.cars)
# # # # # # # # # # print(burns_garage.wines)
# # # # # # # # # # burns_garage.gtype = "Rich"
# # # # # # # # # # burns_garage.pretty_print()
# # # # # # # # # # crusty_garage.pretty_print()


# # # # # # # # # # # crusty_garage.drive(60)
# # # # # # # # # # # crusty_garage.drive(160)
# # # # # # # # # # # crusty_garage.drive(20)
# # # # # # # # # # # crusty_garage.pretty_print()
# # # # # # # # # # # print(burns_garage.get_longest_wine())
# # # # # # # # # # # print(crusty_garage.get_longest_wine())
# # # # # # # # # # burns_garage.drive(100).drive(150).drive(80).pretty_print()
# # # # # # # # # # crusty_garage.drive(10).drive(25).pretty_print()
# # # # # # # # # # wilma_garage = Garage("pink")
# # # # # # # # # # wilma_garage.simple_print()
# # # # # # # # # # burns_garage.simple_print()
# # # # # # # # # # brockman_garage = FancyGarage("Ferrari", "Chuck Wine")
# # # # # # # # # # comic_guy_garage = FancyGarage("Ferrari", "Chuck Wine", "Bright Red")
# # # # # # # # # # comic_guy_garage.simple_print()  # can use Garage method
# # # # # # # # # # comic_guy_garage.pretty_print()  # can use Fancy Garage method

class SimpleGarage(Garage):
    # so __init__ from original Garage is used and everything else from Garage plus
    # plus we just add a new method
    def count_my_nails(self):
        return self.nails

maggies_garage = SimpleGarage()
maggies_garage.add_nails(33).simple_print()
print(maggies_garage.count_my_nails())
