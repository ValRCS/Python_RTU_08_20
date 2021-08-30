# 1. Uzdevums
# Uzrakstiet programmu, kas noprasa un saglabā lietotāja vārdu
username = input("What is your username?") 
#print(username)
 
# Uzdod jautājumu par lietotāja vecumu, jautājumā izmantojot lietotāja vārdu.
age = input(f"{username}, what is your age?")
#print(age)
 
# Uzrāda pēc cik gadiem lietotājam būs 100 gadi :)
import datetime 
currentYear = datetime.datetime.now().year
oldafter = str(+currentYear + 100 - int(age))
 
print(f"{username} will be 100 years old at year: {oldafter}")