# def add_mult(arg1, arg2, arg3):
#     my_list = [arg1, arg2, arg3]
#     my_list.sort() #in place sort modifies my_list
#     # result = (sum(my_list[:2]))*max(my_list)
#     result = (sum(my_list[:2]))*my_list[-1] # faster than max for already sorted list
#     print(f"({my_list[0]}+{my_list[1]})*{max(my_list)} = {result}")
#     return result
 
# save = add_mult(2, 5, 4)
# print(save)

import heapq

def add_mult_advanced(*argv):
    my_list = sorted(argv) #argv is a tuple(which is immutable list type structure)

    # print(f"(sum of {heapq.nsmallest(len(my_list)-1,my_list)})*{max(my_list)} = {(sum(heapq.nsmallest(len(my_list)-1,my_list))) * max(my_list)}")
    print(sum(my_list[:-1])*my_list[-1])

add_mult_advanced (2,4,7,8,10)