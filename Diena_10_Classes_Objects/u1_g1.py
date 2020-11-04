class Song:
    def __init__(self, title="", author="", lyrics=()):
        self.title = title
        self.author = author
        self.lyrics = lyrics
        print(f"New song made: {self.title} by {self.author}: \n{self.lyrics}")

    def _print_text(self, lines, max_lines=-1):
        if self.title != "":
            print(f"Song name: {self.title}")
        if self.author != "":
            print(f"Author: {self.author}")
        print("----")
        for num, line in enumerate(lines, 1):
            if num <= max_lines or max_lines==-1:
                print(f"{num}: {line}")
            else:
                break
        print("\n")

    def sing(self, max_lines=-1):
        self._print_text(self.lyrics, max_lines=max_lines)
        return self

    def yell(self, max_lines=-1):
        self._print_text([line.upper() for line in self.lyrics], max_lines)
        return self


mySong = Song("My heart will go on", "Celine Dion",
              ("You my heart", "You my soul", "Why so long"))
print("\n")
mySong.sing(2).yell(1)

ziemelmeita = Song(lyrics=["Gāju meklēt ziemeļmeitu", "Garu, tālu ceļu veicu"])
print("\n")
ziemelmeita.sing(2).yell()

class Rap(Song):
    def __init__(self, title="", author="", lyrics=()):
        super().__init__(title, author, lyrics)
    
    def break_it(self, max_lines=-1, drop="YAH"):
        rap_text = [" ".join([f"{word} {drop}" for word in line.split(" ")]) for line in self.lyrics]
        self._print_text(rap_text,max_lines)
        return self

my_rap = Rap("My heart will go on", "Celine Dion",
              ("You my heart", "You my soul", "Why so long"))

my_rap.break_it()