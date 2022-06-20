class Song:
    def __init__(self, title="", author="", lyrics=()):
        self.title = title
        self.author = author
        self.lyrics = lyrics 
        print(f"Initialized class instance with {self.title=} {self.author=} {self.lyrics=}")
    
    def sing(self):
        print(self.title,self.author,'\n')
        for rinda in self.lyrics:
            # print(self.lyrics(rinda),'\n')
            print(rinda)
        return self
 
 
ziemelmeita=Song("Ziemelmeita","Jumprava", ["Gāju meklēt ziemeļmeitu","Garu, tālu ceļu veicu"])
ziemelmeita.sing()

print(ziemelmeita.lyrics)