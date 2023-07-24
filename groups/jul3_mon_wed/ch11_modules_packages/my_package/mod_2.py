# so again module is just a file with python code with .py extension
# it sits in my_package directory
# so will generally be my_package/mod_1.py

def my_round(number, precision):
    # useless function - just for demo
    return round(number, precision)


# again if we want to test or run this standalone we can use main guard

if __name__ == "__main__":
    # let's assert that my_round(3.14159, 2) is 3.14
    print("Starting some tests")
    assert my_round(3.14159, 2) == 3.14