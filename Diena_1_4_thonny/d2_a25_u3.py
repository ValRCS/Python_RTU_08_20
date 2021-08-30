# 3. Uzdevums
#print(f"Please input temperature in °C ") # new line after print is default
celsius = float(input(f"Please input temperature in °C \n\t"))
result = round(32+celsius*(9/5), 2)
print(f"{celsius}°C is {result} °F")