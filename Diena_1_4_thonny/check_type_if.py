is_dark = True

if type(is_dark) is bool:
    print(f"Cool {is_dark} is {type(is_dark)}")
else:
    print("not boolean")
    
if type(is_dark) == bool:
    print(f"Cool {is_dark} is {type(is_dark)}")
else:
    print("not boolean")