# common sequence operations apply as to strings as well
# https://docs.python.org/3/library/stdtypes.html#typesseq-common
min("Valdis")
ord("V")
ord("a")
ord("ā")
max("Valdizzs")
"alus " * 5
"alus " + "sula"
"Valdis alā".count("al")
# https://docs.python.org/3/library/stdtypes.html#string-methods
str.capitalize("valdis")
"valdis".capitalize()
"svētki".count('tk')
"alus darva jāņi".capitalize()
"python".center(20, "X")
"maize".center(20, " ")
"maize".center(20, " ")
"maize".center(20, "")
"python".center(20, "")
"python".center(11, "*")
"kartupelis pelis elis".count("li")
"kartupelis".encode()
"kartupelis".endswith("elis")
food = "kartupelis"
food.endswith("elis")
food.find("tup")
"tup" in food
f"mans ēdiens ir {food} un jaunā iespēja {food=}"  # with 3.8 you can use food=
f"mans mainīgas ir food un vertība ir {food}"  # old way of debugin
food.index("tup")  # will raise error
food.find("tupenis")  # -1 when not found
food.index("tupenis")  # will raise ValueError
"dafdfaDDD4532542".isalnum()
"dafdfaDDD   4532542".isalnum()
"dafdfa4532542".isalpha()
"dafdfDDDDa".isalpha()
"Valdis".isascii()
"Kaķis".isascii()  # ķ nav ASCII
ord('ķ')
"5342423".isdecimal()
"5342423.523523".isdecimal()  # useful for finding int inputs not floats
"5342423DD".isdecimal()
"5342423.523523".isdigit()
"5342423523523".isdigit()
# https://docs.python.org/3/reference/lexical_analysis.html#identifiers
'hello'.isidentifier()
'hello007'.isidentifier()
'007hello'.isidentifier()
'fo od'.islower()
'fo  Dod'.islower()
food.islower()  # kartupelis
"3.14159".isnumeric()
"3/6".isnumeric()
"3,6".isnumeric()
"365".isnumeric()
"\t\t   ".isspace()
"Valdis".istitle()
"Alice told rabbit 'drink me' "
print("Alice told rabbit \n 'drink me' rabbit said \" really \" ! ")

print(""" Viss kaut kas
  ' anything goes'' "" more stuff ''
  another line 
        tab
""")
print('''
 this also works!
            cool
''')
"Rīgas Vēlēšanas".istitle()
"Rīgas vēlēšanas".istitle()  # all words must start with capital
"RĪGA".isupper()
# this works because Jūrmalas is a sequence(string in this case)
"XX".join("Jūrmala")
",**".join(["Valdis", "Līga", '10'])
"Rīga".ljust(10, "*")
"Rīga".ljust(10, "X")
"Rīga".ljust(10, " ")
"RīGa".lower()
" \t    Rīga".lstrip()
drink = "alus " * 4
drink
drink.replace("lu", "ka")
drink.replace("lu", "ka", 2)
# if we do not specify count then everything is replaced
drink.replace("lu", "la")
new_stuff = drink.replace("lu", "la")
new_stuff
food.rfind("eli")
food.find("eli")
food += " melis"
food
food.rfind("eli")
food.find("eli")
food.rindex("eli")
"Rīga".rjust(10, "x")
"   Rīga    ".rstrip()
"Valdis Līga Rīga".split()
"Valdis * Līga , Rīga".split(",")
"Valdis\nAnother Line\n Valdis".splitlines()
food.startswith("kart")
"   Rīga    ".strip()
"skaista diena vai ne".title()
"skaista diena".upper()
"3.1415".zfill(10)  # works with pretty much any string
"Rīga".zfill(10)
"-Rīga".zfill(10)
"-5000".zfill(10)
