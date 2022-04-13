# # Task 3
 
# change_verb = "nav"
# change_adjective = "slikt"    # without gendered ending
# verb_length = len(change_verb)    # length
# adj_length = len(change_adjective)    # length (without ending)
# in_text = input("Enter text: ")
# out_text = in_text
# while True:    # to get all "nav...slikts" and "nav...slikta" instances
#     change_idx_1 = out_text.find(change_verb)
#     change_idx_2 = change_idx_1 + verb_length + out_text[change_idx_1+verb_length:].find(change_adjective) # only look for "slikt" after "nav"
    
#     if change_idx_1 > -1 and change_idx_2 > -1:
#         change_to = "ir lab" + out_text[change_idx_2 + adj_length]
#         out_text = out_text[:change_idx_1] + change_to + out_text[change_idx_2+adj_length+1:]
#     else:
#         break
# print(out_text)

# Task 3
# Make the bad to the good
my_text = input("Enter your text: ")
no = "nav"
bad = "slikt"
good = "ir lab"
no_pos = my_text.lower().find(no)
bad_pos = my_text.lower().find(bad)
if no_pos >= 0 and bad_pos >= 0 and no_pos < bad_pos:
    bad_pos += len(bad)
    to_replace = my_text[no_pos:bad_pos]
    print(to_replace)
    print(my_text.replace(to_replace, good))
else:
    print(my_text)