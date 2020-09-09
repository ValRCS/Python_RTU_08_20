import datetime

myName = input("ievadi vārdu ")

myAge = int(input(f"ievadi {myName} vecumu "))

myHundred = 100 - myAge

print(f"{myName} pēc {myHundred} būs 100 gadi")
now = datetime.datetime.now()


currentYear = datetime.datetime.now().year
myTermins = currentYear + myHundred
print(f"tas būs {myTermins} gadā")
