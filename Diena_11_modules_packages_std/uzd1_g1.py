import math
# from math import prod


def sum_prod(seq_a, seq_b):
    result = math.prod(seq_a)+math.prod(seq_b)
    return result


print(sum_prod([2, 3], [5, 10, 2]))


def sum_prod_all(*seq_n):
    end_result = 0

    for x in seq_n:
        end_result += math.prod(x)

    return end_result


print(sum_prod_all([2, 3], [5, 10, 2]))
