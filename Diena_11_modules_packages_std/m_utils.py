import math


def sum_prod(seq_a, seq_b):
    res1 = math.prod(seq_a) + math.prod(seq_b)
    return res1
 
 
def sum_prod_multi(*seqs):
    res2 = math.fsum([math.prod(seq) for seq in seqs])
    return res2