answer = float(input("Ievadi temperatūru "))
if answer < 35:
    print("Auksti")
elif answer <= 37:
    print("OK")
else: # all that remains is answer > 37
    print("Drudzis")

# careful, with strings you will not get the expected answers
# try 9, try 200,
#1. uzdevums
# a=input("Kāda ir Jūsu temperatūra?")
# if a<="35":
#     print("nav par aukstu?")
# elif a>"35" and a<="37":
#     print("viss kārtībā")
# else:
#     print("iespējams drudzis")