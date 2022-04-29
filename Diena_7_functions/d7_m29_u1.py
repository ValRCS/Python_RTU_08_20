# Lielais rezultāts
# def add_mult(n1,n2,n3):
#     my_list=[n1,n2,n3]
#     # my_list.sort() # in place sort changes the list
#     list_sort = sorted(my_list)  # OUT OF PLACE returns a new list
#     result = (list_sort[0]+list_sort[1])*list_sort[2]
#     print(f"({list_sort[0]}+{list_sort[1]})*{list_sort[2]}={result}")
#     return result
# # n1 = int(input("Enter number 1: "))
# # n2 = int(input("Enter number 2: "))
# # n3 = int(input("Enter number 3: "))

def add_mult_many(*argv):
    my_list=sorted(argv)  # sorted returns a new list
    # my_list.sort()
    result = (my_list[0]+my_list[1])*my_list[-1]
    print(f"({my_list[0]}+{my_list[1]})*{my_list[-1]}={result}")
    return result


# without sorting
def add_mult(a: float = 0, b: float = 0, c: float = 0) -> float:
    """
    Funkcija add_mult. Funkcijai vienmēr tiks padoti skaitliski parametri, tipus nepārbaudīt.
    :param a: Pirmais skaitliskais parametrs;
    :param b: Otrais skaitliskais parametrs;
    :param c: Trešais skaitliskais parametrs;
    :return: Atgriež rezultātu, kas ir 2 mazāko argumentu summa reizināta ar lielāko argumenta vērtību.
    """
    if a > b and a > c:
        return a * (b + c)
    if b > a and b > c:
        return b * (a + c)
    return c * (b + a)  # if c > b and c > a

print(add_mult(2,6,5))
print(add_mult_many(2,6,5))
print(add_mult_many(1,30,6,1000,5,2))
