# 1.a Vidējā vērtība
 
# Uzrakstīt programmu, kas liek lietotājam ievadīt skaitļus(float).
 
# Programma pēc katra ievada rāda visu ievadīto skaitļu vidējo vērtību.
 
# PS. 1a var iztikt bez lists
 
# 1.b Programma rāda gan skaitļu vidējo vērtību, gan VISUS ievadītos skaitļus
 
# PS Iziešana no programmas ir ievadot "q"
# 1.c Programma nerāda visus ievadītos skaitļus bet gan tikai TOP3 un BOTTOM3 un protams joprojām vidējo.
def average(lst):
    return sum(lst) / len(lst)

# theres is built in statistics module
# import statistics
# print(statistics.mean([1, 2, 3, 4, 5]))
 
 
numbers = []
while True:
    try:
        number = input("\nievadi skaitli vai q lai izietu: ")
        # Exit if blank
        if number == "q":
            break
        numbers.append(float(number))
        # i want to sort after I add a new number
        numbers.sort() # sorting in general is slow O(n log n) where n is nmber of elements
        # however Timsort used by Python is very fast on partially sorted lists
        print("Visi skaitļi sarakstā:", end=" ")
        print(*numbers, sep=', ')
        # print(f"Pirmie 3: { print(*numbers[:3], sep=', ') }")
        print(f"Pirmie 3: {numbers[:3]}")
        # print(f"Pēdējie 3: { print(*numbers[-3:], sep=', ') }")
        print(f"Pēdējie 3: {numbers[-3:] }")
        print(f"Vidējā vērtība: {average(numbers)}")
    except ValueError:
        print("Lūdzu ievadi skaitlisku vērtību")

