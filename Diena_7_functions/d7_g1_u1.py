#  Lielais rezultāts
def add_mult(a,b,c):
    my_list=[a,b,c]
    list_sort = (sorted(my_list))
#    print (list_sort)
    result = (list_sort[0]+list_sort[1])*list_sort[2]
    print(f"({list_sort[0]}+{list_sort[1]})*{list_sort[2]}={result}")
    return result
a = int(input("Ievadi 1. skaitli: "))
b = int(input("Ievadi 2. skaitli: "))
c = int(input("Ievadi 3. skaitli: "))
add_mult(a,b,c)5