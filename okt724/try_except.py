# we can use try except to catch errors

try: # a little bit like if, we will go to except part when we get error
    number = input("Please enter a whole number pretty please ")
    # number is guaranteed to be string above this line
    number = int(number) # here we try to convert to integer
    # here we are assured that conversion worked
    my_double = number*2
    print(f"Cool this worked double {number} is {my_double}")
except ValueError as e: # principle is to catch SPECIFIC errors
    print("Sorry you did not enter an integer")
    my_double = number*2
    print(f"Not what you want... {my_double}")
    print(f"Error message is {e}")
    
print("my double is of type", type(my_double))    

# above try except is nice for single errors

# but how about making sure input is correct?
# see input_error_checking.py


