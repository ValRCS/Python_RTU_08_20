def get_min_avg_max(my_numbers):
    return min(my_numbers), sum(my_numbers)/len(my_numbers), max(my_numbers)
res = get_min_avg_max([2, 4, 2, 7, 9])
print(res)

def  get_min_med_max(seq):
    sorted_seq = sorted(seq)
    med_num = len(sorted_seq)
    mid_index = int(med_num/2)
    if med_num%2 == 1:
        med = sorted_seq[mid_index]
    else: # even number
        ####### Šeit vajag funkciju lai dabūt "med_num" ka int
        # extra = (med_num)/2 - 0,5
        # pos = int((seq[extra] + seq[extra+1])/2)
        if type(seq[0]) is str:
            return min(seq), sorted_seq[mid_index-1]+sorted_seq[mid_index] ,max(seq)
        med = (sorted_seq[mid_index-1]+sorted_seq[mid_index])/2
    return min(seq), med, max(seq)
 
print(get_min_med_max([2,6,15,7,4]))
res_2 = get_min_med_max([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(res_2)
print(get_min_med_max([10, 2, 3, 4, 5, 6, 7, 8, 9, 1]))
print(get_min_med_max("baedc"))
print(get_min_med_max("bfaedc"))