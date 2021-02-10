#1a
def get_min_avg_max(sequence):
    
    sequence = tuple(sequence)
    min_vert = min(sequence)
    max_vert = max(sequence)
    avg_vert = sum(sequence)/ len(sequence)
    return min_vert, avg_vert, max_vert 

#1b
def get_min_med_max(my_list):
    if len(my_list)==0:
        return None, None, None
    my_tuple = tuple(sorted(my_list))
    if len(my_tuple) % 2 == 1:
        val_med = my_tuple[(len(my_tuple)-1)//2]
    else:
        val1 = my_tuple[len(my_tuple)//2-1]
        val2 = my_tuple[len(my_tuple)//2]
        try: # could use if to check type(val1) 
            val_med = (val1 + val2)/2
        except:
            val_med = "".join([val1, val2])
            # val_med = [val1, val2] # vai šādi (man šis vairāk patīk)
    return my_tuple[0], val_med, my_tuple[-1]
 
print(get_min_med_max([1,5,8,4,3]))
print(get_min_med_max([2,2,9,9,4,3]))
print(get_min_med_max("baaac"))
print(get_min_med_max("faaacb"))
print(get_min_med_max(list(range(10))+list(range(23,31))))