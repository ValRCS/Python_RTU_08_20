# continue
i = 1
while i < 10:
    if i % 2 == 0:
        print("Even number!", i)
        i += 1
        continue # means we go to start of the loop immediately
    print("My generic num", i)
    i += 1
    if i >= 7:
        break
print("All done")

    