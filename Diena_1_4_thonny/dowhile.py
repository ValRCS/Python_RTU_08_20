# emulating do while
# do while loop property is that the loop runs at least once
# do while is shoot first and ask questions later loop
i = -10
while True:
    print("Value of i", i) # so this will run at least once
    i -= 1 # so this will run at least once
    if i < 5:
        break
print("This always runs after the loop is done", i)
