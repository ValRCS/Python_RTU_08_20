mylist = [1,2,3,10,20,3022.44324,342.11]
new_list = [n+100 for n in mylist]  # this will create a copy of mylist
# same as
new_list_2 = []
for n in mylist:
    new_list_2.append(n)

print(mylist)    
print(new_list)    
print(new_list_2) 
# a bit hacky not that often used
res = [print(n) for n in mylist] 
print(res)  