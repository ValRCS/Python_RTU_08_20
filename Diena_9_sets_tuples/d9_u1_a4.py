# def get_min_avg_max(sequence):
#     my_list = sorted(sequence)
#     return my_list[0], sum(my_list)/len(my_list), my_list[-1]

def get_min_avg_max(sequence, precision=2):
    return min(sequence),round(sum(sequence)/len(sequence), precision),max(sequence)

print(get_min_avg_max([0,10,1,9]))
print(get_min_avg_max({0,100,11,99}))
print(get_min_avg_max((0,1000,111,999,10)))
print(get_min_avg_max([0,10,1.553252,9]))
print(get_min_avg_max([0,10,1.553252,9], 3))
# even better
print(get_min_avg_max([0,10,1.553252,9], precision=3))

## Uzdevums 1b
def get_min_med_max(sequence):
    if isinstance(sequence, tuple):
        sequence = list(sequence)
    sorted_seq = sorted(sequence)
    seq_len = len(sorted_seq)
    mid_index = seq_len // 2
    if seq_len % 2 == 0: # even
        if isinstance(sequence[0], str):
            median_val = (sorted_seq[mid_index - 1] + sorted_seq[mid_index])[:2]
        else:
            median_val = (sorted_seq[mid_index - 1] + sorted_seq[mid_index]) / 2
    else:
        median_val = sorted_seq[mid_index]
    min_val = sorted_seq[0]
    max_val = sorted_seq[-1]
    return min_val, median_val, max_val

result = get_min_med_max([1,5,8,4,3])
print(result)  # izprintē (1, 4, 8)

result = get_min_med_max([2,2,9,9,4,3])
print(result)  # izprintē (2, 3.5, 9)

result = get_min_med_max("baaac")
print(result)  # izprintē ('a', 'a', 'c')

result = get_min_med_max("faaacb")
print(result)  # izprintē ('a', 'ab', 'f')

result = get_min_med_max("Valdis")
print(result)  