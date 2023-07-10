#uzd_03
user_text = input("Ievadiet tekstu: ")
trig_one = "nav"
trig_two = "slikt" # now we can use sliktums, slikti, sliktākais etc
replace = "ir lab"

# first two checks will guarantee that we can use find I could even use index() here
if trig_one in user_text and trig_two in user_text and user_text.find(trig_one) < user_text.find(trig_two):
    start = user_text.find(trig_one)
    end = user_text.find(trig_two) + len(trig_two)
    print(user_text[:start] + replace + user_text[end:])
else:
    # print original
    print(user_text)