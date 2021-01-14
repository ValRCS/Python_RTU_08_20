class Song:
    def __init__(self, title="", author="", lyrics=()):
        self.title = title
        self.author = author
        self.lyrics = lyrics
        print(f"New song by {self.title} by {self.author} made!")
 
    def sing(self, max_lines = -1):
        if(max_lines < 0):
            max_lines = len(self.lyrics)
        print(f"Song title: {self.title}, by {self.author}\n")
        for item in self.lyrics[:max_lines]:
            print(item)
        print("\n")
        return self
    # hmm.. these functions are almost the same.
    # If only I could somehow avoid repeating myself..
    # 
    #  
    def yell(self, max_lines = -1):
        if(max_lines < 0):
            max_lines = len(self.lyrics)
        print(f"Song title: {self.title}, by {self.author}\n")
        for item in range(max_lines):
            print(self.lyrics[item].upper())
        print("\n")
        return self
    
class Rap(Song):
    
    def break_it(self, max_lines = -1, drop = "yeah"):
        if(max_lines < 0):
            max_lines = len(self.lyrics)
        print(f"Song title: {self.title}, by {self.author}\n")
        for item in range(max_lines):
            print(self.lyrics[item])
            print(drop)
        print("\n")
        return self
 
 
ziemelmeita = Song("Ziemeļmeita", "Jumprava", ["Gāju meklēt ziemeļmeitu","Garu, tālu ceļu veicu"])
dumai = Song("Dumai","Daniel Khan",["I carry in my heart a dream","a flag of peace and land redeemed","but in my dream a wall of wire","stone and iron forged in fire"])
dumai_rap = Rap("Dumai","Daniel Khan",["I carry in my heart a dream","a flag of peace and land redeemed","but in my dream a wall of wire","stone and iron forged in fire"])
    
#ziemelmeita.sing(1).yell()
dumai.sing(2).yell().yell(3)
dumai_rap.break_it(3,"oy")