# print("Runs always") add only as a sanity check when testing
# defining a new function
my_favorite_drink = "beer"  # global variable

# we can add parameters to whom we give arguments


def eat(food, drink="kefirs"):  # drink is "kefirs" by default
    # print("Hello")
    print(f"Let's eat {food}")
    cal = calc_calories(food)
    print(f"{food=} and {cal=} not bad!")
    # best to avoid using globals directly
    print(f"Let's drink some {drink}")
    # print("Let's leave")
    # i could do more stuff inside eat function
    # food arguments stops living here
    # cal also stops living here
# function is finished here


def calc_calories(my_food):
    calories = len(my_food) * 100  # the more letters themore calories
    # print(f"Wow {calories=}") lets avoid side-effects
    # could even do return len(my_food) * 100
    return calories
# function stops and returns whatever is after return


def main():
    # the main action happens here
    favorite = "ice cream"
    eat(food="potatoes")
    eat("dessert", "coffee")
    eat(drink="milk", food="cookies")  # i can name the arguments
    # eat(5000)
    eat(favorite, "rum")


# if file is called as script (no komandrindras) tad shis būs True
if __name__ == "__main__":
    main()
