# let's wrap our inputs in while try except block

while True:
    try:
        sakuma_skaitlis = int(input("Ievadiet sākuma skaitli: "))
        beigu_skaitlis = int(input("Ievadiet beigu skaitli: "))
        # so here we know BOTH sakuma_skaitlis and beigu_skaitlis are integers
        break
    except ValueError as ex:
        print("Ievadiet skaitli")
        # continue would be needed if I wanted to continue the loop with some other code
 
 
kubi = []
 
 
for skaitlis in range(sakuma_skaitlis, beigu_skaitlis + 1):
    kubs = skaitlis ** 3  
    kubi.append(kubs)  
    print(f"{skaitlis} kubā: {kubs}")  

# it is very common to start with empty list and then add elements
# thus Python offers a shortcut for this
# called list comprehension

# kubi = [skaitlis ** 3 for skaitlis in range(sakuma_skaitlis, beigu_skaitlis + 1)]
also_cubes = [n**3 for n in range(sakuma_skaitlis, beigu_skaitlis + 1)]

# we can also add filters to list comprehension
# how about odd cubes
odd_cubes = [n**3 for n in range(sakuma_skaitlis, beigu_skaitlis + 1) if n % 2 != 0]

# of course we could have created odd cubes with a loop
odd_cubes_loop = []
for n in range(sakuma_skaitlis, beigu_skaitlis + 1):
    if n % 2 != 0: # check for odd number - means we have remainder from division by 2
        odd_cubes_loop.append(n**3)
        # if we needed to do something else here then we would stick with the loop

# when to use list comprehension and when to use loop?

# list comprehension is more compact and often faster
# however, it is not always the best choice
# if you need to do something more complex than just creating a list then use a loop
 
 
print(f"Visi kubi: {kubi}")
print(f"List comprehension visi kubi: {also_cubes}")

# odd cubes
print(f"List comprehension odd kubi: {odd_cubes}")
print(f"Loop odd kubi: {odd_cubes_loop}")