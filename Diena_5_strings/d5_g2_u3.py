# input_text = input("Please enter any text: ")
# value_nav = input_text.find("nav")
# value_slikts = input_text.find("slikts")
# if value_nav != -1 and value_slikts != -1:
#     if value_nav <= value_slikts:
#         replace1 = input_text.replace("nav", "ir")
#         replace2 = replace1.replace("slikts", "labs")
#         print(replace2)
# else:
#     print(input_text)

input_text2 = input("Please enter any text: ")
value_nav2 = input_text2.find("nav")
value_slikts2 = input_text2.find("slikts")
if value_nav2 != -1 and value_slikts2 != -1:
    if value_nav2 <= value_slikts2:
        ind_nav = input_text2.index("nav")
        ind_nav_use = ind_nav + 4
        ind_slikts = input_text2.index("slikts")
        replacetxt = input_text2[:ind_nav_use] + input_text2[ind_slikts:]
        replace1a = replacetxt.replace("nav", "ir")
        replace2a = replace1a.replace("slikts", "labs")
        print(replace2a)
else:
    print(input_text2)