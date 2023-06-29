# name my_module should be more descriptive

# usually we do not want to print anything in our modules but we can
# print("my_module.py is being imported")

my_variable = 10
my_list = [1,2,3,4,5]
my_string = "hello from Valdis"

def my_function(a, b):
    """This is my function docstring"""
    print("I am a function from my_module.py")
    return a + b

class MyClass:
    """This is my class docstring"""
    def __init__(self, name):
        self.name = name
        print(f"Hello from {self.name}")
    def __str__(self):
        return f"Hello I am {self.name}"
    def my_method(self):
        print(f"I am a method from {self.name}")

# let's talk about name guard

# idea is to check if module is run as a script/program or imported

# usually we do not want to print anything in our modules but we can

# this main could be called anything but main is a good name
def main():
    print("Running main function from my_module.py")
    # more stuff here could call other functions etc
    print("Finsihed running main function from my_module.py")

# has to be exactly like this
if __name__ == "__main__":
    # we do what we want to do when we run this file as a program
    print("my_module.py is being run as a program")
    # setup() # we can call our setup function
    main() # we can call our main function
    # cleanup() # we can call our cleanup function
    # of course I could have just written all the code here
    # i could also or only put tests under name guard
    assert my_function(10, 20) == 30
    assert my_function(5,0) == 5
else: # rare but we could do something when imported
    print("my_module.py is being imported")

# key idea do nothing except declare functions, classes, variables etc when imported