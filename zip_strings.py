my_name = "Valdis"
your_name = "Volbis"
new_name = ""
for c1, c2 in zip(my_name, your_name):
    if c1 == c2:
        new_name += c1  # could be c2
    else:
        new_name += "X"
print(new_name)
