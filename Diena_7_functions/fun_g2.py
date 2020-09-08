# print("Runs always") add only as a sanity check when testing
# defining a new function
my_favorite_drink = "beer"  # global variable

# we can add parameters to whom we give arguments


def eat(food, drink="kefirs"):  # drink is "kefirs" by default
    # print("Hello")
    print(f"Let's eat {food}")
    # best to avoid using globals directly
    print(f"Let's drink some {drink}")
    # print("Let's leave")
    # i could do more stuff inside eat function
    # food arguments stops living here
# function is finished here


# eat("potatoes")
# eat("ice cream Sunday")
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
