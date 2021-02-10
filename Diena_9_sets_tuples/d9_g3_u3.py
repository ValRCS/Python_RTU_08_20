# 3
def is_pangram(mytext, a='abcdefghijklmnopqrstuvwxyz'):
    # mytext = set(mytext.lower())
    # a = set(a)
    # return mytext.issuperset(a)
    return set(mytext.lower()) >= set(a)

# without sets
def is_pangram_no_sets(mytext, a='abcdefghijklmnopqrstuvwxyz'):
    for char in a:
        if char not in mytext.lower():
            return False
    return True
 
print(is_pangram("The five boxing wizards jump quickly"))
print(is_pangram("The five unwizards jump quickly"))

print(is_pangram_no_sets("The five boxing wizards jump quickly"))
print(is_pangram_no_sets("The five unwizards jump quickly"))