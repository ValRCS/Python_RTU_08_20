# Vitauts
def is_pangram_en(mytext, a=set('abcdefghijklmnopqrstuvwxyz')):
    return len(set(mytext.lower()).intersection(a)) == 26


def is_pangram_lv(mytext, a='aābcčdeēfgģhiījkķlļmnņoprsštuūvzž'):
    return len(set(mytext.lower()).intersection(a)) == 33


def main():
    print(is_pangram_en('The quick brown fox jumps over the lazy dog'))       # -> true
    # -> false
    print(is_pangram_en('The quick brown fox jumps over the dog'))
    print(is_pangram_en('The five boxing wizards jump quickly')
          )              # -> true

    print(is_pangram_lv('Tfū, čeh, džungļos blīkšķ, zvaņģim jācērp!'))        # -> true
    print(is_pangram_lv('Čehu zeņķi ģērbj plīša frakā, mūc džungļos, tēv!'))  # -> true
    print(is_pangram_lv('Parasts teikums, kas nav pangramma.')
          )               # -> false


if __name__ == "__main__":
    main()
