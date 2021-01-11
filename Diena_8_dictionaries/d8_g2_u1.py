# text=input("Input text: ")
# def get_char_count(text):
#     count={str(n):text.count(n) for n in text}
#     return count
 


# from collections import Counter
# def get_char_count(text):
#     # text = input("Please enter any text: ")
#     count = Counter(text)
#     print(count)
#     return count

def get_char_count(raw_text):
    text = str(raw_text).replace(" ", "")
    count = {}
    for i in text:
        if i in count.keys():
            count[i] += 1
        else:
            count[i] = 1
    my_list = list(count.items())
    my_list = sorted(my_list, key = lambda el: el[1])[::-1]  
    count = dict(my_list)
    return count
 
# print(get_char_count(a))    
 
my_count = get_char_count("Abracadabra maģija mana")
# print(my_count.most_common()) # for counter only
print(my_count)