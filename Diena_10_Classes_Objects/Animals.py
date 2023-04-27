# I will store all the animal related classes in this file
# I can also store functions, variables, etc. in this file

def my_function():
    print("Hello from Animals.py")
    # this function is not related to any class, so it is a global function

class Animal:
    '''
    Documentation for Animal class
    We will use this class as a parent class for all the animals
    '''
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"Animal {self.name} is born. ")
        self.make_sound()

    # let's define string representation for this class
    # now we can print the object and it will print the string representation
    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def eat(self):
        print(f"{self.name} is eating")
        return self # since this method returns self, we can chain the method calls

    def drink(self):
        print(f"{self.name} is drinking")
        return self # since this method returns self, we can chain the method calls

    def sleep(self):
        print(f"{self.name} is sleeping")
        return self # since this method returns self, we can chain the method calls

    def years_pass(self, years=1):
        self.age += years # same as self.age = self.age + years
        print(f"{self.name} is now {self.age} years old")
        return self

    def make_sound(self):
        pass # we will implement this method in the child classes

class Dog(Animal):
    '''
    Documentation for Dog class
    '''
    # since I did not implement the __init__ method in the child class, it will use the parent class __init__ method
    def make_sound(self):
        print(f"{self.name} says Woof")
        return self # since this method returns self, we can chain the method calls

class Cat(Animal):
    '''
    Documentation for Cat class
    '''
    def make_sound(self):
        print(f"{self.name} says Meow")
        return self # since this method returns self, we can chain the method calls