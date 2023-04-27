# I will import the Animal class from Animals.py

from Animals import Animal # imports specific class from the module
import Animals # this will import the whole module
import my_utilities as myu 
# this will import the whole module from my_utilities.py with alias myu

generic_animal = Animal("Generic Animal", 10)

generic_animal.eat()
generic_animal.drink()
generic_animal.sleep()
generic_animal.make_sound()  # nothing happens, because the method is not implemented in the parent class

my_doggie = Animals.Dog("Rex", 5)
my_doggie.eat()

my_kitty = Animals.Cat("Darcy", 1)
my_other_kitty = Animals.Cat("Winnie", 1)
my_kitty.years_pass(5)
my_kitty.years_pass() # default value is 1

print(myu.add(5, 6))
Animals.my_function() # this is how we call a function from a module

# we can chain the method calls, because the methods return self
my_kitty.eat().drink().sleep().years_pass(5).make_sound()