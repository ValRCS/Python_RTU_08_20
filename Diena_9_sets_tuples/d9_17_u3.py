# Atstarpes ignorējam,un uzskatam ka lielais burts ir tikpat derīgs kā mazais, t.i. šeit A un a -> a
 
def is_pangram(mytext, a="abcdefghijklmnopqrstuvwxyz"):
    return set(a) <= set(mytext.lower())
    # mytext, a = set(mytext.lower()), set(a)
    # return mytext >= a # or a <= mytext
    
 
print(is_pangram("The quick brown fox jumps over the lazy dog Ķēpa"))
print(is_pangram("nav pangramma"))