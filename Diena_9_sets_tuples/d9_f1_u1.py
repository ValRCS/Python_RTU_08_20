import statistics 

my_tuple =(0,10,1,5)
def get_min_avg_max(my_tuple):
    return min(my_tuple),int(sum(my_tuple)/len(my_tuple)),max(my_tuple)
res=get_min_avg_max(my_tuple)
print(res)

def get_min_med_max(sequence):
    sorted_sequence = sorted(sequence)
    if isinstance(sequence, str):
        if len(sequence) % 2 == 0:
            median_str = sorted_sequence[int((len(sequence)/2)-1)] + sorted_sequence[int((len(sequence))/2)]
            my_tuple = (sorted_sequence[0], median_str, sorted_sequence[-1])
    else:
        my_tuple = (sorted_sequence[0], statistics.median(sorted_sequence), sorted_sequence[-1])
    return my_tuple

print(get_min_med_max(my_tuple))

