number_input = int(input("ievadiet cik pirmskaitļus gribat izvadīt"))
 
lst = []
increasing_number = 2
loop_cycle = 2
test_operand = 0
while len(lst) < number_input:
 
    for loop_cycle in range(2, increasing_number):
 
        if increasing_number % loop_cycle == 0:
            test_operand += 1
 
    if test_operand == 0:
        lst.append(increasing_number)
 
    increasing_number += 1
    test_operand = 0
print(lst)