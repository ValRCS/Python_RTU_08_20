start = 1
end = 100
fizz = 3
buzz = 5
end_symbol = ","

for n in range(start,end+1):
    if n == end:
        end_symbol = "\n"
        
    if n % fizz == 0 and n % buzz == 0: 
        print(f"FizzBuzz", end=end_symbol)
    elif n % fizz == 0: 
        print(f"Fizz", end=end_symbol)
    elif n % buzz == 0: 
        print(f"Buzz", end=end_symbol)
    else:
        print(n, end=end_symbol)