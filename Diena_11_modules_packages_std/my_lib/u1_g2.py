import math
 
def sum_prod(seq_a, seq_b):
    result = math.prod(seq_a) + math.prod(seq_b)
    return result
 
def sum_prod_all(*seq_n):
    return sum([math.prod(seq) for seq in seq_n])
    # end_result = 0
 
    # for x in seq_n:
    #     end_result += math.prod(x)
 
    # return end_result
if __name__ == "__main__":
    print(sum_prod_all([2,3], [2,5,10], range(1,5)))
    print(sum_prod_all([2,3], [2,5,10]))
    print(sum_prod_all([2,3]))
    print(sum_prod_all())