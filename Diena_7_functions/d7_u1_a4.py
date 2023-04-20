# Piemērs add_mult(2,5,4) -> atgriezīs (2+4)*5 = 30
# x,y,z
def add_mult(x:float,y:float,z:float) -> float:
    my_list=[x,y,z]    
    my_list.sort()
    result = (my_list[0]+my_list[1])*my_list[2]
    print(f"({my_list[0]}+{my_list[1]})*{my_list[2]}")
    return result
 
print(add_mult(2,5,4))


# we could rewrite this function to take infinite number of arguments
# *args - infinite number of arguments
def add_mult_infinite(*args) -> float:
    my_list=list(args)
    my_list.sort()
    result = (my_list[0]+my_list[1])*my_list[-1]
    print(f"({my_list[0]}+{my_list[1]})*{my_list[-1]}")
    return result

print(add_mult_infinite(1_000,2,5,4,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20))

# we could have built this function to take a single list
def add_mult_list(my_list) -> float:
    # my_list = my_list.copy()
    # my_list.sort() # IN PLACE!
    my_list = sorted(my_list) # here our inner list is sorted, original list stays the same
    result = (my_list[0]+my_list[1])*my_list[-1]
    print(f"({my_list[0]}+{my_list[1]})*{my_list[-1]}")
    return result


new_list = [1,2,3,4,5,77,6,7,8,9,10]
print(add_mult_list(new_list))
print(new_list)