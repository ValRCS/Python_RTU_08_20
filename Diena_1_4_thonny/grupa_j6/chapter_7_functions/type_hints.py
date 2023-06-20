# Python offers type hints for function parameters and return values.
# idea is to help other programmers understand what is expected

def add(a: int, b: int) -> int:
    """Adds two numbers and returns the result
    
    Args:
        a (int): first number
        b (int): second number

    Returns:
        int: sum of a and b
       
    """	
    return a + b

print(add(2, 3)) # 5
print(add(2, 3.5)) # 5.5 # no error !!!
print(add("2", "3")) # 23 # no error !!!
print(add("Valdis", " Saulespurēns")) # ValdisSaulespurēns # no error !!!
print(add([1,2,3], [4,5,6])) # [1, 2, 3, 4, 5, 6] # no error !!!
# so Python interpreter does not care about type hints

# however we can use external tools to check our code
# such as pylint, flake8, pylance

# for writing larger programs it is a good idea to use type hints
# also for sharing code with others

# lets make a function to format number
def format_number(number: float, precision:int=2) -> str:
    """Formats number to have 2 decimal places and comma as thousands separator
    
    Args:
        number (float): number to be formatted

    Returns:
        str: formatted number
       
    """	
    return f"Number to precision {precision} is {round(number, precision)}"

print(format_number(123456.7893423)) # Number to precision 2 is 123456.79
print(format_number(123456.7893423, 3)) # Number to precision 3 is 123456.789
print(format_number(555, 2)) # Number to precision 0 is 123457.0

result = format_number(123456.7893423, 3)
# since we have type hints we can use IDE to help us
# and we know that upper is a string method and result is a string
print(result.upper()) # NUMBER TO PRECISION 3 IS 123456.789