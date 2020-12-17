# continue
# i = 1
# while i < 30:
#     i+=1 # careful with continue we need an increment to avoid forever loop
#     if i % 2 == 0:
#         print("Even Number!", i)
#         print("Jumping to the start of the loop")
#         continue
#     print("Hmm must be odd!", i)
#     i+=10
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
# print("All done")

    