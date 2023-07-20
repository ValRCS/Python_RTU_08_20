#  Definējiet klasi Song
#  Klases construktora vajag būt trīs papildu 3 parametriem(self un vēl 3!)
# class Song:
#     def __init__(self, title="", author="", lyrics=()):
#         self.title = title
#         self.author = author
#         self.lyrics = list(lyrics)
#         print(f"New Song made: {self.title} by {self.author}")
 
#     def sing(self, max_lines=-1):
#         print(f"Title: {self.title}")
#         print(f"Author: {self.author}")
#         print("Lyrics:")
#         if max_lines == -1:
#             max_lines = len(self.lyrics)
#         for line in self.lyrics[:max_lines]:
#             print(line)
#         # below solution of above using ternary operator
#         # for line in self.lyrics[:max_lines] if max_lines != -1 else self.lyrics:
#         #     print(line)
#         return self
 
#     def yell(self, max_lines=-1):
#         print(f"Title: {self.title}")
#         print(f"Author: {self.author}")
#         print("Lyrics (YELLING):")
#         for line in self.lyrics[:max_lines] if max_lines != -1 else self.lyrics:
#             print(line.upper())
#         return self

# let's make a break_row function (not related to class) that we can use in break_it
def row_breaker(row, drop="yeah"):
    words = row.split()
    return " ".join(word + " " + drop for word in words) + " " + drop

class Song:
    def __init__(self, title="", author="", lyrics=()):
        self.title = title
        self.author = author
        self.lyrics = lyrics # if I planned methods for mutating lyrics
        # then we would need to cast to list self.lyrics = list(lyrics)
 
        print(f"New song - {title} by {author}")
 
    def sing(self, max_lines=-1):
        self._print_title_author()
        self.__print_lyrics(None, max_lines)
        return self
 
    def yell(self, max_lines=-1):
        self._print_title_author()
        self.__print_lyrics(lambda line: line.upper(), max_lines)
        return self
 
    def __print_lyrics(self, modifier, max_lines):
        # the name will be mangle into _Song__print_lyrics
        # we could have added self.__print_title_author() here 
        # but it's better to have it in a separate method
        lines_to_print = len(self.lyrics) if max_lines < 0 else max_lines
        for line in self.lyrics[:lines_to_print]:
            # so we either apply modifier function or just print line
            print(modifier(line) if modifier is not None else line)
 
        return self
    
    # let's make a helper method to print title and author
    # there is a concept in OOP as protected methods
    # protected methods are methods are ones that can be used by inherited classes
    # but are not meant for public use
    # in Python we can use _ in front of method name to indicate that it's protected
    # it is not truly protected, but it's a convention
    def _print_title_author(self):
        if self.title: # "" is falsy in python shorter than writing len(self.title) > 0
            print(f"Title: {self.title}")
        if self.author: # again "" is falsy
            print(f"Author: {self.author}")
    
asaras = Song("Asaras", "Čipsis un Dullais", ("Ir piektdienas vakars,", "un es esmu viens.", "Man pietrūkst tavs acu skatiens,", "un pieskāriens."))

asaras.sing(2).yell(1)

pardaugava = Song("Pārdaugava", "PND", 
                          ("tuvu pie sirds, tālu no centra", 
                        "aiziet uz mājām var arī kājām", 
                        "tuvu pie sirds, ne tik tuvu kā tu", 
                        "lai aizietu prom, jābrauc uz spāniju", 
                        "sakrājies ir, bet nav man, ko teikt"))

pardaugava.sing(2).yell()

#  1.B
#  Tie kas jūtas komfortabli, uztaisiet Rap klasi kas manto no Song
#  Papildu metode break_it ar diviem noklusētiem parametriem max_lines un drop vienādu ar "yeah", kura līdzīga sing, bet pievienot drop aiz katra vārda...
class Rap(Song):
    # no need for init if it does the same as parent class
    # def __init__(self, title="", author="", lyrics=()):
    #     super().__init__(title, author, lyrics)
    # it would make sense if I did something extra
 
    # def break_it(self, max_lines=-1, drop="yeah"):
    #     print(f"Title: {self.title}")
    #     print(f"Author: {self.author}")
    #     print("Lyrics (Rapping):")
    #     for line in self.lyrics[:max_lines] if max_lines != -1 else self.lyrics:
    #         words = line.split()
    #         new_line = " ".join(word + " " + drop for word in words)
    #         print(new_line)
    #     return self

    def break_it(self, max_lines=-1, drop="YEAH"):
        # self.__print_title_author() # will not work in inherited class!!
        self._print_title_author() # by convention we call protected methods with _
        # self._Song__print_lyrics(lambda row: f" {drop} ".join(row.split()) + " " + drop, max_lines)
        # we could have used external function for modifier
        # self._Song__print_lyrics(lambda row: row_breaker(row, drop), max_lines)
        # example using static method
        # we are doing this so our breaker functions are attached to class
        self._Song__print_lyrics(lambda row: self.break_row(row, drop), max_lines)
        return self
    
    # let's make a static method that will break a row
    # static methods are methods that don't need self
    # they are not related to class instance
    # they are just helper functions that are related to class

    @staticmethod
    def break_row(row, drop="yeah"):
        words = row.split()
        return " ".join(word + " " + drop for word in words) + " " + drop
    
# remember I can call static methods from class before any Rap instanced are made
print(Rap.break_row("Gāju meklēt ziemeļmeitu", "oho"))
    
my_rap = Rap("Ziemeļmeita", "Jumprava", ["Gāju meklēt ziemeļmeitu", "Garu, tālu ceļu veicu"])

my_rap.yell(1).break_it(2, "ohh yeah")

