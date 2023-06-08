try:
    temperature = float(input("Kāda ir Jūsu temperatūra? "))
    if (temperature) < 35:
        print(f"Vai nav par aukstu? Jums ir {temperature}")
    elif 35 <= (temperature) <= 37:
        print(f"Viss kārtība! Jums ir {temperature}")
    else:
        print(f"Jums laikam ir drudzis! Jums ir {temperature}")
except ValueError:
    print("Bad user input we can only process numbers with optional . "
          ,end = "\n\n\n😞\n") # so 3 newlines instead of default one
    print("Now would be a good time to run this program again")
    print("AB", end="") # no newline
    print("CD")
