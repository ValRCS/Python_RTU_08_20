def get_min_avg_max(sequence):
    return (min(sequence), sum(sequence)/len(sequence), max(sequence))


def get_min_med_max(sequence):
    size_of_input = len(sequence)
    half_size = int(size_of_input/2)
    sequence = sorted(sequence)
    if size_of_input % 2 == 1:
        median = sequence[half_size]
    else:
        if all(isinstance(item, int) for item in sequence) == False:
            median = sequence[half_size - 1] + sequence[half_size]
        else:
            median = sum(sequence[half_size - 1:half_size + 1]) / 2
    return (min(sequence), median, max(sequence))

print(get_min_med_max([1,5,8,4,3]))
print(get_min_med_max([2,2,9,9,4,3]))
print(get_min_med_max("faaacb"))