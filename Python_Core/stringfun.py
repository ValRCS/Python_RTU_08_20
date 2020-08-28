print("Fun with Python")
food = "potatoe"
# ar f strings pieliekot = after variable we get name of the name and value
print(f"{food=}")
drink = "milk"
print(food[1])  # we want to print p, but we o because index starts with 0
print(food[0])
print(len(food))
print(food[len(food) - 1])  # not Pythonic
print(food[-1])  # this is Pythonic use this!
for c in food:
    print(c, end=" :: ")
print(food[:3])
print(food[2:4])
print(food, food[3:])
print(food, food[::2])
print(food, food[3::2])
my_food = "kartupelis"
print(my_food, my_food[3:8:2])
print(my_food, my_food[::-1])  # Pythonic way of reversing string

print(my_food.find("p"))
# my_food[5] = "m"  # strings are immutable so this will not work
# to change strings we need to make new ones
new_food = my_food.replace("p", "m")
print(new_food)
another_food = my_food[:5] + "m" + my_food[6:]
print(another_food)
full_food = "liels " + my_food
print(full_food)
print(full_food.count("l"))
# we could our own count
print("k" in full_food)  # we can find if letter is in our str
count = 0
for c in full_food:
    if c == "l":
        count += 1
print(f"Letter l can be found {count=}")
print("Valdis" > "Voldemars")
print("a" > "o")
print(ord("a"), ord("o"), ord('ā'))
