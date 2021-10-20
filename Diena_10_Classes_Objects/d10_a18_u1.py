class Song:
    def __init__(self, title="", author="", lyrics=()):
        self.title = title
        self.author = author
        self.lyrics = lyrics
        self.delimiter = ''
        if title and author:
            self.delimiter = '–'
        if title or author:
            print(f"New Song made: {self.author.title()} {self.delimiter} {self.title.title()} with {len(self.lyrics)} lines")
    def print_title(self):
        # print title and author if exist
        if self.title or self.author:
            print(f"{self.author.title()} {self.delimiter} {self.title.title()}")
    def sing(self, max_lines=-1, uppercase = False):
        print(f"Printing {max_lines} lines")
        self.print_title()
        lyrics = self.lyrics
        if max_lines != -1:
            lyrics = self.lyrics[:max_lines] # we do not want to mutate original
        for line in lyrics:
            print(line.upper() if uppercase else line)
            # if uppercase: #same as above one liner
            #     print(line.upper())
            # else:
            #     print(line)
        return self
    def yell(self, max_lines=-1):
        self.sing(max_lines=max_lines, uppercase = True)
        return self


# class Song:
#     def __init__(self, title, author, lyrics):
#         self.title = title
#         self.author = author
#         self.lyrics = lyrics
#         print(f'New Song Made: {self.author} - {self.title}')
 
#     def sing(self,max_lines = -1):
#         if max_lines == -1:
#             max_lines = len(self.lyrics)
#         print(self.author,'-',self.title)
#         for line in self.lyrics[:max_lines]:
#             print(line)
#         return(self)
 
#     def yell(self,max_lines = -1):
#         if max_lines == -1:
#             max_lines = len(self.lyrics)
#         print(self.author,'-',self.title)
#         for line in self.lyrics[:max_lines]:
#             print(line.upper())
#         return(self)


# class Song:
 
#     def __init__(self, title="", author="", lyrics=()):
#         self.title = title
#         self.author = author
#         self.lyrics = list(lyrics)
#         print(f"New Song Made: {author} - {title}")
 
#     def sing(self):
#         print(f"{self.title} - {self.author}")
#         lyrics = self.lyrics
#         for line in lyrics:
#             print(line)
#         return self
 
#     def yell(self, max_lines=-1):
#         print(f"{self.title} - {self.author}")
#         for index, x in enumerate(self.lyrics):
#             print(x.upper())
#             if index == (max_lines - 1):
#                 break
#         return self

class Rap(Song):
    # def __init__(self, title="", author="", lyrics=()):  # no need if it is identical
    #     super().__init__(title=title, author=author, lyrics=lyrics)
    def break_it(self, max_lines=-1, drop="yeah"):
        self.print_title()
        lyrics = self.lyrics
        if max_lines != -1:
            lyrics = self.lyrics[:max_lines]
        for line in lyrics:
            words = line.split(' ')
            line = f' {drop} '.join(words)+' '+drop
            print(line)
        return self

# ziemelmeita = Song("Ziemeļmeita", "Jumprava", ["Gāju meklēt ziemeļmeitu", "Garu, tālu ceļu veicu"])
ziemelmeita = Rap("Ziemeļmeita", "Jumprava", ["Gāju meklēt ziemeļmeitu", "Garu, tālu ceļu veicu"])


ziemelmeita.sing().yell(1).break_it()

# falling_away_from_me = Song("Korn", 
falling_away_from_me = Rap("Korn", 
    "Falling away from me", 
    ["Hey, I'm feeling tired", \
                                                            "My time has gone today", \
                                                            "You flirt with suicide", \
                                                            "Sometimes that's okay", \
                                                            "Do what others say", \
                                                            "I'm here standing hollow", \
                                                            "Falling away from me", \
                                                            "Falling away from me"])
falling_away_from_me.sing(3).yell(5)   

falling_away_from_me.break_it(4, drop="DA DUM").sing(2)

