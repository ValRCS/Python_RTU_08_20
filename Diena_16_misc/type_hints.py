# again Python interpreter ignores type hints,
# the hints are for type checking tools
def add(a: int, b: int) -> int:
    return a+b


print(add(6, 10))
print(add("Valdis ", "Līga"))
