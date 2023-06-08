my_name = "Valdis"
# my_name is now available until the end of the program
greeting = f"Hello my name is {my_name} and {3*3*10} is today's number"
print(greeting)
a = 10
b = a / 3
print(a, b)
# with type function we can determing what type of type we hold
print(type(my_name)) # str
print(type(a), type(b)) # int and float
# floats are strange
# not all floating numbers can be represented exactly
# https://en.wikipedia.org/wiki/IEEE_754
double_googol = 10**200
c = b * double_googol
print(c)
d = 0.1
e = 0.2
f = d + e # you would expect 0.3 but... floats are weird
print(f)
rounded_f = round(f,4) # 4 digits after comma
print(rounded_f)
# if i want to keep without rounding I can
# i can just format my output
print(f"number f to 4 digits after comma {f:.4f} ")
# without f it will print up to 4 digits
print(f"number f to 4 digits after comma {f:.4} ")
# https://stackoverflow.com/questions/45310254/fixed-digits-after-decimal-with-f-strings

# too much round can be dangerous
# https://en.wikipedia.org/wiki/Vancouver_Stock_Exchange
# advice to round at the very end



