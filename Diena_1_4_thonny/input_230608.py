# we might want to get some input from users
# python offers a built in function input which gives string
# after enter is pressed
name = input("What is your name friend? ")
print(f"Nice name {name}. I like it! 👍")

# we could pass in blank input()
print(f"{name} what is your favorite city?")
# print by default supplies newline
# city = input() #no extra text needed
city = input("-->")
print(f"Aha! {name} I see you like {city}. Me too!")