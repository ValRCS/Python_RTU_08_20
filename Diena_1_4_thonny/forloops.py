# for loops
for n in range(10):
    print("Number is", n)
my_name = "Valdis"
for c in my_name:
    print("Letter ", c)    
    
print("This happens after the loop is done")
for n in range(20,25):
    print(n)
for my_num in range(100,110,2): # i can add step to range
    print(my_num)
    
my_name = "Valdis"
for c in my_name:
    print("Letter ", c)
    
my_list = [1,2,100,105,"Valdis","potatoes", 9000, 107.35]
total = 0
big_items = 0
for item in my_list:
    print("Working with item: ", item)
    if type(item) == int or type(item) == float:
        total += item
        if item > 100:
            big_items += 1
            
my_num_list = [1,6,17,7,-6,49,642,6,2,-5555]

my_max = None
for num in my_num_list:
    if my_max == None: # this will happen with first item
        my_max = num
    if num > my_max:
        my_max = num
        
print(max(*my_num_list))
    