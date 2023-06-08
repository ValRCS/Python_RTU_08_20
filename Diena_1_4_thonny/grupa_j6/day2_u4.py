users_temp = float(input("What's your temperature? "))
 
if users_temp < 35:
    print("Isn't it a bit too cold?")
elif users_temp <= 37:# 35 <= was not needed
    print("Oh, that's fine")
else: # so >37
    print("Damn, you have fever")