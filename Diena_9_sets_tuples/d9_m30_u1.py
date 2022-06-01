# Ex 1
import statistics
 
# def get_min_avg_max(sequence):
#     # sequence.sort()
#     my_min = min(sequence)
#     my_max = max(sequence)
#     total = sum(sequence)
#     # for el in sequence:
#     #     total += el
#     avg = round(total/len(sequence))
#     return (min, avg, max)
 
# print(get_min_avg_max([0, 10, 1, 9]))

def get_min_avg_max(sequence):
    seq = tuple(sequence)
    average = sum(seq)/len(seq)
    return min(seq), average, max(seq) 
 
my_list = [1, 6, 4, 8, 9, 3, 9, 3,301] 
print(f"Min, Avg, Max {get_min_avg_max(my_list)}")

# 1.B. Min, Med, Max

def get_min_med_max(sequence):
  mylist = []
  if isinstance(sequence, str):
    mylist[:0]=sequence
  else:
    mylist = sequence
  mylist.sort()
  min_val = mylist[0]
  max_val = mylist[-1]
  middle_val = int(len(mylist)/2)
  if len(mylist) % 2 == 0:
    if isinstance(sequence, str):
      med_val = mylist[middle_val-1] + mylist[middle_val]
    else:
      med_val = (mylist[middle_val-1] + mylist[middle_val]) / 2
  else:
    med_val = mylist[middle_val]
  
  return min_val, med_val, max_val


sequence = [0,10,1,9]
sequence = [1,5,8,4,3]
sequence = [2,2,9,9,4,3]
# sequence = "baaac"
# sequence = "faaacb"
print(f"get_min_med_max({sequence}) = {get_min_med_max(sequence)}")


def get_min_median_max(sequence):
    # for numbers only
    # add string check here
    return min(sequence), statistics.median(sequence), max(sequence)

print(f"get_min_med_max({sequence}) = {get_min_median_max(sequence)}")


