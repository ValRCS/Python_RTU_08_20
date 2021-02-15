# a = int(input("Ievadi pozitīvu skaitli"))
#  
# i=1
# c=0
# list= []
# for i in range (2,a):
#  
#     if a % i == 0:
#         c+=1
#         list.append(i)
#  
# if c > 0:
#     print (f"skaitlis {a} nav pirmskaitlis, jo bez sevis un 1, papildus dalās arī ar skaitļiem: {list}")
# else:
#     print(f"skaitlis {a} ir pirmskaitlis")

import math
def user_input_needed(prompt, var_type):
    while True:
        user_input = input(prompt)
        try:
            if var_type == str:
                float(user_input)  # Float because entering 1.01 would pass this test
                print("Incorrect value entered")
            elif var_type == int:
                try:
                    val = int(user_input)
                    return val
                except ValueError:
                    print("Incorrect value entered")
            elif var_type == float:
                try:
                    val = float(user_input)
                    return val
                except ValueError:
                    print("Incorrect value entered")
        except ValueError:
            break
 
    return user_input

def task_3():
    input_digit = user_input_needed("Input digit: ", int)
    if input_digit > 1:
        root = math.sqrt(input_digit)
        for i in range(2, int(root) + 1):
            if (input_digit % i) == 0:
                print(input_digit, "is not a prime number")
                print(i, "times", input_digit // i, "is", input_digit)
                break
        else:
            print(input_digit, "is a prime number")
    else:
        print("Not prime number")

task_3()