# a1 = 5
# a2 = 6
# a3 = 7
my_list = [5, 6, 7]
print(my_list)
my_list[0]
gen_list = my_list + ["Valdis", "Līga", True, 3.14]
print(gen_list)
print(min(my_list), max(my_list))
sum(my_list)
sum(gen_list)
gen_list
gen_list[:3]
gen_list[-3:]
gen_list
gen_list[1::2]
gen_list[1:4:2]
gen_list[::-1]
6 in gen_list
8 in gen_list
"Valdis" in gen_list
"al" in gen_list
needle = "al"
for item in gen_list:
    if type(item) == str and needle in item:
        print(f"Found {needle=} in {item=}")

gen_list.append("alus")  # in-place modifies gen_list
gen_list
gen_list += "kalējs"  # this will be a bit surprising result
gen_list.index("k")
gen_list = gen_list[:8]
# out of place meaning we need to assign to some variable
gen_list += ["kalējs"]  # gen_list = gen_list + ['kalējs']
gen_list

find_list = []
for item in gen_list:
    if type(item) == str and needle in item:
        print(f"Found {needle=} in {item=}")
        find_list.append(item)
print(find_list)
# above could be done with list comprehensions a little simpler
len(gen_list), len(find_list)
find_list[-1]
last_one = find_list.pop()  # in place deletes last item
last_one
find_list

numbers = [1, 4, -5, 3.16, 10, 9000, 5]
sorted_num_asc = sorted(numbers)  # out of place does not modify
sorted_num_asc
sorted_num_desc = sorted(numbers, reverse=True)
sorted_num_desc  # of course we could have done sorted_number_asc[::-1]
numbers.sort()  # in place modifies numbers
numbers
numbers.remove(10)  # find first element containing 10!!
numbers
min(numbers), max(numbers), sum(numbers)
# how to find 2nd largest
numbers = [1, 4, -5, 3.16, 10, 9000, 5]
sorted(numbers)[-2]
numbers[-2]

total = 0
for n in numbers:
    total += n
print(total)
print(sum(numbers))

sentence = "Quick brown fox jumped over a sleeping dog"
word_list = sentence.split()  # by default splits on whitespace
word_list
# lists are mutable unlike strings!
word_list[2] = "bear"
word_list
new_sentence = " ".join(word_list)  # crucial that we are joining all strings
new_sentence
food = "kartupelis"
letters = list(food)
letters
letters[5] = "M"
letters
# new_food = " :X: ".join(letters)
new_food = "".join(letters)
new_food

numbers = list(range(10))
numbers
squares = []
for n in numbers:
    squares.append(n**2)
squares
# list comprehension to replace above code
squares_2 = [n**2 for n in numbers]
squares_2

char_codes = [ord(c) for c in food]
char_codes
char_codes_list = [[c, ord(c)] for c in food]
char_codes_list
char_codes_list[0]
char_codes_list[0][0]
char_codes_list[-1]
char_codes_list[-1][-1]
