#Ex 1: SONG
 
class Song:
 
    def __init__(self, title = "", author = "", lyrics = tuple()):
        self.title = title
        self.author = author
        self.lyrics = lyrics
        print()
        print("New Song made:", self.author, "-", self.title)
 
    def __print_header(self): #so internal hidden helper method
        print()
        if self.title != "":
            print(self.title, end='-')
        if self.author != "":
            print(self.author)

    def print_any_lyrics(self, lyrics, max_lines = -1): # public method for printing any lyrics
        if(max_lines < 0):
            max_lines = len(lyrics)
        for line in lyrics[:max_lines]:
            print(line)

    def sing(self, max_lines = -1):
        self.__print_header() #interally this will work , externally no
        self.print_any_lyrics(self.lyrics, max_lines)
        return self
 
    def yell(self, max_lines = -1):
        self.__print_header()
        yell_lyrics = [line.upper() for line in self.lyrics]
        self.print_any_lyrics(yell_lyrics,max_lines)
        return self

    def __del__(self): #less used than __init__
        # we could send some DB closing signal or something to some web service here
        print(f"THey are tearing me apart, {self.title}")
 
ziemelmeita = Song("Ziemeļmeita", "Jumprava", ["Gāju meklēt ziemeļmeitu","Garu, tālu ceļu veicu", "Lēni un par vēlu nācu", "Meklējot šo ziemeļmalu"])
omnibuss = Song("Omnibuss", "Labvēlīgais Tips", ["Domātāji domās dzīvo","Vēsturnieki – atmiņās","Brauc pa mūsu zemi brīvo","Omnibuss, kas nestājas"])
 
# TEST FOR EXERCISE 1
ziemelmeita.sing(2).yell(33)
omnibuss.yell().sing(1)
 
 
 
#Ex 2: RAP
class Rap(Song):
    def break_it(self, max_lines = -1, drop = "yeah"):
        print()
        if self.title != "":
            print(self.title, end='-')
        if self.author != "":
            print(self.author)
       
        if (max_lines > len(self.lyrics)) or (max_lines == -1):
            max_lines = len(self.lyrics)    #if asked to enter more lines than we have, give all we have
        for line in range(max_lines):
            words = self.lyrics[line].split(" ") 
            for wrd in words:
                print(wrd, drop.upper(), end =' ')   #word, drop," "(space, no new line)
            print()                                  #get a new line after above printed as one line
        return self
 
sitiens = Rap("Sitiens", "Ozols", ["Uz katru sitienu ar pret sitienu","Dzīvē cieņu bieži aizvieto ar necieņu","Uz katru uzbrukumu ar pret uzbrukumu","Tas ir tas, ko es priekš sevīm secinu"])
 
sitiens.break_it(3, "yo")
sitiens.break_it(2)
sitiens.break_it(2).sing().yell(1)

sitiens.print_any_lyrics(["Tālu aizgāja brālis", "Mana nama durvis viņam ciet"])
# del sitiens
