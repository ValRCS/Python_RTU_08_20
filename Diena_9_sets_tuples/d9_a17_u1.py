def getMinMax(my_num_list):
    return min(my_num_list), int(sum(my_num_list)/len(my_num_list)), max(my_num_list)

print(getMinMax([0,10,1,9,]))

print(getMinMax((6,2,6,7,2,67)))

# print(getMinMax("Valdis")) # we can't divide a string

print(getMinMax(range(10,50)))

# def get_min_med_max(my_num):
#     my_list = sorted(list(my_num))
#     even = 0
#     if len(my_list) % 2 == 0:
#         even = (my_list[int((len(my_list)+1)/2-1)]+my_list[int((len(my_list)+1)/2)])/2
#         print(my_list[int((len(my_list)+1)/2)])
 
#     else: 
#         even = my_list[int((len(my_list))/2)]    
 
 
#     return min(my_num), even, max(my_num)

def get_min_med_max(seq):
    sort_seq = sorted(seq)
    print(sort_seq)
    median = 2
    
    if len(sort_seq)%2==1:
        median = int((len(sort_seq))/2)
        median = sort_seq[median]
    else:
        median_1 = int((len(sort_seq))/2)
        median_2 = median_1 - 1
        if type(seq) == str:
            median = (sort_seq[median_2] + sort_seq[median_1])
        else: 
            median = (sort_seq[median_1] + sort_seq[median_2])/2
 
    
 
    return min(seq), median, max(seq)
 
print(get_min_med_max((0,10,1,9, 5, 7)))
print(get_min_med_max([0,10,1,9]))
print(get_min_med_max("baac"))
       
print(get_min_med_max([2, 2, 9, 9, 4, 3]))
print(get_min_med_max([2, 2, 9 , 4, 3]))