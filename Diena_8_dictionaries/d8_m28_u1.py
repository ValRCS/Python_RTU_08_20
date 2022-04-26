#1a
# text = "hubba bubba"
 
# def get_char_count(text):
#     new_dict = {}
#     for n in text:
#         if n in new_dict:
#             new_dict[n] +=1
#         else:
#             new_dict[n] = 1
 
#     return  new_dict
# print(get_char_count(text))

# def get_char_count_also(text, ref_dict = {}):
#     retval = ref_dict
#     return {k: 1 if k not in retval else retval[k]+1 for k in text}

# print(get_char_count_also(text))

#pirmais uzdevums
 
from collections import Counter #skaitītāja imports
# count_symbols = input("lūdzu ievadiet skaitāmo vārdu!") #lietotājs ievada vārdu, kam skaitīt simbolus
count_symbols = "lūdzu ievadiet skaitāmo vārdu!" #lietotājs ievada vārdu, kam skaitīt simbolus
def get_char_count(text: str) -> dict: #šeit definējam funkciju, kas paņem inputu un pārtaisa tā klasi uz dict
    new_dict = {}
    for i in text.upper(): #paceļam inputu lielajos burtos
        if i in new_dict:
            new_dict[i] += 1
        else:
            new_dict[i] = 1
    return new_dict
print(get_char_count(count_symbols)) #izdrukā ievadītā teksta izskaitītos simbolus (ga)
print(get_char_count("Statisks teksts, kura simbolus jāskaita"))

# think of counter as dictionary with benefits
char_counter = Counter(count_symbols) #skaitītāja funkcija
print(char_counter)
char_counter_dict = dict(char_counter) #skaitītāja funkcija
print(char_counter_dict)

print(char_counter.most_common(3)) #izdrukā 3 lielākās vērtības

