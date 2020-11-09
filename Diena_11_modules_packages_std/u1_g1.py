# def sum_prod(seq_a, seq_b) :
#     rezz = [i * j for i in seq_a for j in seq_b] # cartesian product
#     print(rezz)
#     kopa = sum(rezz)
#     return kopa
import math
def sum_prod(seq_a, seq_b):
    result = math.prod(seq_a, start=1000) + math.prod(seq_b)
    return result
 
def sum_prod_many(*seqs):
    # summa = 0
    # for seq in seqs:
    #     summa += math.prod(seq)
    # return summa
    # we can do the above in one line below
    return sum([math.prod(seq) for seq in seqs])

print(sum_prod([2,3],[5,10,2]))

print(sum_prod_many([2,3],[5,10,2],[10,10,100]))