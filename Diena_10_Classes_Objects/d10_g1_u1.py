class Song:
    def __init__(self, title = "", author = "", lyrics = ()):     
        self.title = title
        self.author = author
        self.lyrics = lyrics
        print(f"New song made - {self.title} by {self.author}")
    
    def sing(self):
        print(self.author,self.title)
        print(*self.lyrics, sep = "\n")
        return self
 
    def yell(self):
        print(self.author,self.title)
        lyrics_cap = [sub.upper() for sub in self.lyrics]
        print(*lyrics_cap, sep = "\n")
        return self
 
ziemelmeita = Song("Ziemeļmeita", "Jumprava", ["Gāju meklēt ziemeļmeitu","Garu, tālu ceļu veicu"])
ziemelmeita.sing().yell()
 
es_nevaru_but_Balts = Song("Es nevaru būt balts", "Tranzīts", ["Es nevaru būt balts un tas nav iespējams","Jo visam vienmēr jābūt līdzsvarā"])
es_nevaru_but_Balts.sing().yell().sing()