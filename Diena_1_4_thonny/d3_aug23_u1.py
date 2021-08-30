user_temp = float(input ('Please enter your present body temperature: '))
# user_temp = round(user_temp)
 
if user_temp <= 35:
    print(f'your temp is {user_temp}, is below normal limit, are you cold?')
elif user_temp > 35 and user_temp <= 37:
    print(f'Yours temp equals {user_temp}, looks like you are ok')
else:
    print(f'yors temp, {user_temp}, increased normal level, we need to make extra test')