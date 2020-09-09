i = 0
while True:
    print("Working non-stop")
    is_done = input("Quit? (Y/N) ")
    if is_done == 'Y' or is_done == 'y':
        break
    else:
        print("keep working!")
    if i > 4:
        print("You've done enough work now relax")
        break
    i += 1
print("out of our loop prison!")