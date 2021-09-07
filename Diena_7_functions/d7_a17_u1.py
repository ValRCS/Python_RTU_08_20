# 1. Lielais rezultāts
# def add_mult(a: int, b: int, c: int) -> int:
#     add_mult_list = sorted([a,b,c])
#     result = (add_mult_list[0]+add_mult_list[1])*add_mult_list[2]
#     print(f"({add_mult_list[0]}+{add_mult_list[1]})*{add_mult_list[2]}={result}")
#     return result



a = float(input("a= "))
b = float(input("b= "))
c = float(input("c= "))
def add_mult(a: int, b: int, c: int) -> int:
    A = [a,b,c]
    A = sorted(A)
    a = A[0]
    b = A[1]
    c = A[2] 
    result = (a+b)*c
    print(f"({a}+{b})*{c}={result}")
    return result

print(add_mult(2,5,4))
print(add_mult(a,b,c))