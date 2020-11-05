class Song():
    def __init__(self, title="", author="", lyrics=()):
        self.title = title
        self.author = author
        self.lyrics = lyrics
        print(f"New Song made: {self.author=}, {self.title=}")
 
    def sing(self, max_lines=-1, sing_loud=False):
        self.print_credentials()
        for i, line in enumerate(self.lyrics):
            if i == max_lines: # so -1 will be never be reached and ALL lines will be printed
                break
            print(line.upper() if sing_loud else line)
        return self
 
    def yell(self, max_lines=-1):
        self.sing(max_lines=max_lines, sing_loud=True)
        return self
 
    def print_credentials(self):
        if self.title != "" and self.author != "":
            print(f"{self.title} - {self.author}")
        return self
 
 
class Rap(Song):
    def __init__(self, title="", author="", lyrics=()):
        super().__init__(title=title, author=author, lyrics=lyrics)
 
    def break_it(self, max_lines=-1, drop="yeah"):
        self.print_credentials()
        for i, line in enumerate(self.lyrics):
            if max_lines == i:
                break
            temp_list = line.split(" ")
            drop_to_add = f" {drop.upper()} "
            print(drop_to_add.join(temp_list) + drop_to_add[:-1])
        return self


ziemelmeita = Song("Ziemeļmeita", "Jumprava", ["Gāju meklēt ziemeļmeitu","Garu, tālu ceļu veicu"])
ziemelmeita.sing(1).yell(1)
 
zrap = Rap("Ziemeļmeita", "Jumprava", ["Gāju meklēt ziemeļmeitu","Garu, tālu ceļu veicu"])
zrap.break_it(1, "yah").sing().yell(2).break_it(drop="aha")