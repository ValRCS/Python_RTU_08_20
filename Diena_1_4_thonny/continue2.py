i = 0
while i < 10:
    if i % 2 == 0:
        print(f"Okay number {i} is even")
        continue # means we go to start of the this loop immediately
    print("Just a regular number no.", i)
    i += 1