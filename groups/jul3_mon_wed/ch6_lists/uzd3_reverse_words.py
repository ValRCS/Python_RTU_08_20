teikums = input("Ievadiet teikumu: ")
def reverse_words(teikums, debug=False):
    words = teikums.split()
    reversed_words = [word[::-1] for word in words]
    apgriezts_teikums = " ".join(reversed_words).capitalize()
    if debug:
        print(apgriezts_teikums)
    return apgriezts_teikums

print(reverse_words(teikums, debug=True))