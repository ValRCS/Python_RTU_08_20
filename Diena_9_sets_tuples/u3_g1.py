def is_pangram(mytext, a='aābcčdeēfgģhiījkķlļmnņoprsštuūvzž'):
    my_bool_result = set(a) <= set(mytext.lower())
    return my_bool_result
 
print(is_pangram('Muļķa hipiji turpat brīvi mēģina nogaršot celofāna žņaudzējčūsku'))
print(is_pangram('Mīļš čehu frants jūk — žņaudz pūķi cilpā, bēg vāģos'))
print(is_pangram('Teksts, kas nav pangramma.'))

import string
print(is_pangram("A quick brown fox jumped over a sleeping dog"))
print(string.ascii_lowercase) # all english lowercase
print(is_pangram("A quick brown fox jumped over a sleeping dog",a=string.ascii_lowercase))
print(is_pangram("The quick brown fox jumped over a lazy dog",a=string.ascii_lowercase))
print(is_pangram("The quick brown fox jumps over the lazy dog",a=string.ascii_lowercase))
print(is_pangram("The five boxing wizards jump quickly.",a=string.ascii_lowercase))