name=input("Ievadi vārdu ")
reverse = name[::-1].title()    # reverse the string and capitalize the first letter of every word
print(f"{reverse} pamatigs juceklis vai ne, {name[0].upper()}?")