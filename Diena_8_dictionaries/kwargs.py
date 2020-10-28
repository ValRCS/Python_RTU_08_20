# Passing variable number of named arguments to Function
# https://docs.python.org/3/whatsnew/3.8.html

def name_adder(**kwargs):
    for key, value in kwargs.items():
        print(key, value)


def adder(*args):
    for arg in args:
        print(arg)


# adder(1, 5, 6)


# name_adder(first="Valdis", likes="coding", loves="potatoes")


def get_me_everything(*args, **kwargs):  # order is important positional comes first!!
    for key, value in kwargs.items():
        print(key, value)
    for arg in args:
        print(arg)


# get_me_everything(5, 1, "urra", first="Valdis",
#                   likes="coding", loves="potatoes")
# get_me_everything()


def get_me_all(a, b, args="", **kwargs):  # order is important positional comes first!!
    for key, value in kwargs.items():
        print(key, value)
    for arg in args:
        print(arg)
    print(a, b)


# get_me_all(10, "Homer", 5, 20, greet="Jello", boss="Mr. Burns")
# get_me_all(10, "Homer", [1,2,35,6,'Doh'],greet="Jello", boss="Mr. Burns")
# get_me_all(10, "Homer", greet="Jello", boss="Mr. Burns")
# get_me_all()
# get_me_all("Doh", "Marge")
print()


