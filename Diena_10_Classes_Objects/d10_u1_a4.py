class Song:
 
    def __init__(self, 
                 title: str, 
                 author: str, 
                 lyrics: tuple):
        self.title = title
        self.author = author
        self.lyrics = lyrics
        print(f"🎼 New Song made by {self.author}, titled {self.title}")

    # public method just like any other
    # _ indicates that this method is meant for private use but not enforced
    def _print_title(self):
        print(f'🎶 {self.author} "{self.title}" 🎶')
        return self 

    def sing(self, max_lines = -1):
        self._print_title()
        if max_lines == -1:
            for text in self.lyrics:
                print(text)
        else:
            # for line, text in enumerate(self.lyrics):
            #     print(text)
            #     if line == max_lines - 1:
            #         break
            for line in self.lyrics[:max_lines]:
                print(line)
        return self
    
    def yell(self, max_lines = -1):
        self._print_title()
        if max_lines == -1:
            for text in self.lyrics:
                print(text.upper())
        else:
            # for line, text in enumerate(self.lyrics):
            #     print(text.upper())
            #     if line == max_lines - 1:
            #         break
            for line in self.lyrics[:max_lines]:
                print(line.upper())
        return self
 
ziemelmeita = Song("Ziemeļmeita", "Jumprava", ["Gāju meklēt ziemeļmeitu","Garu, tālu ceļu veicu",
                                               "Lēni un par vēlu nācu", "Meklējot šo ziemeļmalu",
                                               "Naktī zvaigžņu jūrā redzu debess malu to", "Kur mīt mana ziemeļmeita",
                                               "Kā lai tieku vējiem līdzi, kas to apciemo?", "Gadi aiziet viņu meklējot"])
 
kakis = Song("Kaķis", "Hospitāļu iela", ["Zaglīgi soļi", "Un kaķis ar tiem", "Vienā ritmā", "Zaglīgi soļi",
                                         "Un kaķis ar tiem", "Vienā ritmā", "Ar manējiem", "Ar manējiem",
                                         "Ar manējiem", "Ar manenenenenenenē", "Nē, es nevaru", "Tavā istabā sildīt rokas",
                                         "Durvīs ir iestājies suns", "Iekšā ir Taškenta", "Redzu pa logu",
                                         "Ārā ir mīnusi", "Ārā ir tumšs", "Ak, kabata mana nav tukša", "Tur vesela paciņa 'Red and White'",
                                         "Skatos uz dusmīgo duksi", "Saku – kuce laid, ai"])
 
muzu_muzos = Song("Mūžu mūžos būs dziesma", "Imants Ziedonis", ["Mūžu mūžos būs dziesma", "Un mūžu mūžos alus smēķēs",
                                                                "Un mūžam Dziesmu svētkos", "Nāks meitene baltās zeķēs.", 
                                                                "Ziedu un jāņzāļu jūra,", "Un mana zilacainā skuķe",
                                                                "Tur nāk no Dundagas dārziem,", "Un rokās tai balta puķe."])
 
ziemelmeita.sing(3).yell(5)
kakis.yell(15).sing(5)
muzu_muzos.sing(2).yell(4)
ziemelmeita.sing().yell()

class Rap(Song):
    
    def break_it(self,max_lines=-1,drop="yeah"):      
        self._print_title()
        # we set max_lines to the length of the lyrics if max_lines is -1
        # we could use ternary operator here
        # max_lines = max_lines if max_lines > 0 else len(self.lyrics)
        # even simpler is to use single line if statement
        if max_lines == -1:
            max_lines = len(self.lyrics) 

        # using slicing to get the first max_lines elements
        # if max_lines is over that is ok, it will just return all the elements
        for row in self.lyrics[:max_lines]:
            print(row.replace(" ", " "+drop+" "))

        return self
    
zrap = Rap("Never gonna give you up", "Rick Astley", ["Never gonna give you up","Never gonna let you down", "Never gonna run around and desert you"])
zrap.break_it(3).yell()
zrap.break_it(3, "uga")