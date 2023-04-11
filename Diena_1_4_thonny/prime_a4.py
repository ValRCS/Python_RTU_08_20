# finding prime
start=2
while True:
    try:
        number = int(input('enter number: '))
    except ValueError:
        print('enter integer')
        continue
    if number < 2:
        print("Please enter number 2 or more!")
        continue
    break

# if number<0:
#     print(f'{number} is not a positive integer')
# elif number==1:
#     print('1 is not prime number')

# we only need to check until square root of number !
for n in range (start,int(number**0.5)+1):
    if number%n == 0: # no reminder
        print('it is not prime number')
        print(f"{number} divides by {n} with no reminder!")
        break
else: # rare case where else inside for loop is useful
    print(f"{number} is a prime number!")
