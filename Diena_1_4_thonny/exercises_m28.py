print("Ieva " * 5)
print("Vārds tiks izdrukāts vairākas reizes, piemēram, 7 reizes")
print(365*24*60*60)
print(10**100)  # Googol
print("Ba" + "na" * 4)

print(str(10**100) + " tas ir Gugulis") # numbers need to be
# transformed into strings before doing string operation

# starting from Python 3.6 we have f-strings
# formatted strings
print(f"My text and some expression 2+2={2+2}")

# Python variables need no special prefixes
my_result = 2*2+1_000 # we can use _ for larger numbers
print(f"Result of my calculations is {my_result}")
a = 2
b = 3
c = a+b
print(a,b,c)
print(f"Cool the following expression {a}+{b}={c}")

