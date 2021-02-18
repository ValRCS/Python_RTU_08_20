## task 2
num_1 = int(input("Ievadi sākuma skaitli "))
num_2 = int(input("Ievadi beigu skaitli "))
my_list = list(range(num_1,num_2+1))
my_list2 = [n**3 for n in my_list]

print(my_list)
print(my_list2)
# i can zip two lists side by side and the loop through both of them at once
# zip will end when one of the lists will end
for num, cube in zip(my_list, my_list2):
    print(f"{num} cubed is {cube}")
# print((my_list[n], "kubā: ",my_list2[n]) for n in my_list)