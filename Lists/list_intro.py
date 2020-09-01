# https://docs.python.org/3/tutorial/introduction.html#lists
my_list = [1, 2, 3, "Valdis", True, False, None, 3.1415]
print(my_list)
my_list[0]
my_list[-1]
my_list[3:-2]
my_list[3:-1]
my_list[::-1]
# generally lists work best with same value types
# num_list = [1,2,3,4]
num_list = list(range(1, 5))
num_list
dec_list = list(range(10, 40+1, 5))
dec_list
big_list = num_list + dec_list
big_list
big_list += num_list  # same as big_list = big_list + num_list
big_list
# append for adding non list items to list
big_list.append(9000)  # in place meaning big_list gets changed
big_list
# and also append will nest a list within list
# different fromo big_list += num_list
big_list.append(num_list)
big_list
big_list[-2]
big_list[-1]
big_list[-1][-2], big_list[-1][2]
len(big_list)
max(num_list), min(num_list)
# will not work because different data types inside big_list
max(big_list)
# go through all items(elements) in list
for item in big_list:
    print(item)

# use enumerate if we need index
for i, n in enumerate(dec_list):
    print(f"{i=} : {n=}")
