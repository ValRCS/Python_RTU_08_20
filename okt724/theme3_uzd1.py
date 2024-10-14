LOW_TEMP = 35
HIGH_TEMP = 37

temperature = float(input("Ievadiet savu temperatūru: "))
if temperature < LOW_TEMP:
    print("Nav par aukstu?")
elif LOW_TEMP <= temperature <= HIGH_TEMP: # tehniski 35 <= nav nepieciešāms
    print("Viss kārtībā")
else: # šeit mēs zinam ka ir pāri 37
    print("Iespējams drudzis")