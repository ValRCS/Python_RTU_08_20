#3. uzdevums
import string
punctuation = string.punctuation # will give us all the punctuation marks
# we could add our own punctuation marks to this string 
teikums = ""
vardi = []
otradi = []
 
user_input = input("Ievadi teikumu: ")
 
# vardi = user_input.split()
 
# for word in vardi:
#     apgriezts = word[::-1]
#     otradi.append(apgriezts)
# # otradi[0] = otradi[0].lower()
# # otradi[0] = otradi[0].title()
# new_sentence = " ".join(otradi).capitalize()
# print(new_sentence)

new_sentence = " ".join([word[::-1] for word in user_input.split()]).capitalize()
print(new_sentence)
# lets do it one operation at a time
# 0. remove punctuation marks
# so go through each character in the string and replace it with nothing
# for bad_char in punctuation:
#     user_input = user_input.replace(bad_char, "") 
# 1. split the sentence into words
# 2. reverse each word
reversed_words = [word[::-1] for word in user_input.split()]
print(reversed_words)
# 2.5 We could check last word and move punctuation marks to the end of the sentence
if reversed_words[-1][0] in punctuation:
    # we have punctuation mark at the beginnin of the last word
    # lets move it to the end of this word
    reversed_words[-1] = reversed_words[-1][1:] + reversed_words[-1][0]
# 3. join the words back together
new_sentence = " ".join(reversed_words)
# 4. capitalize the first letter of the sentence
new_sentence = new_sentence.capitalize()
print(new_sentence)