import string

for lower, upper, number in zip(string.ascii_lowercase, string.ascii_uppercase, range(20)):
    print(lower, upper, number)

my_list = list(zip(string.ascii_lowercase, string.ascii_uppercase, range(20)))

print(my_list)