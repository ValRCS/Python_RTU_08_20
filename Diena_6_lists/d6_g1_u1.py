numberlist = []
while True:
    num = input("Enter number (or q to quit) ")
    if num == "q":
        break
    else:
        num = float(num)
        numberlist.append(num)
        print(f"Current average: {sum(numberlist)/len(numberlist)}")
# numberlist.sort() #sort the list ascending
numberlist.sort(reverse=True) #sort the list descending
print(f"TOP3 biggest numbers are {numberlist[:3]}") #in a two item list, shows only one biggest number
print(f"BOTTOM3 smallest numbers are {numberlist[-3:]}")
print(f"Total average: {sum(numberlist)/len(numberlist)}")





# Vidējā vērtība
# skaitlis = 0
# virkne = []
# #print (float (skaitlis))
# while skaitlis != "q":
#     skaitlis = input("Ievadiet skaitli, vai q lai iziet: ")
#     if skaitlis == "q":
#         break
#     virkne.append(float(skaitlis))
#     videjais = sum(virkne)/len(virkne)
#     print(f"Vidējā vērtība ir {videjais}")
#     print(f"Skaitļi: {virkne}")

