from collections import Counter
letters = input("enter words to count letters")
count = Counter(letters)
print(count.most_common())
# catalog = {}
# for i in letters:
#     if i in catalog:
#         catalog[i] += 1
#     else:
#         catalog[i] = 1
# list_ = list(catalog.keys())
# list_.sort()
# for z in list_:
#     print(f"{z} : {catalog[z]}")