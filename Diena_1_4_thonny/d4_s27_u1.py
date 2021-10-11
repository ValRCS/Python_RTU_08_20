start = 1
last_value = 40
fizz = 3
buzz = 5

for n in range(start,last_value+1):
    end = ","
    if n == last_value:
        end = "\n" # original end

    if n % fizz == 0 and n % buzz == 0:
      print("FizzBuzz", end=end)
    elif n % buzz == 0:
      print("Buzz", end=end)
    elif n % fizz == 0 :
      print("Fizz", end=end)
    else:
      print(n, end=end)