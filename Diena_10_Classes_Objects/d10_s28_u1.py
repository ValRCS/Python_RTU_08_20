#1 uzd
class Song:
    def __init__(self, title="", author="", lyrics=()):  # use tuple for default value instead of list
        """
        Constructor for the Song class
        :param title: str
        :param author: str
        :param lyrics: list
        """
        self.title = title
        self.author = author
        self.lyrics = lyrics
        print(f"New song made:  {self.title} izpilda {self.author}")


    def ref_function(self):                                 # method with self argument, method used for reference
        if self.title != "" and self.author != "":          #check fo title and author for blank entry
            return self.title + ' - ' + self.author         #return if both rules True (not blank)
        elif self.title == "" and self.author != "":
            return "Unknown song name - " + self.author
        elif self.title != "" and self.author == "":
            return self.title + " - Unknown Author"
        else:
            return "Unknown song name and Author" 

    def sing(self, repeat=1, max_lines=-1):
        print(self.ref_function())
        if max_lines == -1:
            max_lines = len(self.lyrics)
        # for _ in range(repeat): # _ is a placeholder for any value
        #     print(*self.lyrics[:max_lines], sep = "\n")  # * unpacks the list
        # same as above
        for _ in range(repeat):
            for line in self.lyrics[:max_lines]:
                print(line)
        return self
 
    # def yell(self):
    #     print(self.author,self.title)
    #     lyrics_cap = [sub.upper() for sub in self.lyrics]
    #     print(*lyrics_cap, sep = "\n")
    #     return self
    def yell(self, max_lines=-1):
        # print(f"{self.title} - {self.author}")
        print(self.ref_function())
        for index, x in enumerate(self.lyrics):
            print(x.upper())
            if index == max_lines-1:
                break
        return self


ziemelmeita = Song("Ziemeļmeita", "Jumprava", ["Gāju meklēt ziemeļmeitu", "Garu, tālu ceļu veicu"])
ziemelmeita.sing().yell()        
 
piradzins = Song("Pīrādziņ nāc ārā", "Labvēlīgais Tips", ["Skolā trešā klasē visi mani sauca, kuru grūti atkārtot",
"Māte katru dienu lika izēst putru",
"Bet aiz loga draugu balsis skan",
"Viens, divi, trīs, četri",
"Pīrādziņ, nāc ārā, nāc ārā, nāc ārā"])
piradzins.sing(3).yell(2)

lyrics = ['The truth is, you turn into someone else',                                # too large text, separated to multiple lines 
          'You keep running like the sky is falling',
          'I can whisper, I can yell',
          'But I know, yeah I know, yeah I know',
          "I'm just talking to myself"]    
 
music_song = Song('Talking To Myself ', ' Linkin Park', lyrics)                      # new title and Author to check
music_song.sing(max_lines=3).yell(max_lines=1).yell(max_lines=2).sing(repeat=2) 

gulbis = Song("Balāde par gulbi"
        , "Pērkons"
        , ["Kārna vārna"
        ,"Uz slapa kapa"
        ,"Man savu patiesību ķērc"
        ,"Vai tiešām viņa neattapa"
        , "Ka viss tas - tikai joka pēc"])

gulbis.yell(5).sing(3)

class Rap(Song):
    def break_it(self, max_lines = -1, drop = "yeah"):
        print(self.ref_function())
       
        if max_lines == -1:
            max_lines = len(self.lyrics)    
        for line in self.lyrics[:max_lines]:
            words = line.split(" ") 
            for word in words:
                print(word, drop.upper(), end =' ')  
            # alternative is to use join() method
            # drop = drop.upper() + " "
            # print(drop.join(words) + drop )
            print()                                 
        return self

ziemelmeita = Rap("Ziemeļmeita", "Jumprava", ["Gāju meklēt ziemeļmeitu","Garu, tālu ceļu veicu", "Lēni un par vēlu nācu", "Meklējot šo ziemeļmalu"])
ziemelmeita.sing().yell().break_it(2).break_it(3, drop="aha")