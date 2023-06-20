# functions can also return values

# consider a function print_calculation
# it prints the result of a calculation
# but it does not return the result
# so we cannot use it in other calculations

def print_calculation(a, b):
    print(f"{a} + {b} = {a + b}")
    # for one we might not want to print but return
    # if we do not write return Python will return None

result = print_calculation(2, 3)
print(result) # None

# we can also return values from functions
# we use return keyword

def return_calculation(a, b):
    # we could do more processing here
    # also name of function should be more descriptive
    # for example add_numbers
    return a + b

result = return_calculation(2, 3)
print(result) # 5 # so we can use result in other calculations as well

# in Python functions are first class citizens so we can assign them to variables
# we can pass them as arguments to other functions - as well
add = return_calculation # notice no () we are not calling the function
# so add is a shortcut to return_calculation
print(add(2, 3)) # 5

# let's do a multiplication function
def multiply(a, b): 
    return a * b

# with return I can nest functions
print(multiply(add(2, 3), multiply(10,2))) # 100

# let's make a function that multiples list of numbers
def multiply_list(numbers):
    result = 1 # we start with 1 since we will be multiplying
    for number in numbers:
        result *= number
    return result

print(multiply_list([2,30,4,5])) # 1200

# how about returning multiple values?
# we can return a tuple - tuple is more or less immutable list

def return_multiple(a, b):
    return a + b, a * b, a / b

print(return_multiple(2, 3)) # (5, 6, 0.6666666666666666)

# could have also returned a list
def return_multiple_list(a, b):
    return [a + b, a * b, a / b]

result_list = return_multiple_list(2, 3)
print(result_list) # [5, 6, 0.6666666666666666]

# of course we could return anything say a string
def return_string(a, b):
    # i could do more processing here
    return f"{a} + {b} = {a + b}"

my_formated_string = return_string(2, 3) # 2 + 3 = 5
print(my_formated_string)