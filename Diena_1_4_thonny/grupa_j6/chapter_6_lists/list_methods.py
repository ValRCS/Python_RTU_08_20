# let's look at more list methods

# first we create a list of chocolates
chocolates = ["M&M", "Snickers", "Mars"]
#, "Twix", "Bounty", "Milka", "Kinder", "Lindt", "Ritter Sport", "Toblerone"]
print(chocolates)

# we can add elements to the end of the list
chocolates.append("Twix")
print(chocolates)
chocolates.append("Serenāde")
print(chocolates)

# so append is IN PLACE - it changes the list

# we could use + to add two list together and creating a new list
# here we overwrite the original list
chocolates = chocolates + ["Bounty", "Milka"]
# also chocolates += ["Bounty", "Milka"] would work
print(chocolates)

# instead we can use extend method to add values from another list
chocolates.extend(["Kinder", "Lindt"])
print(chocolates)

# compare with append
chocolates.append(["Ritter Sport", "Toblerone"])
print(chocolates)

# so we added a list as an element to the list
# print last element
print(chocolates[-1]) # prints ["Ritter Sport", "Toblerone"]
# btw how could we access the last element of the inner list?
print(chocolates[-1][-1]) # prints Toblerone

last_element = chocolates.pop() # removes last element and returns it
print(last_element)
print(chocolates)

# let's get rid of first element
first_element = chocolates.pop(0) # removes first element and returns it
print(first_element) # prints M&M
print(chocolates) 

# i can insert an element at a specific index
chocolates.insert(5, "Diāna") # inserts at index 5 - so 6th element
# rest of elements are shifted to the right
print(chocolates)
# in large lists these operations can be slow

# find index of an element
print(chocolates.index("Serenāde")) # returns 3
try:
    print(chocolates.index("M&Lukss")) 
except ValueError:
    print("M&Lukss not found")

# we can count how many times an element is in the list
# first lets add Diāna again
chocolates.append("Diāna")
print(chocolates)
print(chocolates.count("Diāna")) # returns 2

# let's create a copy of our chocolates list
chocolates_copy = chocolates.copy() # creates a new list - so called shallow copy
print(chocolates_copy)

# let's create a an alias for our list
chocolates_alias = chocolates # so we have two names for the same list
# this is not a copy - it is an alias!!
print(chocolates_alias)

# let's remove Twix from our original list
chocolates.remove("Twix") # removes first occurence of Diāna

# let's print our lists
print(chocolates)
print(chocolates_copy) # Twix is still there!
print(chocolates_alias)

# let's sort our list
chocolates.sort() # sorts in place - using lexicographical order
print(chocolates)
# again copy is not affected
print(chocolates_copy)


# for numeric lists we have sum, min, max
# let's create some random numbers
import random
# i am creating 10 random numbers between 1 and 100 - including 1 and 100
# _ indicates that we do not care about the value
# to set a seed for random numbers use 
random.seed(2023) # so we get the same pseudo-random numbers good for testing
# remove the seed for real random numbers
random_numbers = [random.randint(1,100) for _ in range(10)]
print(random_numbers)

# these work if ALL elements are numeric
# sum
print("Sum", sum(random_numbers))
# min
print("Min", min(random_numbers))
# max
print("Max", max(random_numbers))
# finally average
print("Average", sum(random_numbers)/len(random_numbers))

# finally we can clear the list
chocolates.clear() # Clears the list IN PLACE! modifies the list
print(chocolates)

# we have eaten all the chocolates - so sad
# of course we do have a backup list in chocolates_copy
print(chocolates_copy)
