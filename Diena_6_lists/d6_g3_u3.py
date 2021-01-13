# 3.uzdevums
my_name = str(input('Enter sentence '))
words = my_name.split()
rev_list = [word[::-1] for word in words]
rev_string=" ".join(rev_list)
result=rev_string.capitalize()
print(result)

print(" ".join([w[::-1] for w in my_name.split()]).capitalize())