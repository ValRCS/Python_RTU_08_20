# 2.1 Min, Avg, Max
# Uzrakstiet funkciju get_min_avg_max(sequence), kas atgriež tuple ar trīs vērtībām attiecīgi mazāko,
# aritmētisko vidējo un lielāko vērtību no virknes.
 
def get_min_avg_max(sequence):
    minimum = min(sequence)
    maximum = max(sequence)
    average = sum(sequence) / len(sequence)
    return minimum, average, maximum
 
sequence = [0, 10, 1, 9]
result = get_min_avg_max(sequence)
print(result)  # (0, 5, 10)

# alternative allow unlimited arguments
def get_min_avg_max_args(*args):
    minimum = min(args)
    maximum = max(args)
    average = sum(args) / len(args)
    return minimum, average, maximum

# difference will be in how we pass in arguments
result = get_min_avg_max_args(0, 10, 1, 9) # so we pass in arguments one by one
print(result)  # (0, 5, 10)
# if we already have a list we can use * to unpack/unroll it
sequence = [0, 10, 1, 9]
result = get_min_avg_max_args(*sequence) # so we pass in arguments one by one
print(result)  # (0, 5, 10)