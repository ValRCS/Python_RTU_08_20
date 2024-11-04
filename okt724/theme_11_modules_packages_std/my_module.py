# this will be my module where I put functions that I want to use in my program
# i can also put variables in my module
# I can also put classes in my module

# print("My module is being imported!") # typically we do not want anything to run when we import a module

# some variables - less used than functions
my_favorite_foods = ['pizza', 'pasta', 'sushi', 'ramen', 'tacos']
my_number = 42 # answer to the ultimate question of life, the universe, and everything

# some functions
def print_fav_foods(food_list):
    print('My favorite foods are:')
    for food in food_list:
        print(food)

# some class
# you could store each class in separate module but it is not required
class MyPet:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def __str__(self):
        return f'{self.name} is a {self.species}'

# now let's use the functions and variables from my_module

# sometimes we want to use module as a program and not as a module
# solution is to use if __name__ == '__main__': block
# idea is to check if the module is being run as a program or being imported
# if it is being run as a program we can run some code
# typically thsi block is at the end of the module
# also it could be used for testing purposes

# so lets do a bit of testing

if __name__ == '__main__':
    print("My module is being run as a program!")
    print(my_favorite_foods) # ['pizza', 'pasta', 'sushi', 'ramen', 'tacos']
    # so we use my_module namespace to access the variables and functions in my_module

    # i can define some shopping list
    shopping_list = ['milk', 'eggs', 'bread', 'cheese', 'butter']
    # i can use the function from my_module to print my shopping list
    print_fav_foods(shopping_list)

    # i can use MyPet class from my_module
    my_pet = MyPet('Winnie', 'cat')
    print(my_pet) # Winnie is a cat
    # i could add some assertions here to test the functions and classes in my_module
    # assertions are used to check if the code is working as expected
    # if the assertion is True nothing happens
    # if the assertion is False an AssertionError is raised
    # assert 1 == 2 # AssertionError
    assert my_favorite_foods == ['pizza', 'pasta', 'sushi', 'ramen', 'tacos']
    # assert Winnie is the name of my pet
    assert my_pet.name == 'Winnie', 'Name of my pet is not Winnie!!!!'
    # again if assert is True nothing happens, which is the expected behavior
else: # rare but I could do something if the module is being imported
    print("I am being imported!") # typically we do not want anything to run when we import a module