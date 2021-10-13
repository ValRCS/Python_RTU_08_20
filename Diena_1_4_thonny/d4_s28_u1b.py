# 1. FizzBuzz uzdevums
fizz = 3
buzz = 5
start = 1
finish = 40
for n in range(start,finish+1):
    end = ","
    if n == finish:
        end = "\n"
    if n%fizz == 0 and n%buzz == 0:
        print("FizzBuzz", end=end)
    elif n%fizz == 0:
        print("Fizz", end=end)
    elif n%buzz == 0:
        print("Buzz", end=end)
    else:
        print(f"{n}", end=end)