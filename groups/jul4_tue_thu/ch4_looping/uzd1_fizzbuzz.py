# 2. uzdevums Fizz Buzz
buffer = ""
sep = ","
fizz = 5
buzz = 7
stop = 100
# for num in range(1,stop+1):
#     if num == stop:
#         sep = "" # \n" # or""
#     # very careful it is possible that all 3 ifs fire
#     # here only 2 can fire at once Fizz and Buzz
#     if num % fizz == 0:
#         buffer += "Fizz" # same as buffer = buffer + "Fizz"
#     if num % buzz == 0:
#         buffer += "Buzz"
#     if num % fizz != 0 and num % buzz != 0:
#         buffer += str(num)
#     buffer += sep
# print(buffer)
end = "," # default is \n
for n in range(1, stop+1):
    if n == stop:
        end = "\n"
    if n % fizz == 0 and n % buzz == 0:
        print("FizzBuzz", end=end)
    elif n % fizz == 0:
        print("Fizz", end=end)
    elif n % buzz == 0:
        print("Buzz", end=end)
    else:
        print(n, end=end)