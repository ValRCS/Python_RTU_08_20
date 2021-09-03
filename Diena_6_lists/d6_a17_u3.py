## Uzdevums-3
"""
Lietotājs ievada teikumu.
Izvadam visus teikuma vārdus apgrieztā formā.
Alus kauss -> Sula ssuak
PS Te varētu noderēt split un join operācijas.
"""
teikums = input("Ievadi teikumu: ")
tokens = teikums.split(' ')
# teikums_reversed = ''

# my_list = [] 
# for token in tokens:
#     # teikums_reversed += f"{each[::-1]} " # this can get slow on large texts
#     my_list.append(token[::-1])
tokens_reversed = [token[::-1] for token in tokens]
teikums_reversed = " ".join(tokens_reversed) # we only put spaced between not around or end
teikums_reversed = teikums_reversed.capitalize()
print(f"{teikums} -> {teikums_reversed}")