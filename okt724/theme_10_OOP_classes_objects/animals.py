# let's look at creating an Animal class
# Animals have a name, age, weight, color, what food they eat and how they sound
# of course there could be many more properties, but let's keep it simple

class Animal:
    # first we need to create a constructor
    # __init__ is a special method that is called when an object is created
    # in real life think of sane defaults for the properties
    def __init__(self, name, 
                 age=1, 
                 weight=1, 
                 color="Black", 
                 food="Cookies", 
                 sound="hmmmm", 
                 species="alien",
                 secret="I am an alien"):
        self.name = name
        self.age = age
        self.weight = weight
        self.color = color
        self.food = food
        self.sound = sound
        self.species = species
        # in OOP we have the concept of private properties
        # this is calle information hiding
        self.__secret = secret # this secret is private, because it starts with __
        # print("Object animal created with name", self.name)
        print(f"Object {species} created with name {self.name}")

    # we can define other so called dunder methods
    # full list is here: https://docs.python.org/3/reference/datamodel.html#special-method-names
    # __str__ is a special method that is called when we try to print the object
    # i can define my own
    # only requirement is that it returns a string
    def __str__(self):
        # i could do some formatting here
        return f"{self.name} is a {self.color} {self.species}"
    
    # let's define + operator for our class
    # for that we need to define __add__ method
    # this is a special method that is called when we use + operator
    def __add__(self, other):
        # here we can improvise
        # we will create a new species
        new_species = self.species + other.species
        # we will create a new name
        new_name = self.name + other.name
        # we will create a new color
        new_color = self.color + other.color
        # we will create a new food
        new_food = self.food, other.food
        # we will create a new sound
        new_sound = self.sound + other.sound
        # we will create a new weight
        new_weight = self.weight + other.weight
        # we will create a new age
        new_age = 0
        # we will create a new animal
        new_animal = Animal(new_name, new_age, new_weight, new_color, new_food, new_sound, new_species)
        return new_animal

    # let's create a method that will print the sound of the animal	
    def make_sound(self):
        # note how self is used to access the properties of the object
        # print(self.sound)
        print(f"{self.name} says {self.sound}")
        return self # again we return self so we can chain multiple methods

    # let's make a method to adjust weight
    def adjust_weight(self, weight_change, verbose=False):
        self.weight += weight_change
        # above is same as self.weight = self.weight + weight_change
        if verbose:
            self.print_weight() # i can call other methods from the class
            # note how I am calling a method that is defined later in the class
            # that is okay with Python, because it reads the whole class before executing it
        # if our methods do not return anything
        # then it is a good idea to return self
        # then we can chain multiple methods
        return self

    # let's make a method to print the weight
    def print_weight(self):
        print(f"{self.name} weighs {self.weight} kg")
        return self # again so we can chain multiple methods
    
    # let's make methods to manage secrets
    def get_secret(self):
        # i could do some validation here
        # and check authorization as well
        return self.__secret
    
    def set_secret(self, secret):
        # i could do some validation here
        # and check authorization as well
        self.__secret = secret


# let's make a dog
reksis = Animal("Reksis", 5, 10, "Brown", "Meat", "vau", "Dog")

# let's make a cat
winnie = Animal("Winnie", 3, 5, "White", "Fish", "meow", "Cat")

# let's make a cow
moo = Animal("Raibaļa", 4, 100, "Black", "Grass", "moo", "Cow")

# now let's make some sounds
# note how self is not passed as an argument! it is automatically passed by Python
reksis.make_sound() # Reksis says vau
winnie.make_sound() # Winnie says meow
moo.make_sound() # Raibaļa says moo

# i could change weight directly, but in OOP that is not a good practice
# moo.weight = 200
# winnie.weight += 2
# reksis.weight -= 1
# # now I could print them
# print(f"{moo.name} weighs {moo.weight} kg")
# print(f"{winnie.name} weighs {winnie.weight} kg")
# print(f"{reksis.name} weighs {reksis.weight} kg")
# better OOP approach would be to create methods for adjusting weight and print the weight

# let's adjust the weight of the animals
reksis.adjust_weight(2) # Reksis weighs 12 kg
reksis.print_weight() # Reksis weighs 12 kg
winnie.adjust_weight(-1) # Winnie weighs 4 kg
winnie.print_weight() # Winnie weighs 4 kg
moo.adjust_weight(10, verbose=True) # Raibaļa weighs 110 kg

# i have a lot of class attributes
# let's use named attributes
# let's make new animal
# how about a horse

horse = Animal(name="Zirgs", 
               age=7, 
               weight=200, 
               color="Brown", 
               food="Grass", 
               sound="neigh", 
               species="Horse")

# I can make an animal with some default values
# let's make a bird
bird = Animal("Pīlēns", species="pīle") # only name is required, species defaults to alien
bird.make_sound() # Pīlēns says hmmmm
# what species is the bird?
print(bird.species) 


# now since i can chain methods, I can do this
# let's adjust the weight of the bird
bird.adjust_weight(1).adjust_weight(2).adjust_weight(10).print_weight() # Pīlēna weighs 14 kg

# now let's do the horse
horse.adjust_weight(10).make_sound().adjust_weight(30).print_weight() # Zirgs weighs 240 kg

# print types of primitives
print(type(1)) # <class 'int'>
print(type(1.0)) # <class 'float'>
print(type("hello")) # <class 'str'>
print(type(True)) # <class 'bool'>

# now let's print some objects
print(type(reksis)) # <class '__main__.Animal'>
print(reksis) # Reksis is a Brown Dog # because we defined __str__ method
print(bird) # Pīlēns is a Black pīle

# let's create a chicken
chicken = Animal("Cālīte", species="chicken")
franken_chicken = bird + chicken # we can use + operator because we defined __add__ method
print(franken_chicken) 

# now how do I access the private property?
try:
    print(chicken.__secret) # AttributeError: 'Animal' object has no attribute '__secret
except AttributeError as e:
    print(e)

# now I have my getters
print(chicken.get_secret()) # I am an alien
# set different secret
chicken.set_secret("I am a kangaroo")
print(chicken.get_secret()) # I am a kangaroo

# now let's talk inheritance
# we would want to use Dog, Cat, Cow, Horse, Chicken classes
# let's make a Dog class that inherits Everything from Animal class

class Dog(Animal):
    # let's make our consturctor for Dog 
    # it will OVERRIDE the constructor of Animal
    # we will call the constructor of Animal with super()
    # if I had no extra parameters then I would not need a custom constructor
    def __init__(self, name, age=1, weight=1, color="Black", food="Cookies"):
        # now I will call the constructor of Animal
        # I will pass all the parameters
        # I will also pass the species as Dog
        # I will also pass the sound as vau
        super().__init__(name, age, weight, color, food, "vau", "Dog", "I am a dog")
        # new doggie created
        print(f"New doggie created")
        # i could even print myself here
        print(self) # will work because we defined __str__ method in Animal

    # make bark method that is unique to Dog
    # the rest stays the same
    def bark(self):
        print(f"{self.name} says {self.sound} {self.sound} {self.sound}")   
        return self
    
# let's make another Dog - we still have to pass vau and Dog to the constructor
rex = Dog("Rex", 10, 20, "Black", "Meat")
# print secret, ALL methods are inherited from Animal
print(rex.get_secret()) # I am a dog
# let's make Rex bark
rex.bark() # Rex says vau vau vau - this is unique to Dog, Animal doesn't have this method