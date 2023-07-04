#2. uzdevums
# without user functions
# w = float(input("Telpas platums "))
# l = float(input("Telpas garums ")) # 1 I l used to be similar in many fonts
# h = float(input("Telpas augstums "))
# volume = round(w*l*h, 2)
# print(f"Telpas tilpums {volume} m³")

# functional solution - used defined
def get_user_input():
    # i could add error handling
    w = float(input("Telpas platums "))
    l = float(input("Telpas garums ")) # 1 I l used to be similar in many fonts
    h = float(input("Telpas augstums "))
    return w,l,h # i could return all 3 at once as tuple

def get_volume(wdt, lng, hgt):
#     return int(lng) * int(wdt) * int(hgt)
    return wdt*lng*hgt

def print_result(volume):
    print(f"Telpas tilpums {volume:.2f} m³")

# we would need to call this function at some point
w,l,h = get_user_input()
also_volume = get_volume(w, l, h)
print_result(also_volume)


