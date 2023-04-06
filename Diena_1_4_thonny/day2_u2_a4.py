# height = float(input("building height"))
# width = float(input("building width"))
# length = float(input("building length"))
# volume = width * length * height
# print(f"building volume {volume}")

# 2.uzdevums
telpasgarums = input("Ievadi telpas garumu, metros")
telpasplatums = input("Ievadi telpas platumu, metros")
telpasaugstums = input("Ievadi telpas augstumu, metros")
telpasgarums = telpasgarums.replace(",",".")
telpasplatums = telpasplatums.replace(",",".")
telpasaugstums = telpasaugstums.replace(",",".")
telpasgarums = float(telpasgarums)
telpasplatums = float(telpasplatums)
telpasaugstums = float(telpasaugstums)
teplpastilpums = telpasgarums*telpasplatums*telpasaugstums
teplpastilpums = round(teplpastilpums,2)
print(f"telpas tilpums ir {teplpastilpums} m³")