fraze = input("Ievadiet minamo frazi: ")
new_fraze = ""
for i in fraze:
    if i != " ":
        new_fraze += "*"
    else:
        new_fraze += " "
print(new_fraze)
burts = input("Ievadiet minamo burtu: ")
while fraze.find(burts) > -1:
    nr = fraze.find(burts)
    print(nr)
    fraze = fraze.replace(burts, "+", 1) #??Kāpēc nestrādāja??
    # fraze = fraze[:nr] + "+" + fraze[nr+1:]
    print(fraze)
    new_fraze = new_fraze[:nr] + burts + new_fraze[nr+1:]
print(new_fraze)

# text = input("Ievadi tekstu: ")
# text_new = ""
# for x in text:
#     if x == " ":
#         text_new += " "
#     else:
#         text_new += "*"
# print(text_new)
# char = input("Uzmini burtu: ")
# text_guess = ""
# for x in text:
#     if x == " ":
#         text_guess += " "
#     elif x == char:
#         text_guess += x
#     else:
#         text_guess += "*"
# print(text_guess)