# Tuples & Sets 01
 
def get_min_avg_max(sequence):
    # temp_list = list(sequence)
    # temp_list.sort() # sorting is not free
    # min_val = temp_list[0]
    # max_val = temp_list[-1]
    # avg_val = round(sum(temp_list) / len(temp_list), 2) # round 2 digits to decimal
    # a bit faster will be to use min max sum functions
    min_val, avg_val, max_val = min(sequence), sum(sequence) / len(sequence), max(sequence)

    return min_val, avg_val, max_val # return values as tuple
 
my_list = [10,-200,30,4, 1000]
print(get_min_avg_max(my_list))

# lets write our own min function
def my_min(sequence):
    my_min = sequence[0]
    for item in sequence[1:]:
        if item < my_min:
            my_min = item
    return my_min # so go through only once