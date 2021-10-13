#Third
import string
from collections import Counter
def is_pangram(mytext, alpha = "abcdefghijklmnopqrstuvwxyz"):
    return set(mytext.lower()) >= set(alpha)
    
 
print(is_pangram("If you see a crocodile, don't forget to scream"))
print(is_pangram("The quick brown  fox jumps over the lazy dog"))

a_lv = 'aābcčdeēfgģhiījkķlļmnņoprsštuūvzž'
print(is_pangram('Tfū, čeh, džungļos blīkšķ, zvaņģim jācērp!', alpha=a_lv))
print(is_pangram('Čehu zeņķi ģērbj plīša frakā, mūc džungļos, tēv!', alpha=a_lv))
print(is_pangram('Neteikums ģērbj plīša frakā, mūc džungļos, tēv!', alpha=a_lv))

lat_pan = "Tfū, čeh, džungļos blīkšķ, zvaņģim jācērp!"

bad_chars = string.punctuation + string.whitespace
print(f"Will remove {bad_chars} from {lat_pan}")

clean_text = lat_pan
for c in bad_chars:
    clean_text = clean_text.replace(c,"")
print(clean_text)
print(len(clean_text))

count = Counter(lat_pan)
print(count.most_common())
