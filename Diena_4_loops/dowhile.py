# emulating do while
# do while loop property is that the loop runs at least once
i =15
while True:
    print("Value of i", i)
    i -= 1
    if i < 5:
        break
print("This always runs after the loop is done", i)
