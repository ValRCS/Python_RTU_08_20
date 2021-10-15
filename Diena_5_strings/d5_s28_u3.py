# # Uzd. 3-1 replace a not bad to good (LV end of the words doesn't work ... ????? should find an answer)
# char_1 = input("Enter the sentence (example: this ship is not bad): ") # Enter a sentence
# no_chr = "not"  # 1st Variable for search and exchange
# bad_chr = "bad" # 2nd Variable for search and exchange
# bad_chr_len = len(bad_chr)
# repl_1 = "good" # replacement variable
 
 
# no = char_1.find(no_chr) # searching for the first variable in the sentence and apply a new variable "no"
# bad = char_1.rfind(bad_chr) # searching for the second variable in the sentence and apply a new variable "bad"
# if no >= 0 and bad >= 0 and no < bad:
#     char_1 = char_1[:no] + repl_1 + char_1[bad+bad_chr_len:] # result after cutting (+3 for cut bad_chr)
# print(char_1)

# #Uzd. Nr. 3-2
 
no_text = "nav" # 1st variable
bad_text = "slikt" # 2nd variable without end of the word, cause of changing
rep_text = "ir lab" # 3rd variable without end of the word, cause of changing
text = input("Enter any sentence that contains words: 'nav', 'slikts/a': ") # text input by user
 
new_text = text.find(no_text) # searching for variable no_text (if nav slikts/slikta only - give 0)
new_bad_t = text.find(bad_text) # searching for variable bad_text (if nav slikts/slikta only - give 4) should be greater than new_text
 
if new_bad_t > -1 and new_text > -1 and new_text < new_bad_t:  # check for True/False values with the end of the variables
    head = text[:new_text] #cutting part
    tail = text[new_bad_t+len(bad_text):] 
    print(head)
    print(rep_text)
    print(tail)
    result = head + rep_text + tail # result if function = True
    print(result)
else:
    print(text) 