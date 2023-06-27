# # 1. Min, Avg, Max

# Uzrakstiet funkciju get_min_avg_max(sequence), kas atgriež tuple ar trīs vērtībām attiecīgi mazāko, aritmētisko vidējo un lielāko vērtību no virknes.

# get_min_avg_max([0,10,1,9]) -> (0,5,10)

# ienākošā sequence var būt tuple vai list ar skaitliskām vērtībām. 

def get_min_avg_max(sequence):
    """Returns tuple with min, avg, max values from sequence"""
    return min(sequence), sum(sequence)/len(sequence), max(sequence)

print(get_min_avg_max([0,10,1,9]))

# let's make a function that returns min, median and max from a sequence
def get_min_median_max(sequence):
    """Returns tuple with min, median, max values from sequence"""
    sorted_sequence = sorted(sequence)
    # not quite correct for even number of elements, but good enough for now
    return sorted_sequence[0], sorted_sequence[len(sequence)//2], sorted_sequence[-1]

print(get_min_median_max([0,10,1,9, 5]))
# even number of elements
print(get_min_median_max([0,10,1,9, 5, 7]))

# simple way to fix use statistics module
import statistics
def get_min_median_max(sequence):
    """Returns tuple with min, median, max values from sequence"""
    return min(sequence), statistics.median(sequence), max(sequence)

print(get_min_median_max([0,10,1,9, 5]))
# even number of elements
print(get_min_median_max([0,10,1,9, 5, 7]))

# we also have mode
print(statistics.mode([0,10,1,9, 5, 7, 1, 1]))