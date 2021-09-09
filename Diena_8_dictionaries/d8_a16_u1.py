from collections import Counter
import string
print(string.digits)

def get_char_count(text):
    text = str(text)
    # letters = {}
    # for i in text:
    #     if i in letters:
    #         letters[i] += 1
    #     else:
    #         letters[i] = 1
    letters = Counter(text)
    print(letters)
    return letters

 
 
get_char_count("suns")
get_char_count("hubba bubba")
get_char_count(599637003)

my_counter = get_char_count("hubba bubba abracadabra")
print(my_counter.most_common())
print(my_counter.get("b"), my_counter["b"])

# def get_char_count(text):
#     a={}
#     for c in text:
#         keys=a.keys()
#         if c in keys:
#             a[c]+=1
#         else:
#             a[c]=1
#     return a
  
# print(get_char_count("hubba bubba"))
# print(get_char_count("Alus ari ira sula"))

# def get_char_count(text):
#     count = {}
#     for c in set(text): # set gives us unique values in our collection
#         count[c] = text.count(c) # counting each item will be suboptimal
#     return count
 
# print(get_char_count("hubba bubba"))