for i in range (1, 101):
    if i % 5 == 0 and i % 7 == 0:
        print('FizzBuzz', end="")
    elif i % 5 == 0:
        print('Fizz', end="")
    elif i % 7 == 0:
        print('Buzz', end="")
    else:
        print(i, end="")
    if i != 100:
        print(",", end="")
        
# lst=[]
# for n in range(1,101):
#     if n%5 == 0 and n%7 == 0:
#         lst.append("FizzBuzz")
#     elif n%7 == 0:
#         lst.append("Buzz")
#     elif n%5 == 0 :
#         lst.append("Fizz")
#     else:
#         lst.append(n)
# print(lst)

# cumulative = ""
# x = int(input("Enter range lowest num: "))
# z = int(input("Enter range highest num: "))
# for i in range(x, z+1):
#     if i % 5 == 0 and i % 7 == 0:
#         #print ('Fizz')
#         cumulative +='FizzBuzz,'
#     elif i % 7 == 0:
#         #print('Buzz')
#         cumulative +='Buzz,'
#     elif i % 5 == 0:
#          #print('FizzBuzz')
#         cumulative +='Fizz,'
#     else:
#         #print(i)
#         #cumulative += str(i)&
#         cumulative +=f"{i},"          
# print(cumulative)

# rez = ""
# for i in range(1,101):
#     if i%5 == 0:
#         rez+='Fizz'
#     if i%7 == 0:
#         rez+='Buzz'
#     if i%5 != 0 and i%7 !=0:
#         rez+=f'{i}' #rez+=str(i)
#     rez+= ","
# print(rez)
