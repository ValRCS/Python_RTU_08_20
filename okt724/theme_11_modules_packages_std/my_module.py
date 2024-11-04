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