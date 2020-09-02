my_list = [5, 6, "Valdis", True, 3.65]
print(my_list)
my_list[0]
my_list[1] = 66  # lists are mutable (unlike strings)
my_list[:3]
my_list[-2:]  # last two
my_list[1:4], my_list[1:-1]
my_list[::2]
my_list[1::2]
6 in my_list
66 in my_list
"Valdis" in my_list
# iterate over items
needle = "al"
for item in my_list:
    if type(item) == str and needle in item:
        print(f"Found {needle=} in {item=}")

#
my_list.append("alus")  # in place methods, means we modify the list
my_list

# example how to filter something
find_list = []
for item in my_list:
    if type(item) == str and needle in item:
        print(f"Found {needle=} in {item=}")
        find_list.append(item)
print(f"{find_list=}")
# ps the above could be done simpler with list comprehension

# out of place meaning find_list stays the same
new_list = my_list + ["Kalējs"]
len(new_list), len(my_list)

new_list += ["Malējs"]  # same as new_list = new_list + ["Malējs"]
new_list

new_list[-1]
last = new_list.pop()  # also in place meaning i destroyed the last value
last, new_list
new_list.append(last)
new_list

numbers = [1, 4, -5, 3.16, 10, 9000, 5]
saved_sort_asc = sorted(numbers)  # out of place does not modify numbers
saved_sort_asc
sorted(numbers, reverse=True)  # out of place does not modify numbers
numbers
numbers.sort()  # in place meaning it modifies the numbers
numbers
numbers.remove(9000)  # will remove in place first 9000 found in the list
numbers
min(numbers), max(numbers)
sum(numbers)
total = 0
for n in numbers:
    total += n
print(total)
sentence = "Quick brown fox jumped over a sleeping dog"
words = sentence.split()
print(words)
words[2] = "bear"
print(words)
new_sentence = " ".join(words)
print(new_sentence)
food = "kartupelis"
letters = list(food)  # list with all letters
print(letters)
letters[5] = "m"
new_word = "".join(letters)
print(new_word)

new_list = []
for word in words:
    new_list.append(word.capitalize())
print(new_list)
# list comprehension same as above
new_list_2 = [w.capitalize() for w in words]
print(new_list_2)
filtered_list = [w for w in words if w.startswith("b")]
filtered_list
filtered_list_2 = [w for w in words if w[0] == "b"]
filtered_list_2
filtered_list_3 = [w.upper() for w in words if w[0] == "b"]
filtered_list_3

numbers = list(range(10))
print(numbers)
squares = []
for n in numbers:  # could also use range(10)
    squares.append(n*n)
print(squares)
squares_2 = [n*n for n in range(10)]
print(squares_2)
even_squares = [n*n for n in range(10) if n % 2 == 0]
even_squares

food
char_codes = [ord(c) for c in food]
char_codes
char_codes_list = [[f"Char:{c}", ord(c)] for c in food]
char_codes_list
print(char_codes_list[0])
print(char_codes_list[0][0])
print(char_codes_list[-1])
print(char_codes_list[-1][-1])
