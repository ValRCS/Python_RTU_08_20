class Robot:
    def __init__(self, name, build_year, lk=0.5, lp=0.5):
        self.name = name
        self.build_year = build_year
        self.__potential_physical = lk
        self.__potential_psychic = lp

    def __str__(self) -> str:
        return "Name: " + self.name + ", Build Year: " + str(self.build_year)
    
    # repr is used when printing lists, dictionaries, etc.
    def __repr__(self) -> str:
        return "Robot('" + self.name + "', " + str(self.build_year) + ")"

    def condition(self):
        s = self.__potential_physical + self.__potential_psychic
        if s <= -1:
            return "I feel miserable!"
        elif s <= 0:
            return "I feel bad!"
        elif s <= 0.5:
            return "Could be worse!"
        elif s <= 1:
            return "Seems to be okay!"
        else:
            return "Great!"
        
    # let's add a method to return dictionary of data
    def get_dict(self):
        return {
            "name": self.name,
            "build_year": self.build_year,
            "potential_physical": self.__potential_physical,
            "potential_psychic": self.__potential_psychic,
            "flying": False,
            "likes": ("tv", "cooking", "reading", "riešana") 
            # tuple will be converted to list when saving to json
        }