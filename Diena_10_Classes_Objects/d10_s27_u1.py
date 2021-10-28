class Song:
    """dziesma"""
    def __init__(self, title="", author="", lyrics=tuple()):
        self.title = title
        self.author = author
        self.lyrics = tuple(lyrics)
        print ("New Song made:", title," - ", author)
    
    def sing(self, max_lines=-1):
        print("SINGING", self.title, "-", self.author, ":")
        if max_lines == -1:
            max_lines = len(self.lyrics)
        for line in self.lyrics[:max_lines]:
            print(line)
        return self
    
    def print_author_title(self):
        if self.author:
            print(self.author, end=" - ")       
        if self.title:
            print(self.title)
        else:
            print("="*40)

    def yell(self, max_lines=-1):
        print("YELLING", self.title, "-", self.author, ":")
        if max_lines == -1:
            max_lines = len(self.lyrics)
        for line in self.lyrics[:max_lines]:
            print(line.upper())
        return self

song_nr_1 = Song("Iron sky", "Paolo Nutini"
    , ["We are proud individuals"
    , "living on the city"
    , "But the flames couldn't go much higher"
    , "We find gods and religions to"
    , "To paint us with salvation"
    , "But no one", "No nobody", "Can give you the power", "...."])

song_nr_1.sing().yell().sing(2).yell(3)


song_nr_2 = Song("Zaz", "Je Veux", ["Donnez-moi une suite au Ritz, je n'en veux pas!"
, "Des bijoux de chez Chanel, je n'en veux pas", "Donnez-moi une limousine, j'en ferais quoi? (Papala-papapala)"
, "Offrez-moi du personnel, j'en ferais quoi?"
, "Un manoir à Neuchâtel, c'n'est pas pour moi"
, "Offrez-moi la Tour Eiffel, j'en ferais quoi?", "......"])

song_nr_2.sing().yell().sing(2).yell(3)

class Rap(Song):
    def break_it(self,max_lines=2_000_000,drop="yeah"):
        self.print_author_title()
        drop = " " + drop.upper() + " "
        # if max_lines == -1:
        #     max_lines = len(self.lyrics)
        for line in self.lyrics[:max_lines]:
            temp = line.split()
            temp = drop.join(temp)
            temp += drop
            print(temp)  
        return self    

zrap = Rap("Ziemeļmeita", "Jumprava", ["Gāju meklēt ziemeļmeitu","Garu, tālu ceļu veicu"])

zrap.sing().break_it().break_it(1,"tak").break_it(drop="aha").yell(max_lines=4)