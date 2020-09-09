for i in range(1,101):
    end = ","
    if i == 100:
        end = ""
    if i % 5 == 0 and i % 7 == 0:
        print("Fizzbuzz",end=end)
    elif i % 7 == 0:
        print("Buzz",end=end)
    elif i % 5 == 0:
        print("Fizz",end=end)
    else:
        print(i,end=end)