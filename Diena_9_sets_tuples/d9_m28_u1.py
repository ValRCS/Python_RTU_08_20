import statistics
#1. uzdevums
def get_min_avg_max(sequence):
    my_list=list(sequence) # not strictly required
    avg_my_list=round(sum(my_list)/len(my_list),2)
    also_average = statistics.mean(my_list)
    return min(sequence), avg_my_list, also_average, max(sequence)
print(get_min_avg_max([0,10,1,9,450]))

def get_min_med_max(sequence):
    result = (min(sequence), statistics.median(sequence), max(sequence))
    print(result)
    return result

this_tuple = (5, 5, 7, 7, 1, 2, 2, 2, 3, 4)
print(get_min_med_max(this_tuple))
print(get_min_avg_max(this_tuple))