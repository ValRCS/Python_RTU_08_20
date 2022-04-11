#3
# username=str(input("Username?"))
#username="username"
text=str(input("Please enter text:"))
#text="Tas biezpiens nav nemaz tik slikts"
a=text.find("nav")
b=text.find("slikts")
if a > 0 and b > 0 and a < b:  # a - nav has to be before b - slikts
    print(text[:a]+"ir labs"+text[b+6:])  # TODO replace 6 with len("slikts")
else:
    print(text)