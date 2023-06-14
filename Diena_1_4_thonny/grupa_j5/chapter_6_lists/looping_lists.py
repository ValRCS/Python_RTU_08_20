# let's create a grocery list
grocery_list = ["milk", "bread", "eggs", 
                "cheese", "ham", "tomatoes"]

print(grocery_list)

needle = "eggs"
for index, item in enumerate(grocery_list):
    if item == needle:
        print(f"Found {needle} at index {index}")
        break
# we can also use index function - there is no find function
print(grocery_list.index("eggs"))

# let's change needle to partial match
needle = "egg"
for index, item in enumerate(grocery_list):
    if needle in item: # notice the change here
        print(f"Found {needle} at index {index}")
        break

# let's add new item to our list
grocery_list.append("vinegar")
print(grocery_list)
grocery_list.append("milk")
print(f"Count of milk: {grocery_list.count('milk')}")
print(grocery_list)

# append is a method of a list
# it is IN PLACE method meaning it changes the list
# before the methods did not change the list (and strings are immutable)

# it is important to understand that append does not return anything
# it just changes the list
# we can also remove items from a list

# let's remove milk from our list
grocery_list.remove("milk")
# this would remove first milk from the list
print(grocery_list)

# how about removing last item?
popped_item = grocery_list.pop() # this method returns the removed item
print(popped_item)
# my list is now shorter
print(grocery_list)

# alternative to shorten a list would be to use slice
grocery_list = grocery_list[:-1] # so overwrite the list with shorter list
print(grocery_list) # no more vinegar which was last item

sub_list = grocery_list[1:3]
print(sub_list)