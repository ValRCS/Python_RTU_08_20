#day4 ex1
start = 1 # it could be user input just like rest of values
stop = 100
fizz = 5
buzz = 7
fizz_text = "Fizz"
buzz_text = "Buzz"

for n in range(start,stop+1):
    end_symbol = ","
    if n == stop:
        end_symbol = "\n" # actually "\n" is default in print
    if n % fizz == 0 and n % buzz == 0:
        print(fizz_text+buzz_text, end=end_symbol)
    elif n % buzz == 0:
        print(buzz_text, end=end_symbol)
    elif n % fizz == 0:
        print(fizz_text, end=end_symbol)
    else:
        print(n, end=end_symbol)