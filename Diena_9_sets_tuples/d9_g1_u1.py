# sequence = [0,10,1,9,20,5]
# def get_min_avg_max(sequence):
#     summa = sum(sequence) # would not work on strings
#     my_min = sorted(list(sequence))[0]
#     my_max = sorted(list(sequence))[-1]
#     my_avg = round(summa / len(sequence),1)
#     return my_min, my_avg, my_max
 
# print(get_min_avg_max(sequence))

# b
def get_min_med_max(sequence):
    sequence = tuple(sorted(sequence))
    my_min = sequence[0]
    my_max = sequence[-1]
    my_len = int(len(sequence))
    if my_len % 2 == 0:
        if type(sequence[0]) != str:
            my_med = (sequence[int(my_len/2) - 1] + sequence[int(my_len/2)])/2
            # print(my_med)
        else:
            my_med = (sequence[int(my_len/2)-1] + sequence[int(my_len/2)])
    else:
        my_med = sequence[int(my_len/2)]
    return my_min, my_med, my_max
 
print()
print(get_min_med_max([1,5,8,4,3]),'           should be:  (1,4,8)') 
print(get_min_med_max([2,2,9,9,4,3]),'         should be:  (2,3.5,9)') 
print(get_min_med_max("baaac"),  '''     should be:  ('a','a','c')''') 
print(get_min_med_max("faaacb"),' ''''   should be:  ('a', 'ab', 'f') ''')