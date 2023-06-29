# kind of like datetime module which has datetime.datetime
# https://peps.python.org/pep-0008/#package-and-module-names
# say that modules should have short all lowercase names

class Robot:
    def __init__(self, name, battery=100, skills=()):
        self.name = name
        self.battery = battery
        self.skills = list(skills)

    def __str__(self):
        return f"Robot {self.name} with battery: {self.battery}"

    def say_hi(self):
        print(f"Hi, I am {self.name}")

    def charge(self):
        self.battery = 100
        print(f"{self.name} is charged")