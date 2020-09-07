# global variable here
dessert = "ice cream"

# defining function


def eat_food(dish):
    """
    Orders Food
    """
    # the above triple quoted string is documentation
    # printing is considered a side-effect
    print("Hello")
    print(f"Let's eat {dish}")
    print("Good bye")
    # returns None by default if not specified


eat_food("potatoes")
# DRY princips DO NOT REPEAT YOURSELF
eat_food("fish")

eat_food(dessert)
eat_food(9000)

print(dessert)

# returning values


def adder(a, b):
    result = a+b  # result will not be available outside adder
    # print(a+b)
    # print(result)
    # return a+b
    return result
 # result is not visible after indentation stops


my_val = adder(5, 10)
my_str = adder("alus", " muca")
print(my_val, my_str)

print(adder(adder(5, 20), 50))


def mult(a, b):
    # there could be some sanitization and validation here
    return a * b


big_result = mult(adder(5, 10), mult(2, 20))
print(big_result)


def big_calc(a, b, c):
    result = mult(adder(a, b), adder(b, c))  # (a+b)*(b+c)
    return result


result = big_calc(2, 3, 4)
print(result)

# we can add default values to parameters/argument

# sane defaults


def lazy_pow(a=10, b=2, pretty_print=False):
    result = a**b
    if pretty_print:
        print(f"Cool {a=} to the power of {b=} is {result}")

    return result


print(lazy_pow(5, 3))
print(lazy_pow(5))
print(lazy_pow())
print(lazy_pow(pretty_print=True))
# could change order but generally not recommended
print(lazy_pow(pretty_print=True, b=4, a=10))


def super_add(*argv):
    result = 0
    for arg in argv:
        print(arg)
        result += arg
    # return sum(argv)
    return result


# super_add(5, 10, "Valdis", True, 3.14)
result = super_add(5, 10, 20)
print(result)
# print(super_add("Valdis", " likes", " coding", "and food"))

my_list = [1, 2, 3]


def mod_list(arg_list):
    arg_list.append(10)
    arg_list += [20]  # turns out += for list is like extends in place
    # arg_list = arg_list + [30] this will creat a new list!!
    return my_list


print(my_list)
mod_list(my_list)
print(my_list)
another_list = [14, 30]
mod_list(another_list)
print(another_list)
