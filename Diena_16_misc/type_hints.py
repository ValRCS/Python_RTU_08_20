# again Python interpreter ignores type hints,
# the hints are for type checking tools
def add(a: int, b: int) -> int:
    return a+b

def mult(a:int,b:int) -> int:
    """
    My Multiplication function
    """
    return a*b
print(add(6, 10))
print(mult(6, 10))
# print(add("Valdis ", "Līga"))
