my_name = "Valdis"
# I can use variable from now on
# f-string let use variables and any valid expression inside string template
greeting = f"Hello my name is {my_name} and 2+2={2+2}"
print(greeting)
# it can be useful to find the type of data
print(type(greeting))
a = 10
b = a / 3
print(a, b)
print(f"a is {a} and b is {b}")

print(f"a is {a} and is of type {type(a)}")
print(f"b is {b} and is of type {type(b)}")
# floats are weird!
# https://en.wikipedia.org/wiki/IEEE_754
c = 0.1
d = 0.2
result = c + d
print(result)
# so we could round up the result to say nearest 2 digits after comma
rounded_result = round(result, 4)
print(rounded_result)
# care should be taken to round towards end
# do not round everything all the time
# https://en.wikipedia.org/wiki/Vancouver_Stock_Exchange#Rounding_errors_on_its_Index_price

# also it is possible to print results without rounding
print(f"b to the 4 digits {b:.4}")
