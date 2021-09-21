# import math 
txt = "Quick brown fox"
mlist = [1, 2, 3, 9]

# typically a library would not have standalone lines like this
print("THis will run no matter what") # generally you'd want to avoid things that always run
print(txt, mlist)
# TODO move add to my utilities module


def add(a, b):
    print(f"adding {a=} and {b=}")
    return a+b

# my own sorted function, so possible namespace collision with built in sorted
# def sorted(seq):
#     return seq[::-1] # not sorted :)

# best to keep Classes in separate module
# big class could have its own file with name such as klase.py


class Klase:
    pass


class Garage:
    def __init__(self, gname="La biblioteca"):
        self.gname = gname
        print(f"Garage initialized! {self.gname=}")


# this will also on import
# print("Running my_mod")

# this will only run when not imported
if __name__ == "__main__":
    # typically you would put tests here or standalone program
    assert(add(2, 3) == 5) # assert will raise AssertError if eval is False
    print("This will run when my_mod.py is called normally")
    my_gar = Garage()
# else: # generally you do not need this else when importing
#     print("I was imported! My __main__ is", __name__)
