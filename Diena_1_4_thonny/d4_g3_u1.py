fizz = 3
buzz = 5
for i in range(1,101):
    if i % fizz == 0 and i % buzz == 0:
        print("FizzBuzz", end=",")
    elif i % buzz == 0:
        print("Buzz", end=",")
    elif i % fizz == 0:
        print("Fizz", end=",")
    else:
        print(i,end=",")

# result = ""
# for i in range(1,101):
#     rem5 = i % 5
#     rem7 = i % 7
#     if rem5 == 0:
#         result+="Fizz"
#     if rem7 == 0:
#         result+="Buzz"
# #    if rem5 * rem7 != 0:
#     if rem5 != 0 and rem7 != 0:
#         result+=str(i)
#     if i!=100:
#         result+=","
# print(result)