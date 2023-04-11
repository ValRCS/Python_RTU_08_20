# small calculator app

while True:
    try:
        max_tries = int(input("Enter maximum number of tries "))
    except ValueError:
        print("Please enter integer!")
        continue
    break # so no break unless valid integer
# now we have valid max_tries
for n in range(max_tries):
    print("Doing something when n is", n)