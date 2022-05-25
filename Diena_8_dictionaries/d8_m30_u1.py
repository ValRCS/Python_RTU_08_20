# 1.a
from collections import Counter

def get_char_count(text: str) -> dict:
    """
    Returns a dictionary with the count of each character in the text.
    :param text: str
    :return: dict
    """
    # char_count = {}
    # for char in text:
    #     if char in char_count:
    #         char_count[char] += 1
    #     else:
    #         char_count[char] = 1
    # return char_count	
    text = text.lower()
    vardnica = {}
    for i in text:
        if i in vardnica:
            vardnica[i] += 1 # same as vardnica[i] = vardnica[i] + 1
        else:
            vardnica[i]=1
    return vardnica
    
text = "hubba bubba"
print(f"get_char_count(\"{text}\") => {get_char_count(text)}")
skaitlis = 599637003
text = str(skaitlis)
print(f"get_char_count(\"{text}\") => {get_char_count(text)}")

counter = Counter("hubba bubba")
print(counter) # counter is a dictionary with some extra methods such as most_common()
print(counter.most_common())
print(dict(counter))

food_count = Counter(["banana", "apple", "orange", "banana", "apple", "orange", "pineapple"])
print(food_count)