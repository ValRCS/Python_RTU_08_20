print(True and True) # nevis &&, tas ir citās valodas
print(True and False)
print(False and True)
print(False and False)
print(True and 2*2 == 4)
print(True and 2*2 == 4 and len("Valdis") > 5 and 2*2 == 5)
print(True and 2*2 == 5 and 2*2 == 4 and 2*2 == 6) #last statement will not be processed
is_math_ok = True
is_mic_ok = True
is_zoom_ok = False
print(is_math_ok and is_mic_ok)
print(is_math_ok and is_mic_ok and is_zoom_ok)
# or nevis || kas nav Python
print(True or True)
print(True or False)
print(False or True)
print(False or False)
print(2*2 == 5 or 2*2 == 4 or is_math_ok)
print(2*2 == 4 and 3*3 == 9 or 5 > 10)
print(not False, not True)
print(not is_math_ok)