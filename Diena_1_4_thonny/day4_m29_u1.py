def uzdevums_1():
    """
    Izdrukāt virknīti 1,2,3,4,Fizz,6,Buzz,8,.....34,FizzBuzz,36,....līdz  97,Buzz, 99,Fizz
    Tātad ja skaitlis dalās ar 5 tad Fizz
    Ja dalās ar 7 tad Buzz,
    Ja dalās ar 5 UN 7 tad FizzBuzz
    savādāk pats skaitlis
    """
    print_value = ""
    for i in range(1, 101):
        if not i % 5:
            print_value += "Fizz"
        if not i % 7:
            print_value += "Buzz"
        if i % 7 and i % 5:
            print_value += str(i)
        if i < 100:
            print_value += ","
    print(print_value)
    
# uzdevums_1()
start = 1
finish = 100
fizz = 3
buzz = 5
for i in range(start,finish+1): # outer loop
    end = ","
    if i == finish:
        end = "\n"
    # one liner    
#     end = "," if i < finish else "\n"
        
    if i % fizz == 0 and i % buzz == 0:
        print("FizzBuzz", end=end)
    elif i % fizz == 0:
        print("Fizz", end=end)
    elif i % buzz == 0:
        print("Buzz", end=end)
    else:
        print(i, end=end)
print()  