# 3. uzdevums
# a = float(input("a"))
# b = float(input("b"))
# c = float(input("c"))
# if a >= b >= c:
#     print(f"{a},{b},{c}")
# elif a >= c >= b:
#     print(f"{a},{c},{b}")
# elif b >= a >= c:
#     print(f"{b},{a},{c}")
# elif b >= c >= a:
#     print(f"{b},{c},{a}")
# elif c >= a >= b:
#     print(f"{c},{a},{b}")
# elif b >= c >= a:
#     print(f"{b},{c},{a}")
    
# bonuss 3. uzdevums izmantojot cilpu elementu ievadīšanai un listes elementu sortēšanu
# lst = []
# n = int(input("Element count to sort: "))
# for i in range(n):
#     ele = int(input(f"Please input element nr. {i+1}: "))
#     lst.append(ele)
# print(*sorted(lst))

a = 2020
b = 2021
a, b = b, a # this is called tuple unpacking