#3.uzdevums
# 3.uzdevums
print("")
num_1 = int(input("1.veselais skaitlis: "))
num_2 = int(input("2.veselais skaitlis: "))
num_3 = int(input("3.veselais skaitlis: "))
 
if num_1 <= num_2 <= num_3:
    print(num_1, num_2, num_3)
elif num_1 <= num_3 <= num_2:
    print(num_1, num_3, num_2)
elif num_2 <= num_1 <= num_3:
    print(num_2, num_1, num_3)
elif num_2 <= num_3 <= num_1:
    print(num_2, num_3, num_1)
elif num_3 <= num_1 <= num_2:
    print(num_3, num_1, num_2)
else:
    print(num_3, num_2, num_1)
 
# factorial 3! == 6
 