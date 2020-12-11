# c_temp = input("What is the temperature in Celsius?")
c_temp = input("Kāda ir Jūsu temperatūra?")
c_temp = float(c_temp)
f_temp = 32 + c_temp * (9/5)
f_temp = round(f_temp, 2)
# 2 is how many digits after comma we want precision

print(f"{c_temp} degrees in Celsius is {f_temp} degrees in Farenheit.")
