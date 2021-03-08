import math

def sum_prod(*seqs):
    my_sum = 0
    for seq in seqs:  
        my_sum += math.prod(seq)
    return my_sum
 
if __name__ == "__main__":
    seq_a = [2,3]
    seq_b = [5,10,2]
    seq_c = [1,3,2]
    print(sum_prod(seq_a,seq_b,seq_c))