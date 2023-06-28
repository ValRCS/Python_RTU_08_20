# so this is meant for importing from the same folder
# but it is just a regular .py file


# print("Oh I am a module and I am being imported") 
# usually we do not want to print anything when importing
my_data = 100
my_list = [1, 2, 3, 4, 5]
my_string = "Hello from my_module.py"

def my_function(a, b):
    """This is a function that will add two numbers"""	
    return a + b

def another_function(a, b):
    """This is a function that will multiply two numbers"""	
    return a * b

# i could have a class defined here
class Car:
    """This is a class that represents a car"""
    def __init__(self, make, model):
        print(f"Car.__init__({make}, {model}) is being called")
        self.make = make
        self.model = model


# we can use main guard to test our module or run it as a program
if __name__ == "__main__":
    # so nothing here will run when imported!
    print("Oh I am a module and I am being run as a program")
    print("I can do anything I want here")
    print("I can even call my_function(10, 20)")
    print(my_function(10, 20))
    assert my_function(10, 20) == 30
else: # rarely used
    print("Oh I am a module and I am being imported")
    # usually we want nothing to happen when imported