import statistics

def get_min_avg_max(sequence):
    # avg = round(sum(sequence) / len(sequence), 4)
    avg = int(sum(sequence) / len(sequence))
    return min(sequence), avg, max(sequence)

print(get_min_avg_max([0, 10, 1, 9, 4]))
my_min, my_avg, my_max = get_min_avg_max(range(10))
print(my_min, my_avg, my_max)

my_tuple = get_min_avg_max(range(20))
print(my_tuple[0], my_tuple[1], my_tuple[2])

def median(sequence):
    sorted_sequence = sorted(sequence)
    sequence_Len = len(sequence)
    index = (sequence_Len - 1) // 2
 
    if sequence_Len % 2: # odd
        return sorted_sequence[index]
    else:
        if type(sequence) is str:
            return sorted_sequence[index] + sorted_sequence[index + 1]
        else:
            return (sorted_sequence[index] + sorted_sequence[index + 1]) / 2.0
 

 
def get_min_med_max(sequence):
    return min(sequence), median(sequence), max(sequence)
 
 
print(get_min_med_max([1, 5, 8, 4, 3]))
# Output -> (1,4,8)
print(get_min_med_max([2, 2, 9, 9, 4, 3]))
# Output -> (2,3.5,9)
print(get_min_med_max("baaac"))
# Output -> ('a','a','c')
print(get_min_med_max("faaacb"))
