
class Song:
    def __init__(self, title = "", author = "", lyrics = ()):
        self.title = title
        self.author = author
        self.lyrics = lyrics
        print(F"New song {self.title} by {self.author} was made.")
 
    def _print_title_author(self):
        if self.title != "":
            print(self.title)
        if self.author != "":
            print(self.author)
 
    def _print_lyrics(self, lyrics, max_lyrics = -1):
        if max_lyrics == -1:
            max_lyrics = len(lyrics)
        new_lyrics = lyrics[:max_lyrics]
        for line in new_lyrics:
            print(line)
 
    def sing(self, print_title = False, max_lyrics = -1):
        if print_title:
            self._print_title_author()
        self._print_lyrics(self.lyrics, max_lyrics)
        return self
 
    def yell(self, print_title = False, max_lyrics = -1):
        if print_title:
            self._print_title_author()
        self._print_lyrics([l.upper() for l in self.lyrics], max_lyrics)
        return self
 
# class Song:
 
#     def __init__(self, title='', author='', lyrics=()) -> None:
#         self.title = title
#         self.author = author
#         self.lyrics = lyrics
#         print(f"New Song made{f' - {self.title} by {self.author}' if self.title and self.author else ''}")
 
#     def sing(self, linecount= -1, upper=False):
#         if self.title and self.author:
#             if upper:
#                 print(f"*** {self.title} by {self.author} ***".upper())
#                 print()
#             else:
#                 print(f"*** {self.title} by {self.author} ***")
#                 print()
#         if self.lyrics:
#             if upper:
#                 for line_nr, line_txt in enumerate(self.lyrics):
#                     if linecount == -1:
#                         print(f"{line_txt}".upper())
#                     else:
#                         if line_nr < linecount:
#                             print(f"{line_txt}".upper())
#                         else:
#                             break
#             else:
#                 for line_nr, line_txt in enumerate(self.lyrics):
#                     if linecount == -1:
#                         print(f"{line_txt}")
#                     else:
#                         if line_nr < linecount:
#                             print(f"{line_txt}")
#                         else:
#                             break
#         else:
#             print("Sorry, this Song is missing lyrics.")
#         return self
 
#     def yell(self, linecount= -1):
#         self.sing(linecount, upper=True)
#         return self


class Rap(Song):
    # we need to to this if we add anything new otherwise the original Song constructor is called
    # def __init__(self, title="", author="", lyrics=()):
    #     super().__init__(title, author, lyrics)
    
    def break_it(self, max_lines=-1, drop="YAH"):
        rap_text = [" ".join([f"{word} {drop}" for word in line.split(" ")]) for line in self.lyrics]
        self._print_lyrics(rap_text,max_lines)
        return self
 
old_bob_lyrics = (
    "Mama take this badge from me",
    "I can't use it anymore",
    "It's getting dark too dark to see",
    "Feels like I'm knockin' on heaven's door",
    "",
    "Mama put my guns in the ground",
    "I can't shoot them anymore",
    "That cold black cloud is comin' down",
    "Feels like I'm knockin' on heaven's door")
 
old_bob = Song("Knockin' on Heaven's Door", "Bob Dylan", old_bob_lyrics)
 
# old_bob.sing()
old_bob.sing(2).yell(2)



# class Song:
#     def __init__(self, title="", author="", lyrics=()):
#         self.title = title
#         self.author = author
#         self.lyrics = lyrics
#         print(f"New song made - {self.author}, {self.title}", end="\n"*2)
    
 
#     def sing(self):
#         print(f"{self.title} - {self.author}")
#         print(*self.lyrics, sep="\n", end="\n"*2)
#         return self
 
#     def yell(self):
#         print(f"{self.title} - {self.author}")
#         yelling = [c.upper() for c in self.lyrics]
#         print(*yelling, sep="\n", end="\n"*2)
#         return self
 
ziemeļmeita = Song("Ziemeļmeita", "Jumprava", ["Gāju meklēt ziemeļmeitu", "Garu, tālu ceļu veicu"])
ziemeļmeita.sing().yell()
 
dzeguzes_balss = Song("Dzeguzes balss", "Menuets", ["Starp mašīnām, motoriem, meitenēm", "Uz ielu stūriem, kas salst"])
dzeguzes_balss.sing().yell(2).sing(1).yell()
 
stairway_to_heaven = Song("Stairway to Heaven", "Led Zeppelin", ["There's a lady who's sure all that glitters is gold",
"And she's buying a stairway to heaven"])
stairway_to_heaven.sing().yell()

hell_to_have_you = Song("Hell To Have You" , "Our Last Night & Sam Tinnesz"
                        , ("Lone wolf, I was running by myself"
                                ,"I don't want, don't want anybody else"
                                , "I'm solo, being on my own was easy"
                                , "Thought that I was all I needed, but no"))
 
# hell_to_have_you.sing(print_title = True)
# hell_to_have_you.yell(print_title = True).sing(max_lyrics=2)
hell_to_have_you.sing()
hell_to_have_you.yell().sing(2)

print(dir(Song))

method_names = [method_name for method_name in dir(Song) 
                if callable(getattr(Song, method_name))
                 and not method_name.startswith("_")]
print(method_names)

my_methods = [getattr(Song, name) for name in method_names]
print(my_methods)
print(my_methods[0].__name__)

bob_rap = Rap("Knockin' on Heaven's Door", "Bob Dylan", old_bob_lyrics)

bob_rap.sing(2).yell(3).break_it(2, drop="OH YEAH")
