# common sequence operations apply as to strings as well
# https://docs.python.org/3/library/stdtypes.html#typesseq-common
min("Valdis")
ord("V")
ord("a")
max("Valdizzs")
"alus " * 5
"alus " + "sula"
"Valdis".count("al")
# https://docs.python.org/3/library/stdtypes.html#string-methods
str.capitalize("valdis")
"valdis".capitalize()
"alus darva jāņi".capitalize()
"python".center(20, "X")
"python".center(11, "*")
"kartupelis pelis elis".count("li")
"kartupelis".encode()
"kartupelis".endswith("elis")
food = "kartupelis"
food.endswith("elis")
food.find("tup")
"tup" in food
f"mans ēdiens ir {food} un jaunā iespēja {food=}"  # with 3.8 you can use food=
food.index("tup")
food.find("tupenis")
food.index("tupenis")
"dafdfa4532542".isalnum()
"dafdfa4532542".isalpha()
"dafdfDDDDa".isalpha()
"Valdis".isascii()
"Kaķis".isascii()  # ķ nav ASCII
"5342423".isdecimal()
"5342423.523523".isdecimal()  # useful for finding int inputs not floats
"5342423DD".isdecimal()
"5342423.523523".isdigit()
# https://docs.python.org/3/reference/lexical_analysis.html#identifiers
'hello'.isidentifier()
'food'.islower()
food.islower()  # kartupelis
"3.14159".isnumeric()
"3/6".isnumeric()
"3,6".isnumeric()
"365".isnumeric()
"\t\t   ".isspace()
"Valdis".istitle()
"Rīgas Vēlēšanas".istitle()
"Rīgas vēlēšanas".istitle()  # all words must start with capital
"RĪGA".isupper()
# this works because Jūrmalas is a sequence(string in this case)
"XX".join("Jūrmala")
",".join(["Valdis", "Līga", '10'])
"Rīga".ljust(10, "*")
"RīGa".lower()
" \t    Rīga".lstrip()
drink = "alus " * 4
drink
drink.replace("lu", "la", 2)
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
