# let's make a simple add function

def add(a, b):
    return a + b

# let's call it
# print(add(1, 2))
# instead of printing i could save the results
result = add(1, 2)
# and use it later
print(result)

# how about multiply
def multiply(a, b):
    return a * b

# let's call it
print(multiply(2, 3))

# with return values we get a lot of flexibility 
# we can use them in other functions
print(add(add(5,10), multiply(2, 3)))

# let's make a function that multiplies list values
def multiply_list_values(values):
    result = 1 #very important to initialize the result
    for value in values:
        result *= value
    return result

# let's call it
mult_result = multiply_list_values([10, 2, 3, 4])
print(mult_result)