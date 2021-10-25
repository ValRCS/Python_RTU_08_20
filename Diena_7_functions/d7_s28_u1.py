#1.uzdevums (var 1)
# num1 = int(input("Enter Number1: "))
# num2 = int(input("Enter Number3: "))
# num3 = int(input("Enter Number3: "))
num1, num2, num3 = 5, 10, 3 


def add_mult(num1, num2, num3):
    my_list = [num1, num2, num3]
    my_list.sort()
    step1 = sum(my_list[:2])  # could use my_list[0]+my_list[1]
    step2 = my_list[-1]
    result = step1*step2
    return result
print(f"For numbers {num1} {num2} {num3} Result is:", add_mult(num1, num3, num2))