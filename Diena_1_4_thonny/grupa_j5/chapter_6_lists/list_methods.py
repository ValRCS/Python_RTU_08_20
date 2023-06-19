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