# def  get_min_avg_max(sequence):
#     my_list=list(sequence)
#     avg_my_list=sum(my_list)/len(my_list)
#     return min(sequence), (avg_my_list), max(sequence)
# print(get_min_avg_max([0,10,1,9,3]))
import math

def get_min_med_max(sequence):
    my_list = sorted(list(sequence))
    # find_middle = math.ceil(len(my_list)/2)
    find_middle = len(my_list)//2 # // tirais atlikums
 
    if len(sequence) % 2 == 0:
        med = (my_list[find_middle-1] + my_list[find_middle])/2
    else:
        med = my_list[find_middle]
 
    return min(sequence), med, max(sequence)
 
response = get_min_med_max([1,5,8,4,3])
print(response)
response = get_min_med_max([2,2,9,9,4,3])
print(response)
response = get_min_med_max([2,2,1,1,9,9,4,3])
print(response)