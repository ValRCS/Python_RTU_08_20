# let's look at some more list methods

my_beer_list = ["IPA", "APA", "Stout", "Porter"]
#, "Lager", "Pilsner", "Wheat", "Sour", "Gose", 
# "Bock", "Doppelbock", "Dunkel", "Helles", "Marzen", "Rauchbier", 
# "Schwarzbier", "Weizenbock", "Altbier", "Barleywine", 
# "Bitter", "Brown Ale", "Cream Ale", "Dunkelweizen", "Flanders Red Ale", 
# "Grisette", "Hefeweizen", "Kolsch", "Lambic", "Mild Ale", "Old Ale",
#  "Pale Ale", "Red Ale", "Saison", "Scotch Ale",
#  "Steam Beer", "Vienna Lager", "Witbier", "Zwickelbier"]

# let's add a new beer to our list
my_beer_list.append("Lager") # IN PLACE method - modifies the list
print(my_beer_list)

# we could also add using + operator OUT OF PLACE method
my_beer_list = my_beer_list + ["Pilsner"] # creates a new list out of old list and new item
print(my_beer_list)

# lets add multiple items to our list
my_beer_list.extend(["Wheat", "Sour", "Gose"]) # IN PLACE method
# we added multiple items to our list
print(my_beer_list)
# compare with append
my_beer_list.append(["Bock", "Doppelbock", "Dunkel"]) # IN PLACE method
# so we added a single list as an item to our list
print(my_beer_list)

# let's remove our last item
unwanted_beers = my_beer_list.pop() # IN PLACE method also returns the removed item
print(unwanted_beers)
print(my_beer_list)

# let's remove our first item
unwanted_beers = my_beer_list.pop(0) # IN PLACE method also returns the removed item
print(unwanted_beers)
print(my_beer_list)

# let's sort our list
my_beer_list.sort() # IN PLACE method
print(my_beer_list) # sorted lexically

# let's sort our list in reverse order
my_beer_list.sort(reverse=True) # IN PLACE method
print(my_beer_list) # sorted lexically

# how about saving a copy of our list?
my_beer_list_copy = my_beer_list.copy() # OUT OF PLACE method
# so called shallow copy - only copies the list but not the items
print(my_beer_list_copy)
# let's create an alias
my_beer_list_alias = my_beer_list # this is not a copy but an alias -
# both variables point to the same list
print(my_beer_list_alias)

# let's change our list
my_beer_list.append("Helles") # copy will not change but alias will
print(my_beer_list)
print(my_beer_list_copy)
print(my_beer_list_alias)

# let's clear our list
my_beer_list.clear() # IN PLACE method - removes all items from the list!!!
print(my_beer_list)

my_beer_list = my_beer_list_copy.copy() # so let's restore our list
# i did lose Helles beer
print(my_beer_list)

# let's find an index of a beer
print(my_beer_list.index("APA")) # returns the index of the first match
# we use try except to handle the case when item is not found
try:
    print(my_beer_list.index("Helles"))
except ValueError:
    print("Helles not found")

# let's count how many times a beer is in our list
print(my_beer_list.count("APA")) # returns the count of the items in the list
# let's add another APA
my_beer_list.append("APA")
print(my_beer_list.count("APA")) # returns the count of the items in the list

print(my_beer_list)
# finally we can insert into our list
my_beer_list.insert(2, "Helles") # IN PLACE method inserts before the index specified
# so index 2 will become the new item rest will be shifted to the right
# this can be slow for large lists
print(my_beer_list)
my_beer_list.reverse() # IN PLACE method reverses the list
# new_reverse_list = reversed(my_beer_list) # OUT OF PLACE method returns a new reversed list
new_reverse_list = my_beer_list[::-1] # OUT OF PLACE method returns a new reversed list

print(my_beer_list)
print(new_reverse_list)
