temp_cels = float(input(f"Let's convert temperature from Celsius to Farenheit, pleas enter the temperature in ℃ "))
temp_converted = 32 + temp_cels * (9 / 5)
temp_converted = round(temp_converted, 2)
print(f"{temp_cels} degrees in celsium is {temp_converted}℉ in Farenheit")