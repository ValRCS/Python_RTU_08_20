temperature = float(input("What is your temperature? "))
cold_temp = 35.3
hot_temp = 36.9
if temperature < cold_temp:
    print("Not too cold?" )
# elif temperature >= cold_temp and temperature <= hot_temp:
elif cold_temp <= temperature <= hot_temp:
    print("You are well!" )
else:
    print("You have fever!")