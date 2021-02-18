# my_nums = list(range(20))
my_nums = list(range(5,26,3))
print(my_nums)

# mylist = [1,2,3,10,20,3022.44324,342.11]
# new_list = [n+100 for n in mylist]  # this will create a copy of mylist
# # same as
# new_list_2 = []
# for n in mylist:
#     new_list_2.append(n)

# print(mylist)    
# print(new_list)    
# print(new_list_2) 
# # a bit hacky not that often used
# res = [print(n) for n in mylist] 
# print(res)  
# # filter
# new_list_even = [n+100 for n in mylist if n % 2 == 0]
# print(new_list_even)

# new_list = []
# for n in range(10):
#     new_list.append(n)
#     new_list.append(n+0.5)
# print(new_list)

# n_list = [[n,n+0.5] for n in range(10)]
# print(n_list)
# # this recipe will flatten 2D list into 1d list but not that easy to read
# flat_list = [item for sublist in n_list for item in sublist]
# print(flat_list)

# flat_2 = [n+a for n in range(10,16,2) for a in range(100,105)]
# print(flat_2)