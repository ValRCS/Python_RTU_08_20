food = "kartupelis"
food[0]
food[9], food[-1]
food[-2]
food[0:3], food[:3]
food[2:5]  # remember last char is not written
food[2:7:2]
food[::2]
# how to reverse a string
rev_food = food[::-1]
rev_food
food
food += " elis"
food
food.index("p")
food.count("p")
new_food = food.replace("p", "ZE")
new_food
also_new = food[:5] + "X0Xmytext___" + food[6:]
also_new
food[:5] + "H" + food[5:]
