#2.uzdevums
 
visi_skaitli = []
list_2d = []
sakuma_skaitlis = int(input("Ievadi sakuma skaitli -"))
beigu_skaitlis = int(input("Ievadi beigu skaitli - "))
# we add logic for reverse order
# step = 1
# if sakuma_skaitlis > beigu_skaitlis:
#     step = -1
# if sakuma_skaitlis > beigu_skaitlis:
#     step = -1
# else:
#     step = 1

# same as above
# ternary operator
step = 1 if sakuma_skaitlis < beigu_skaitlis else -1

for i in range(sakuma_skaitlis, beigu_skaitlis, step):
    visi_skaitli.append(i)
    list_2d.append([i, i*i])

print(visi_skaitli)
print(list_2d)


for n in range(sakuma_skaitlis,beigu_skaitlis+step, step):  
   kubaa = n**3
   print("Izvads:")
   print(f"{n} kubā: {kubaa}")
   visi_skaitli.append(kubaa)
   list_2d.append([n,kubaa])

also_cubes = [i**3 for i in range(sakuma_skaitlis, beigu_skaitlis+step, step)]
print("also cubes:", also_cubes)

print(f"Visi kubi: {visi_skaitli}")
print(f"2d list of results: {list_2d}")

print(range(sakuma_skaitlis,beigu_skaitlis+step, step))  # range is an iteratable but not a list!
print(list(range(sakuma_skaitlis,beigu_skaitlis+step, step)))  # range is an iteratable so we cast it to list