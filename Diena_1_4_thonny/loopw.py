res = []
for n in range(1,101):
    if n % 7 == 0 and n % 5 == 0:
        res.append("FizzBuzz")
    elif n % 5 == 0:
        res.append("Fizz")
    elif n % 7 == 0:
        res.append("Buzz")
    else:
        res.append(n)
print(res)