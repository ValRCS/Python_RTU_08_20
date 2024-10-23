# 1. Lielais rezultāts
# Uzrakstiet funkciju add_mult, kurai nepieciešami trīs parametri/argumenti
# Atgriež rezultātu, kas ir 2 mazāko argumentu summa reizināta ar lielāko argumenta vērtību.
# PS Uzskatīsim, ka funkcijai vienmēr tiks padoti skaitliski parametri, varam tipus nepārbaudīt.
# Iespējami dažādi risinājumi, piemēram ar list struktūru varētu būt tīri eleganti.
# Piemērs add_mult(2,5,4) -> atgriezīs (2+4)*5 = 30
# def add_mult(a,b,c):
#     if a<c and b<c:
#         return (a+b)*c
#     elif b<a and c<a:
#         return (b+c)*a
#     else:
#         return (a+c)*b


# using list it is even easier
def add_mult(a, b, c):
    numbers = [a, b, c] # we create a list of numbers from the arguments
    numbers.sort() # IN PLACE sorting of the list modifies the original list
    return (numbers[0] + numbers[1]) * numbers[-1] # numbers list will be destroyed after the function ends
    
# we can assign multiple values to multiple variables in one line
a,b,c = 2,5,4 # this is due to tuple unpacking

print(add_mult(a,b,c)) # 30
print(add_mult(-2,45,4)) # 90

# let's create unlimited number of arguments version
# this version will return sum of two smallest numbers multiplied by the largest number
def add_mult(*args) -> int|float|str: # we use type hinting to show that the function returns int or str
    if len(args) < 2: # we need at least 2numbers to sum and multiply
        return "Please provide at least 2 numbers"
    # also we could have returned None or raise an exception or return 0 or something else
    # we need at least 2 numbers to sum and multiply
    numbers = list(args) # we create a list of numbers from the arguments
    # we needed to use list because tuple is immutable and we can't sort it
    numbers.sort() # IN PLACE sorting of the list modifies the original list
    return (numbers[0] + numbers[1]) * numbers[-1] # numbers list will be destroyed after the function ends

print(add_mult(5,4)) # 45 because (4+5)*5 = 45
print(add_mult(2,5,4)) # 30
print(add_mult(-2,45,4,1,2,5,6,2,6,-8)) # -450