def get_char_count(numOrText):
    text = str(numOrText).replace(" ", "")
    countDict = {}
    for i in text:
        if i in countDict.keys():
            countDict[i] += 1
        else:
            countDict[i] = 1
    my_list = list(countDict.items())
    my_list = sorted(my_list)  # could also do my_list.sort()
    countDict = dict(my_list)
    return countDict


my_dict = get_char_count(599637003)
print(my_dict)
print(get_char_count("hubba bubba"))
print(get_char_count(" "))
print(get_char_count("1_000_000"))

# print(list(my_dict.items()))
