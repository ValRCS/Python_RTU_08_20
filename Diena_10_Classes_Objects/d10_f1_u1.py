 
# class Song:
#     def __init__(self, title = "", author = "", lyrics = ()):
#         self.title = title
#         self.author = author
#         self.lyrics = lyrics
#         if title and author:
#             print(f"New song made - Title:{self.title}, Author: {self.author}")
#         elif title:
#             print(f"New song made - Title:{self.title}")
#         elif author:
#             print(f"New song made - Author: {self.author}")
#         else:
#             print("New song made")
 
#     def header(self):
#         if self.title and self.author:
#             print(f"{self.title} by {self.author}")
#         else:
#             print(f"{self.title}{self.author}")
 
#     def sing(self, max_lines = -1):
#         self.header()
#         if max_lines < 0:
#                 for i in self.lyrics:
#                     print(i, sep="\n")
#         elif max_lines > len(self.lyrics):
#             print("Not enough rows in lyrics")
#         else:
#             row = 0
#             while row != max_lines:
#                 print(self.lyrics[row], sep="\n")
#                 row += 1         
#         return self
        
#     def yell(self, max_lines = -1):
#         self.header()
#         if max_lines < 0:
#                 for i in self.lyrics:
#                     print(str(i).upper(), sep="\n")
#         elif max_lines > len(self.lyrics):
#             print("Not enough rows in lyrics")
#         else:
#             row = 0
#             while row != max_lines:
#                 print(str(self.lyrics[row]).upper(), sep="\n")
#                 row += 1         
#         return self
 
class Song:
    def __init__(self, title="", author="", lyrics=()):
        self.title = title
        self.author = author
        self.lyrics = lyrics
        print(f"New Song made: {title=} {author=}")
 
    def sing(self, max_lines=-1):
        print (f"{self.title} - {self.author}" )
        if max_lines != -1:
            for i in self.lyrics[0:max_lines]:
                print(i)
        else:
            for i in self.lyrics:
                print(i)
        return self
 
    def yell(self, max_lines=-1):
        print(f"{self.title} - {self.author}")
        if max_lines != -1:
            for i in self.lyrics[:max_lines]:
                print(i.upper())
        else:
            for i in self.lyrics:
                print(i.upper())
        return self
 

 
class Rap(Song):
    def break_it(self, max_lines=-1, drop=""):
        lyrics = self.lyrics # local for our break_it method
        # rap_lyrics = []
        if max_lines != -1:
            lyrics = self.lyrics[:max_lines]
        for line in lyrics:
            words = line.split()
            words_with_break = [f"{word} {drop.lower()}" for word in words]
            print(*words_with_break) # words_with_break is a list so we can just print all list elements
            # alterantive would be to use " ".join(words_with_break)
            # here i could save my rap lyrics if needed
        #     rap_lyrics.append(words_with_break)
        # for line in rap_lyrics:
        #     print(line)
 

ziemelmeita = Rap("Ziemeļmeita", "Jumprava", ["Gāju meklēt ziemeļmeitu", "Garu, tālu ceļu veicu"])
ziemelmeita.sing(1).yell()
numb = Song("Numb", "Linkin Park", ["I'm tired of being what you want me to be", "Feeling so faithless, lost under the surface", "Don't know what you're expecting of me", "Put under the pressure of walking in your shoes" ])
numb.sing(3).yell()
ziemelmeita.break_it(1,"yah") 
ziemelmeita.break_it(drop="Oh yeah") 

# ziemelmeita = Song(title = "Ziemeļmeita", author = "Jumprava", lyrics=("Gāju meklēt Ziemeļmeitu","Garu, tālu ceļu veicu"))
# monty = Song(title="Always Look on the Bright Side of Life", author="Monty Python", lyrics=("Some things in life are bad", "They can really make you mad", "Other things just make you swear and curse"))
# ziemelmeita.sing(1).yell()
# monty.sing(3).yell(1)