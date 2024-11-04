class Song:
    def __init__(self, title="", author="", lyrics=()):
        self.title = title
        self.author = author
        self.lyrics = lyrics #if we wanted to allow change in the future, we could use list(lyrics)
        print(f"New Song made: {self.title} by {self.author}")

    # let's define a helper method that will print author and title if they are set
    # if I use a single _ that means the method is meant for internal use
    # it is not really private but meant to be used as private
    def _print_info(self):
        if self.author or self.title:
            print(f"{self.title} by {self.author}")
        return self # so we can chain multiple methods    
 
    def sing(self, max_lines=-1):
        """
        Sing the song
        :param max_lines: maximum number of lines to sing
        if max_lines is -1, then all lines will be sung
        :return: self
        """
        self._print_info()
        if max_lines == -1:
            max_lines = len(self.lyrics)
        # below is another approach to limit the number of lines
        # for line in self.lyrics[:max_lines if max_lines != -1 else len(self.lyrics)]:
        for line in self.lyrics[:max_lines]:
            print(line)
        return self 
 
    def yell(self, max_lines=-1):
        """
        Yell the song
        :param max_lines: maximum number of lines to yell
        if max_lines is -1, then all lines will be yelled
        :return: self
        """
        self._print_info()
        if max_lines == -1:
            max_lines = len(self.lyrics)
        # for line in self.lyrics[:max_lines if max_lines != -1 else len(self.lyrics)]:
        for line in self.lyrics[:max_lines]:
            print(line.upper())
        return self 
 

lyrics = ("Gāju meklēt ziemeļmeitu", 
          "Garu, tālu ceļu veicu",
          "Lēni un par vēlu nācu",
          "Meklējot šo ziemeļmeitu") 
ziemelmeita = Song("Ziemeļmeita", "Jumprava",lyrics)
ziemelmeita.sing(1).yell()

mana_dziesma = Song("Mana dziesma", "Prāta vētra",
                    ["Kad dators izslēgts un telefons kluss", 
                     "Ļauj pie Tevis man šovakar nākt",
                     "Gribu mācīties pirmos soļus", 
                        "Un pirmo dziesmu sākt"])

mana_dziesma.sing().yell(2)

rudens = Song("Rudens","Prāta vētra",["Rudens kā rudens","Biezie un gājputni laižas uz Nīlu","Pēkšņi man likās","Tu esi mans draugs un es tevi","Mazliet mīlu"])
rudens.sing()
rudens.yell()

# 1.B
# Tie kas jūtas komfortabli, uztaisiet Rap klasi kas manto no Song
# Papildu metode break_it ar diviem noklusētiem parametriem max_lines un drop vienādu ar "yeah", kura līdzīga sing, bet pievienot drop aiz katra vārda...
# zrap = Rap("Ziemeļmeita", "Jumprava", ["Gāju meklēt ziemeļmeitu","
# Garu, tālu ceļu veicu"])
# zrap.break_it(1, "yah")
# Ziemeļmeita - Jumprava
# Gāju YAH meklēt YAH ziemeļmeitu YAH
 
class Rap(Song):
    # so we need to create our own __init__ method if we want to add some initialization
    # otherwise we can use the one from the parent class
    # def __init__(self, title: str = '', author: str = '', lyrics: tuple = tuple()):
    #     print("Rap init")
    #     super().__init__(title, author, lyrics)
    #     # we could add our own Rap related initialization here
    #     print("Rap init done")
 
    def break_it(self, max_lines: int = -1, drop: str = 'yeah'):
        # if not (self.author == '') or not(self.title == ''):
        #     print(f'{self.author} - {self.title}')
        self._print_info() # we can use the parent class method
            
        if max_lines == -1:
            for line in self.lyrics:
                # line_mod = ''
                tokens = line.split()
                # for word in tokens:
                #     line_mod += word + " " + drop + " "
                # tokens = " ".join([f"{word} {drop}" for word in tokens]) # alternative
                line_mod = f" {drop} ".join(tokens) + f" {drop}" # 3rd alternative
                print(line_mod)
        else:
            for i in range(max_lines):
                print(self.lyrics[i])
        return self
    
 
rap = Rap("Ziemeļmeita", "Jumprava", ["Gāju meklēt ziemeļmeitu","Garu, tālu ceļu veicu"])
rap.break_it()
rap.break_it(drop="YO")