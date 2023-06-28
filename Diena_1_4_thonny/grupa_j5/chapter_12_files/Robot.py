class Robot:
    def __init__(self, name, build_year):
        self.name = name
        self.build_year = build_year

    def __repr__(self):
        return "Robot('" + self.name + "', " + str(self.build_year) + ")"

    def __str__(self):
        return "Name: " + self.name + ", Build Year: " + str(self.build_year)
    
    def get_dictionary(self):
        return {'name': self.name, 
                'build_year': self.build_year,
                'is_flying': False,
                'foods': ('apple', 'banana', 'orange') # i use tuple to show that json can handle tuples
                }

    def say_hi(self):
        print("Hi, I am " + self.name)

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_build_year(self, by):
        self.build_year = by

    def get_build_year(self):
        return self.build_year