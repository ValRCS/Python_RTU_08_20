# lesson_2, 1. Uzdevums
# Uzrakstiet programmu, kas noprasa un saglabā lietotāja vārdu
# Uzdod jautājumu par lietotāja vecumu, jautājumā izmantojot lietotāja vārdu.
# Uzrāda pēc cik gadiem lietotājam būs 100 gadi :)
 
import datetime
year_Limit = 100
 
current_Year = datetime.datetime.now().year
#input prasa ievadīt tekstu(str)
my_Name = input("Ieraksti savu vardu: ")
my_Age = input("Ieraksti savu vecumu: ")

years_To_End = year_Limit - int(my_Age) # try to avoid magic numbers
# DRY - Do not Repeat Yourself
end_Year = current_Year + int(years_To_End)
# f = formatted string
print(f"{my_Name}, jums {year_Limit} gadi būs pec {years_To_End} gadiem.")
print(f"{my_Name}, jums {year_Limit} gadi būs {end_Year}. gadā.")