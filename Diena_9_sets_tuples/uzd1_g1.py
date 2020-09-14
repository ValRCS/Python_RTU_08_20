# Ludmila
def get_min_avg_max(sequence):
    a = min(sequence)
    b = sum(sequence)/len(sequence)
    c = max(sequence)
    return (a, b, c)


sequence = (6, 9, 15, 10, 22)
print(get_min_avg_max(sequence))
sequence = (0, 10, 1, 9)
print(get_min_avg_max(sequence))


def get_min_med_max(sequence):
    a = min(sequence)
    c = max(sequence)
    if len(sequence) % 2 == 0:
        b = (sequence[(int(len(sequence)/2 - 1))],
             sequence[int(len(sequence)/2)])
    else:
        b = sequence[len(sequence)//2]
    return (a, b, c)


sequence = "marusja"
print(get_min_med_max(sequence))
sequence = [8, 10, 2, 6, 9, 11]
print(get_min_med_max(sequence))
print(get_min_med_max("Valdis"))
