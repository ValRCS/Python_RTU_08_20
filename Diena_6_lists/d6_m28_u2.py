# 2. uzdevums
my_list = []
start_val = int(input("Lūdzu ievadiet sākuma skaitli "))
end_val = int(input("Lūdzu ievadiet beigu skaitli "))

# we can let user input the start and end values in reverse order
step = 1 if start_val < end_val else -1
# same as
# if start_val < end_val:
#     step = 1
# else:    
#     step = -1   



for n in range(start_val, end_val + 1, step):
    cube_numb = n**3
    print(f"{n} kubā: {cube_numb}")
    my_list.append(cube_numb)
print(f"{my_list}")
print("Visi kubi: [" + ",".join([ str(kub) for kub in my_list]) + "]")