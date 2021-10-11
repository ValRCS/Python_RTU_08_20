first_text = "nav"
second_text = "slikt"
replacement_text = "ir lab"
sentence= input("Please enter your text: ")

nav_index = sentence.lower().find(first_text)
slikts_index = sentence.lower().find(second_text)
if nav_index > -1 and nav_index < slikts_index:
    cut_sentence = sentence[:nav_index]
    new_sentence = cut_sentence + replacement_text + sentence[slikts_index+len(second_text):]
    print(new_sentence)
else:
    print(sentence)

# 3. uzdevums
# first_part_to_find = "nav"
# second_part_to_find = "slikt"
# replacement_string = "ir lab"
# ending_char_opt_1 = "s"
# ending_char_opt_2 = "a"
# final_ending_char = ""
# user_input = input("Please enter any sentence:")
# print(user_input)
# start_index_first_part = user_input.find(first_part_to_find)
# start_index_second_part =  user_input.find(second_part_to_find)
# if user_input[start_index_second_part + len(second_part_to_find)] == ending_char_opt_1:
#     final_ending_char = ending_char_opt_1
# elif user_input[start_index_second_part + len(second_part_to_find)] == ending_char_opt_2:
#     final_ending_char = ending_char_opt_2
# else:
#     final_ending_char = "STOP"
# if start_index_first_part != -1 and start_index_second_part != -1 and final_ending_char != "STOP":
#     print("Modified string:")
#     modified_string = user_input[:start_index_first_part] + replacement_string + final_ending_char + user_input[start_index_second_part + len(second_part_to_find)+len(final_ending_char):]
#     print(modified_string)