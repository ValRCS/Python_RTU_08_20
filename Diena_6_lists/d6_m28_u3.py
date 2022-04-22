# 6. nod 3.uzd Apgrieztie vārdi
 
 
def flipped_words():
    user_sentence = input('enter sentence:').split()
    flipped_stence = []
    for i in user_sentence:
        flipped_stence.append(i[::-1])
    print(' '.join(flipped_stence).capitalize())
 
flipped_words()