#1A
class Song():
    def __init__(self, title, author, lyrics):
        self.title = title
        self.author = author
        self.lyrics = lyrics
        self.print_song_info()
 
    def print_song_info(self):
        print(f"Title: {self.title}, author: {self.author}")
 
    def sing(self, maxlines = -1):
        if maxlines == -1:
            maxlines = len(self.lyrics)
        self.print_song_info()
        for sentence in self.lyrics[:maxlines]:
            print(sentence)
        return self #for chaining
 
    def yell(self, maxlines = -1):
        if maxlines == -1:
            maxlines = len(self.lyrics)
        self.print_song_info()
        for sentence in self.lyrics[:maxlines]:
            print(sentence.upper())
        return self

ziemelmeita = Song("Ziemeļmeita", "Jumprava", ["Gāju meklēt ziemeļmeitu","Garu, tālu ceļu veicu","Lēni un par vēlu nācu", "Meklējot šo ziemeļmalu"])
ziemelmeita.sing()
ziemelmeita.yell()
ziemelmeita.sing(2).yell(3)

instrumenti = Song("HES un tu", "Instrumenti", ["Kad pieturā pie bankas",
"Tev prātā iešaujos", "Krīt trolejbusam stangas", "Šķīst zilas dzirksteles"])
instrumenti.sing().yell(2)

dziesma = Song("MTZ", "Jurka no Satiķiem", ["Man bija traktors, to sauca MTZ","Es saucu meitenes, bet viņas saka NĒ","Jo MTZ! JO MTZ!"])
dziesma.sing().yell(2)

class Rap(Song):
    def break_it(self, maxlines = -1, drop="Yeah"):
        if maxlines == -1:
            maxlines = len(self.lyrics)
        self.print_song_info()
        for sentence in self.lyrics[:maxlines]:
            print(sentence.replace(" "," "+drop.upper()+" "),drop.upper())
            # a little safer than replace above - no multiple drops on extra whitespace
            print((" "+drop.upper()+" ").join(sentence.split()) + " " + drop.upper())
        return self


# bohrhap_rap = Rap(*("Bohemian Rhapsody", "Queen",["Is this the real life?",
# "Is this just fantasy?", "Caught in a landside,", "No escape from reality"]))
bohrhap_rap = Rap("Bohemian Rhapsody", "Queen",["Is this the real  life?",
"Is this just fantasy?", "Caught in a landside,", "No escape from reality"])
bohrhap_rap.sing(2).break_it(3)