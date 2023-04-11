# for loops
# for loops are to be used
# when we know how many times we want to run loop
# in other words
# we iterate over some collection of some values
# there are many different collections that are iterable

# by default we only have exclusive(not included) end and start is 0
for n in range(4):
    print("Number is ", n)
    print(f"Indeed number is {n}")

# I can supply start and end to range

for n in range(10,15):
    print(f"Indeed number is {n}")
# we are outside for loop
print(f"n is is still {n}")
# i could reuse n
# here we see step (3rd argument for range)
for n in range(100, 111, 3):
    print(f"Indeed number is {n}")
    
# i could go another direction
for n in range(30, 20, -2):
    print(f"now n is {n}")
    
# there are many different types of iterables
# strings are iterable
name = "Valdis"
for c in name:
    print("Letter", c)
    
# i might want to see the element by order number
# in other words I would like to enumerate the collection

for i,c in enumerate(name):
    print(f"Item No. {i} is {c}")
    
# we could start numeration from any number
for i,c in enumerate(name, start = 101):
    print(f"Item No. {i} is {c}")
    
for i,n in enumerate(range(1_000,1_200, 50)):
    print(f"Item No. {i} is {n}")
    
# if I just want to repeat some stuff but do not need loop variable

for _ in range(3): # _ is just a variable but indicates it is not imporant
    print("Just doing some stuff")
    print("still doing stuff")

# i could use more descriptive names but usually loop variables are short
for single_character in name:
    print(f"Checking {single_character}")
    
# we can nest loops
for x in range(5): # outer loop
    for y in range(4): # inner loop
        result = x*y 
        print(f"{x} * {y} == {x*y}")

print("Starting another nested loop")
for x in range(1,6): # outer loop
    for y in range(1,5): # inner loop
        result = x*y 
        print(f"x*y {x} * {y} == {x*y}")
        
# again to generalize a for loop with range
start = 100
end_not_included = 110
step = 2
for n in range(start, end_not_included, step):
    print("n is ", n)

# break and continue work in for loops as well
for n in range(10):
    if n == 4:
        print("Early quitting time!", n)
        break
    if n == 2:
        print("Going straight to next loop cycle")
        continue # will skip the below line(s)
    print(f"Working on number {n}")
    
    
# for (and also while) loops have else !!!

for n in range(3):
    print("n is ", n)
else: # will only run if loop did not break early
    print("Loop finished without break!")

print("Outside loop")

for n in range(3):
    print("n is ", n)
    if n == 1:
        print("Early break so else for the loop will not work")
        break
    else: # this is for if not for !!!
        print("n is not 1")
else: # will only run if loop did not break early
    print("Loop finished without break!")
    
# more on loops
# https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops

print("Outside loop")

# Again we use for loops when have definite number of cycles
# while loops are better when we do not know the exact number
    