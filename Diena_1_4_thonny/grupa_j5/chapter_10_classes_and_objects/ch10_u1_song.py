class Song:
    '''Class to represent a song	
    Attributes:
        title (str): The title of the song
        author (str): The creator of the song
        lyrics (list,tuple): List of the song lyrics

    Methods:
        print_song_info(): Prints information about the song
        sing(): Prints the lyrics of the song
        yell(): Prints the lyrics of the song in uppercase
    '''

    # class method example

    # class method is a method that is called on the class itself no object instances
    # class methods are defined with @classmethod decorator
    @classmethod
    def create_song(cls):
        title = input("Ievadi dziesmas nosaukumu vai Enter ja nezini: ")
        author = input("Ievadi dziesmas autoru: vai Enter ja nezini")
        lyrics = []
        print("Ievadi dziesmas tekstu rindiņu pa rindiņai, lai pabeigtu ievadi tukšu rindiņu")
        while True:
            line = input()
            if line == "":
                break
            lyrics.append(line)
        return cls(title, author, lyrics) # cls is Song class
    
    # static method example
    # we might want to create a method that is related to the class but does not need any class data
    # we can create a static method
    # static methods are defined with @staticmethod decorator
    @staticmethod # 
    def print_song_list(song_list):
        print("Dziesmu saraksts:")
        for i, song in enumerate(song_list):
            # print(f"{i+1}. {song.title} - {song.author}")
            print(f"{i+1}. {song}") # simple item printing
        return song_list
    # this print_song_list is a regular function just attached to the class
    
    def __init__(self, title="", author="", lyrics=(), lyric_author=""):
        # notice default lyrics is empty tuple not empty list
        # DO NOT USE MUTABLE OBJECTS AS DEFAULT VALUES !!!
        # https://docs.python-guide.org/writing/gotchas/#mutable-default-arguments
        # otherwise all instances will share the same list !!!
        # we can use list as actual argument when creating instance - no problem
        self.title = title
        self.author = author
        self.lyrics = lyrics
        self.lyric_author = lyric_author
        # we can call any method from __init__ method
        print("New song created")
        self.print_song_info() # notice I need self here
    
    def print_song_info(self):
        print(f"Dziesma: '{self.title}' \nAutors: '{self.author}' \n")
        return self
    
    def sing(self, max_lines=-1):
        self.print_song_info()
        lyrics = self.lyrics # alias to self.lyrics
        if max_lines > 0:
            lyrics = lyrics[:max_lines] # slice list to get first max_lines
        for line in lyrics: # we want to iterate over alias or slice
            print(line)
        return self
 
    def yell(self, max_lines=-1):
        self.print_song_info()
        lyrics = self.lyrics # alias to self.lyrics
        if max_lines > 0:
            lyrics = lyrics[:max_lines] # slice list to get first max_lines
        for line in lyrics:
            print(line.upper())
        return self
 
# i can call static method without any instance
Song.print_song_list([("Dziesma1", "Autors1"), ("Dziesma2", "Autors2")])

patiesibai = Song("Patiesībai", "Instrumenti", 
                  ["Prasme atšķirt karstu no auksta", 
                   "Atšķirt krastu no upes sausas",
                   "Atšķirt karstu no auksta",])
ziemelmeita = Song("Ziemeļmeita", "Jumprava", 
                   ["Gāju meklēt ziemeļmeitu",
                    "Garu, tālu ceļu veicu",
                    ])
 
patiesibai.print_song_info()
patiesibai.sing()
patiesibai.yell()
 
print("\n")
 
ziemelmeita.print_song_info()
# ziemelmeita.sing()
# ziemelmeita.yell()
ziemelmeita.sing(1).yell(1)

ballejam=Song("Ballējam, neguļam","B2st", 
              "Ballējam, neguļam,\nLīdz rītam izturam!\n".splitlines())

ballejam.sing()
ballejam.yell(1)

vardite = Song("Vardīte", 
               "Raimonds Pauls", 
               "Maza zaļa vardīte - kvā kvā kvā,\nsēž uz lapas upītē - kvā kvā kvā".splitlines())
vardite.sing()
vardite.yell(1)

# let's make a stand alone function that prompts user for song info and creates a song
def create_song():
    title = input("Ievadi dziesmas nosaukumu vai Enter ja nezini: ")
    author = input("Ievadi dziesmas autoru: vai Enter ja nezini")
    lyrics = []
    print("Ievadi dziesmas tekstu rindiņu pa rindiņai, lai pabeigtu ievadi tukšu rindiņu")
    while True:
        line = input()
        if line == "":
            break
        lyrics.append(line)
    return Song(title, author, lyrics)

# let's create a song using our function
# jauna_dziesma = create_song()
# jauna_dziesma = Song.create_song() # this can be called even before any Song instance is created
# jauna_dziesma.sing()

class Rap(Song):
    # Rap class inherits everything from Song class
    # plus adds some new functionality
    def break_it(self, max_lines=-1, drop="YEAH"):
        self.print_song_info()
        lyrics = self.lyrics.copy() # Out of place
        if max_lines > 0:
            lyrics = lyrics[:max_lines] 
        for line in lyrics:
            modified_line = "" # te glabāsies pārveidotā repa rinda
            words = line.split() 
            for word in words:
                modified_line += word + " " + drop + " " 
            print(modified_line.strip()) 
        return self # lai varētu ķēdēt
    
ballejam=Rap("Ballējam, neguļam","B2st", 
              "Ballējam, neguļam,\nLīdz rītam izturam!\n".splitlines())

ballejam.break_it(drop="YEAH")
ballejam.sing().yell().break_it(1, "oh")