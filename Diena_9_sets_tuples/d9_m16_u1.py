# 1. Min, Avg, Max
"""Uzrakstiet funkciju get_min_avg_max(sequence), kas atgriež tuple ar trīs vērtībām attiecīgi mazāko, aritmētisko vidējo un lielāko vērtību no virknes.
get_min_avg_max([0,10,1,9]) -> (0,5,10)
ienākošā sequence var būt tuple vai list ar skaitliskām vērtībām. 
"""
def get_min_avg_max(sequence:list):
    
    return min(sequence),sum(sequence)/len(sequence),max(sequence)
 

def get_min_med_max(sequence:list):
    if type(sequence)==str:
        sequence=list(sequence)
        sorted_seq = sorted(sequence)
        # even string length requires extra work for median
        if len(sequence)%2==0:
            return sorted_seq[0],sorted_seq[len(sequence)//2-1]+sorted_seq[len(sequence)//2],sorted_seq[-1]

    import statistics
    return min(sequence),statistics.median(sequence),max(sequence)
 
print(get_min_avg_max([0,10,1,9]))
 
print(get_min_med_max([1,5,8,4,3]))
 
print(get_min_med_max([2,2,9,9,4,3]))
 
print(get_min_med_max("baaac"))

print(get_min_med_max("faaacb"))
print(get_min_med_max("āfaaacbg"))