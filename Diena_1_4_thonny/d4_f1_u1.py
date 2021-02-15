# fizz = "Fizz"
# buzz = "Buzz"
# fiz_num = 5
# buzz_num = 7
# for n in range (1,101):
#     if n % fiz_num == 0 and n % buzz_num == 0:
#         print(fizz+buzz)
#     elif n % fiz_num == 0:
#         print(fizz)
#     elif n % buzz_num == 0:
#         print(buzz)
#     else:
#         print(n)

for i in range(1,101):
    if i%5 == 0:
        print("Fizz",end="")
    if i%7 == 0:
        print("Buzz",end="")
    if i%5 !=0 and i%7 != 0:
        print(i, end="")
    if i < 100:
        print(",", end="")
