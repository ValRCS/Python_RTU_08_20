# def replace_between_words(string, first_word, second_word, replacement):
#     start_index = string.find(first_word)
#     end_index = string.find(second_word)
 
#     if start_index != -1 and end_index != -1 and end_index > start_index:
#         replaced_string = string[:start_index] + replacement + string[end_index + len(second_word):]
#         return replaced_string
#     else:
#         return string
 
 
# text = input("Ievadi teikumu: ")
 
# new_text = replace_between_words(text, "nav", "slikts", "ir labs")
# print(new_text)

# rewrite the above code without functions
text = input("Ievadi teikumu: ")
first_word = "nav"
second_word = "slikt"
replacement = "ir lab"
start_index = text.find(first_word)
end_index = text.find(second_word)
if start_index != -1 and end_index != -1 and end_index > start_index:
    replaced_string = text[:start_index] + replacement + text[end_index + len(second_word):]
    print(replaced_string)
else:
    print(text) # original text if no replacement


# write the same code as above but using regular expressions
# import re
# # regular expression is a pattern that is used to match character combinations in strings
# # regular expressions are language agnostic - they are used in many programming languages
# # there are some differences in regular expressions between programming languages
# more on regular expressions: https://docs.python.org/3/library/re.html
# nice for testing 101 regular expressions: https://regex101.com/
# text = input("Ievadi teikumu: ")
# first_word = "nav"
# second_word = "slikt"
# replacement = "ir lab"
# replaced_string = re.sub(rf"{first_word}.*{second_word}", replacement, text)
# print(replaced_string)
