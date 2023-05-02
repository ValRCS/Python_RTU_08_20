MAGIC_PI = 3.14  # capitals indicates constants by conventions


def subadd(a, b):
    print(f"Subadd {a-b+100}")
    return a-b+100


def subprint(t):
    print(f"Sub {t}")


def badprint():
    print("I do not want to use this!")

# i could add main guard here
if __name__ == "__main__":
    # could do some tests here
    assert(subadd(2, 3) == 99) # assert will raise AssertError if eval is False
    print("This will run when sub_utils.py is called normally")