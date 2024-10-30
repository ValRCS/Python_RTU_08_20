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