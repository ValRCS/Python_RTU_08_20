from collections import Counter
text = "hubba bubba"
# def get_char_count(text):
#     letters = {}
 
#     for letter in text:
#         letters[letter] = text.count(letter)  # hidden loop in count    
        
#     return letters

def get_char_count(text):
    res_dict = {}
    for c in text:
        if c in res_dict:
            res_dict[c] += 1
        else: 
            res_dict[c] = 1
    return res_dict
 
print(get_char_count(text))

count = Counter(text)
print(count)
print(count.most_common())
