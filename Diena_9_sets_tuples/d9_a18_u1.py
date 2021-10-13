import statistics

def get_min_avg_max(sequence):
    return min(sequence),round(sum(sequence)/len(sequence), 2),max(sequence), 
res = get_min_avg_max([0,10,1,9])
print(res)
print(type(res))

def get_min_med_max(sequence):
    try:
        med = statistics.median(sequence)
    except:
        print("statistics will not work, we have to do the work ourselves")
        new_tuple = tuple(sorted(sequence))
        val_1 = new_tuple[len(new_tuple)//2-1]
        val_2 = new_tuple[len(new_tuple)//2]
        med = ''.join([val_1, val_2])
    return min(sequence), med, max(sequence)

print(get_min_med_max([1,5,8,4,3]))
print(get_min_med_max([2,2,9,9,4,3]))
print(get_min_med_max("baaac"))
print(get_min_med_max("faaacb"))