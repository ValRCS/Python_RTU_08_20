# print("Diana" * 5) # Izdrukājiet savu vārdu 5 reizes
# print("Diana"*7) # Kas notiks ja mēģināsiet reizināt savu vārdu ar kādu pozitīvu skaitli, piem. 7
# print((60*60)*24*365) # Aprēķiniet cik sekundes būs šogad (365 dienas šogad!)
# print(10**100) # Aprēķiniet googol, tas ir 10 - 100tajā pakāpē (10**100)
# print("Ba" + "na"*4) # Izdrukājiet Banananana - tikai izmantojot Ba un na (nevis pilnu vārdu

print(1_000_000+24)  # _ here is used for cosmetic reasons
print((5+4)*(3+2))  # we can use parenthesis for priority

name = "Visvaldis"  # in Python we declare variable when we first use it
number = 7
print(name)  # this is a variable
print("Nice to meet you {name} No.{number}")  # just text
print(f"Nice to meet you {name} No.{number} ")
print("Nice to meet you" + name + "No." + str(number))

print("name") # this is just a string
square = number**2
print(f"{number} squared is {square}")

my_string_num = "9000"
my_number_from_string = int(my_string_num)

print(my_string_num * 2)
print(my_number_from_string * 2) # notice the difference


print("Whew all done")