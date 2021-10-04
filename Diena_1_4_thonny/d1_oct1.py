print("Valdis", "Līga")
print("Valdis","Līga", "Maija", sep=" 😅+😆 ")
print("Alus", end="")  # so this line will not start a newline as default print
print(" ari ira sula")

print("Ilze "*5)
print("Ilze "*7)
print(365*24*60*60)
print(10**100)
print("Ba"+"na"*4)

print("2 + 2 =", 2+2)



print(1_000 + 50) # so _ in 1_000 is cosmetic, Python ignores it
print(1_000_000 + 50)

print(20/6)
print(20//6) # so only the whole part which is 3
print(20%6) # so reminder will be 2
print(10%6) # so reminder will be 4
print(11%6) # so reminder will be 5
print(12%6) # so reminder will be 0 indeed! 😅
print(13%6) # so again now it will be 1
print(14%6) # 2
print(15%6) # 3

# so Python has built in irrational number math as well
# where 1j is one i in regular math books
print((0+1j)**2) # should be -1

print(round(3.1415926, 4))