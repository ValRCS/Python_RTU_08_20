# your_name = input(f'Please enter name: ')
# back_name = your_name[::-1] 
# print(f'{your_name} -> {(back_name.capitalize())} , pamatigs juceklis vai ne {your_name[0].upper()}?')

name = input("Enter the name:") 
name = name.capitalize()
name_rev = name[::-1].capitalize()
 
print(f"{name_rev}, pamatīgs juceklis, vai ne {name[0]}?")