while True:
    try:
        height = int(input("Ievadiet eglītes augstumu: "))
        break
    except ValueError:
        print("Lūdzu ievadiet veselu skaitli")

# here we have integer height guaranteed, could check negative here with if

sym = "*"
# sym = "🌲" # might not work exactly due to the font used for unicode
# sym = "x"
for i in range(height): # sometimes people start with 1 then formula changes slightly
    print(' ' * (height - i - 1) + sym * (2 * i + 1))
trunk_height = height // 3
for i in range(trunk_height):
    print(' ' * (height - 1) + sym)