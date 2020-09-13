# https://www.toptal.com/python/python-class-attributes-an-overly-thorough-guide#so-when-would-you-use-them

class TC:
    my_val = "Static property/attribute"
    s_val = "Another static"

    def __init__(self, my_val):
        self.my_val = my_val


c1 = TC("doh")
c2 = TC("self")
print(c1.my_val)
print(TC.my_val)
# how static and normal attributes can diverge
print(c1.s_val)
print(TC.s_val)
c1.s_val = "Not so static anymore is it?"
print(c1.s_val)
print(TC.s_val)
