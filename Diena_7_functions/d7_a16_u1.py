def add_mult(a,b,c,):
    my_list=[a,b,c]    
    my_list.sort()
    count=sum(my_list[:2]) # could write my_list[0]+my_list[1]
    times=my_list[-1]
    result=count*times
    return result
print(add_mult(1,2,3))
print(add_mult(10,30,20))