# 3.uzdevums uzlabotais
text = input("Please enter a text: ")
contains1 = "nav"
contains2 = "slikt"
s = "s"
a = "a"
change_to = "ir lab"
start_index = text.find(contains1)
# contains2s_index = text.find(contains2+s)
# contains2a_index = text.find(contains2+a)
# #print(contains1_index)
# #print(contains2s_index)
# #print(contains2a_index)
# if contains1_index != -1 and contains2s_index != -1 and contains1_index < contains2s_index:
#     text = text[:contains1_index] + change_to + s
# elif contains1_index != -1 and contains2a_index != -1 and contains1_index < contains2a_index:
#     text = text[:contains1_index] + change_to + a
end_index = text.find(contains2)
# apskatamies vai vispar ir kaut kas jadara
# un jadara ir tad kad abi indexi ir atrasti un pirmais ir pirms otra
if start_index != -1 and end_index != -1 and start_index < end_index:
    text = text[:start_index] + change_to + text[end_index+len(contains2):]
print(text)