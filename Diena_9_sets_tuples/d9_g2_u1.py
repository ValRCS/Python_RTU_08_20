from statistics import mean, median
a = [2, 2, 9, 9, 4, 7, 85]
 
def get_min_avg_max(a):
    b = tuple([min(a), mean(a), max(a)])
    return(b)
print(get_min_avg_max(a))
 
def get_min_med_max(a):
    return min(a), median(a), max(a)
print(get_min_med_max(a))

print(get_min_med_max([1,2,3,4,4,26]))