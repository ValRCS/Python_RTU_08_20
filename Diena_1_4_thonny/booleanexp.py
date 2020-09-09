print(5 == 5)
is_equal = 2*2 == 4
print( 10 != 15)
print( 200 != 200)
a = 5
b = int(2 * 2.5)
c = 2 * 2.5
print(a == b, b == c, c == a)
print(a != b, b != c)
big_num = 9000
print(a > big_num, big_num > a)
print(a < big_num, big_num < a)
name = "Voldemars"
my_name = "Valdis"
print(my_name > name, my_name < name)
name = name.upper()
print(my_name > name, my_name < name)
d = 6
print(a >= 5, a <= b, a <= c, d >= a)
# last we can check object equality
print(a is b, b is c, c is a)
print(id(a) == id(b))
print(len("Valdis") == 6)
