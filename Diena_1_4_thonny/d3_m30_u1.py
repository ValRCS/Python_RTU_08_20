#1
t_low = 35
t_high = 37
my_t = round(float(input("What is your doby temperature in celsius? ")),1)
if my_t < t_low:
    print(f"Too low! Your temp is {my_t}")
elif my_t <= t_high: # we already know that my_t >= t_low
    print(f"All good! Your temp is {my_t}")
else:
    print(f"Too high! Your temp is {my_t}")