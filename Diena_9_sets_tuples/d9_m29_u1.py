# from statistics import mean
import statistics
 
# def get_min_avg_max(sequence):
#     vector = (min(sequence), mean(sequence), max(sequence), )
#     return vector

def get_min_avg_max(sequence):
    avg = round(sum(sequence) / len(sequence), 2)
    return min(sequence), avg, max(sequence)
 
# def get_min_med_max(seq):
#     # seq.sort() # in place sort of list
#     # return seq[0], statistics.median(seq), seq[-1]
#     return min(seq), statistics.median(seq), max(seq)

def get_min_med_max(sequence):
    if all(isinstance(i, (int, float)) for i in sequence) or type(sequence) == str:
        len_sequence = len(sequence)
        is_odd = len_sequence % 2 != 0
        mid_idx = int((len_sequence + 1)/2) - 1
        mid_idx_left = int((len_sequence)/2) - 1
        sort_sequence = sorted(sequence)
        if is_odd:  
            my_median = sort_sequence[mid_idx]
        elif type(sequence) != str:
            my_median = sum(sort_sequence[mid_idx_left:mid_idx_left + 2])/2
        else:
            my_median = sort_sequence[mid_idx_left] + sort_sequence[mid_idx_left + 1]
        return min(sequence), my_median, max(sequence)
    raise ValueError("Unsupported input!")

test = [1, 2, 3, 4, 5, 10, 20, 25, 32]
 
print(get_min_avg_max(test))