# Uzrakstīt programmu teksta pārveidošanai
 
not_string = "nav"
bad_string = "slikt" # will work with slikta un sliktie as well
 
text = input("Lūdzu ievadiet tekstu: ")
 
not_index = text.find(not_string)
bad_index = text.find(bad_string)
 
# need_replacement = True if bad_index > not_index > -1 else False
# # we can rewrite it as:
# if bad_index > not_index > -1:
#     need_replacement = True
# else:
#     need_replacement = False

# even simpler
need_replacement = bad_index > not_index > -1
# same as need_replacement = bad_index > not_index and not_index > -1
# we are guaranteed True or False
# also we want bad_index to be after not_index
# and we want both to be found thus over -1
    
if need_replacement:
    print(f"{text[:not_index]}ir lab{text[bad_index + len(bad_string):]}")
    # with string concatenation
    print(text[:not_index] + "ir lab" + text[bad_index + len(bad_string):])
else:
    print(text)

# TODO make it work with multiple bad words