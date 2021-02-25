# text = 'hubba bubba'  # Create one long string
# # Then create a set of all unique characters in the text
# characters = {char for char in text }
# print(characters)
# statistics = {}         # Create a dictionary to hold the results
# for char in characters: # Loop through unique characters
#     statistics[char] = text.count(char) # and count them
# print(statistics)

def get_char_count(text):
    my_dict = {}
    for letter in text:
        if letter in my_dict:
            my_dict[letter] += 1 # i add +1 to the bucket holding my letter
        else:
            my_dict[letter] = 1 # make a new bucket for new letter
    return my_dict

print(get_char_count("hubba bubba"))