print("Hello October Pythonists! :) 😀") # izdruka uz ekrāna
# This is a comment meant for humans - it is ignored by computer
print("Es varu rakstīt arī latviski 🥔")
print('I can use single quotes it is the same thing')
print('Ar vienkāršām pēdiņām es varu iekšā likt dubult "pēda" tekstu')
print("") #pilnīgi tukšs teksts
print() # varu ari drukāt neko, tā būs jauna rinda pēc noklusējuma
print("Darbs turpinās")
# mēs varam ari veikt aritmētiskas darbības
print(2+2)
# ievērojam atškirību
print("2+2")
# how about other arithmetic
print(2*10)
# i can combine multiple expression and print them
print("2+2=",2+2) # by default , will give you space as separator
# if we do not want it
print("2+2=",2+2, sep="")
# i prefer so called f-strings since Python 3.6
print(f"2+2={2+2}") # the expression inside {} will be evaluated
# back to arithmethic
print(10-3)
# print(20/4) # / gives you so called float jeb decimal skaitlis ar komatu
# print(10/3) # interestingly we get 5 at the end not 3 or 4!
# print(10/0)
print(20//6) # this is so called integer division
# we get 3 since
# we can also get reminder
print(20%6) # reminder is 2 here since 3*6 == 18
# we also get built in power with **
print(2**3) # 2 cubed is 8
print(2**8)
print(2**32) # limitations of 32 bit systems
print(2**64)
# Python has built in support for large or bigNumbers, no limit
print(10**100)
# i could also take square root
print(4**0.5)
# interesting we can multiply strings
print("Beer 🍻")
print("Beer 🍻 " * 5)
