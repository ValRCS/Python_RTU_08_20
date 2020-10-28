# text = input(" Ievadiet tekstu - ")    
# def get_char_count(text):
#     textin = {}
#     for c in text:
#         textin[c]=text.count(c) # not the most optimal
#     return textin
# print(get_char_count(text))

# def get_char_count(text) :
#     text = text.replace(" ", "")
#     dic = {}
#     for i in text:
#         dic[i] = dic.get(i,0) + 1
#     return dic

def get_char_count(text:str) -> dict:
    out_dict = {k:0 for k in text}
    for char in text:
        out_dict[char] += 1
    return out_dict
 
 
print(get_char_count("hubba bubba"))
print(get_char_count("abracadabra"))