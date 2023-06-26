# def get_min_avg_max(sequence:tuple) -> tuple:
 
#     return min(sequence),sum(sequence)/len(sequence),max(sequence)
 
# print(get_min_avg_max([0,10,1,9]))

# Sets & Tuples - 1 #
 
def get_min_avg_max(sequence):
    # so if we have any sequence
    # and if it is tuple or list
    # then we can get min, avg, max
    if sequence and type(sequence) in (tuple, list):
        minimum = min(sequence)
        average = sum(sequence) / len(sequence)
        maximum = max(sequence)
        return minimum, average, maximum
 
    return None

print(get_min_avg_max([0,10,1,9]))
print(get_min_avg_max((0,10,1,9)))
# how about set?
print(get_min_avg_max({0,10,1,9}))
# how about string?
print(get_min_avg_max("hello"))