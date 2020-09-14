# with set we give an iterable
char_set = set("abracadabra")
char_set
# with {} syntax we give each element
item_set = {"abra", "dabra", "abracadbra", "abra"}
print(item_set)
item_set_2 = set(["abra", "dabra", "abracadbra", "abra"])
print(item_set_2)
len(char_set)
for c in char_set:
    print(f"{c=}")

# we can cast from set to list
char_list = list(char_set)
char_list = sorted(char_list)
print(char_list)
char_string = "".join(char_list)
print(char_string)
print("|".join(char_set))

set("aaabcrddd") == set("abracadabra")

numbers = set(range(12))
print(numbers)

n3_7 = set(range(3, 8))
print(n3_7)
5 in numbers, 5 in n3_7

# below two are equal
n3_7.issubset(numbers)
n3_7 <= numbers  # this lets you have equal sets
n3_7 < numbers  # this will be false if both sets are equal

# below two are euqal
numbers.issuperset(n3_7)
numbers >= n3_7
numbers > n3_7

n5_9 = set(range(5, 10))
print(n5_9)

# below two are equal
n3_7 | n5_9
n3_7.union(n5_9)
n3_9 = n3_7 | n5_9 | {5, 2, 6, 111}  # i could chain union more sets here
print(n3_9)
n3_9 = n3_7 | n5_9 | {5, 2, 6, 111} | set(
    [-5, 5, 100, 200])  # i could chain union more sets here
print(n3_9)

n5_7 = n3_7 & n5_9 & {6, 7}
n3_7.intersection(n5_9)
print(n5_7)

n3_4 = n3_7 - n5_9  # this is not simmetrical
print(n3_4)

n8_9 = n5_9 - n3_7  # this is not simmetrical
print(n8_9, n5_9.difference(n3_7))

n_sim = n3_7 ^ n5_9
print(n_sim, n3_7.symmetric_difference(n5_9))

# do the sets below have anything in common?
n3_4.isdisjoint(n8_9)

n_sim.update([3431, 21, 452, 1, 3, 5, 6])
print(n_sim)
print(sorted(n_sim))
type(sorted(n_sim))
type(n_sim)
n_sim.clear()
print(n_sim)
