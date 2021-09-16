print("Uzdevums")
 
class Song:
    def __init__(self, title="", author="", lyrics=()):
        self.title = title
        self.author = author
        self.lyrics = lyrics
        print(f"New song made: {self.title} by {self.author}: \n{self.lyrics}")
 
    def _print_text(self, lines, max_lines=-1):
        if self.title:
            print(f"Song name: {self.title}")
        if self.author:
            print(f"Author: {self.author}")
        print("----")
        for num, line in enumerate(lines, 1):
            if num <= max_lines or max_lines==-1:
                print(f"{num}: {line}")
            else:
                break
        print("---")
 
    def sing(self, max_lines=-1):
        self._print_text(self.lyrics, max_lines=max_lines)
        return self
 
    def yell(self, max_lines=-1):
        self._print_text([line.upper() for line in self.lyrics], max_lines)
        return self

# class Song:
#     def __init__(self, title="", author="", lyrics=("",), max_lines = 0):
#         self.title = title
#         self.author = author
#         self.lyrics = lyrics
#     def sing(self, max_lines=-1):
#         if max_lines == -1:
#             max_lines = len(self.lyrics)
#         lyrics_len = self.lyrics[:max_lines]
#         print(f"{self.author} - {self.title}")
#         print("\n".join(lyrics_len))
#         return self
#     def yell(self, max_lines=-1):
#         if max_lines == -1:
#             max_lines = len(self.lyrics)
#         lyrics_len = self.lyrics[:max_lines]
#         lyrics_len = [each_string.upper() for each_string in lyrics_len]
#         print(f"{self.author} - {self.title}")
#         print("\n".join(lyrics_len))
#         return self
 
mySong = Song("Аборигены почему-то съели Кука", "Владимир Высоцкий",
              ("Но почему аборигены съели Кука?", "Комуй-то под руку попался каменюка,", "Метнул, гадюка, — и нету Кука!"))
print("---")
mySong.sing().yell(1).sing(1)
 
ziemelmeita = Song(lyrics=["Gāju meklēt ziemeļmeitu", "Garu, tālu ceļu veicu"])
print("---")
ziemelmeita.sing(2).yell()
 
class Rap(Song):
    # we need to to this if we add anything new otherwise the original Song constructor is called
    # def __init__(self, title="", author="", lyrics=()):
    #     super().__init__(title, author, lyrics)
    
    def break_it(self, max_lines=-1, drop="YAH"):
        rap_text = [" ".join([f"{word} {drop}" for word in line.split(" ")]) for line in self.lyrics]
        self._print_text(rap_text,max_lines)
        return self
 
# my_rap = Rap("Аборигены почему-то съели Кука", "Владимир Высоцкий",
#               ("Переживали, что съели Кука!", "Ломаем голову веками — просто мука!", "Зачем и как аборигены съели Кука."))
 
# my_rap.break_it()























# class Song:
#     def __init__(self, title='', author='', lyrics=()):
#         self.title = title
#         self.author = author
#         self.lyrics = lyrics
#         print(
#             f"Initialized class instance with {self.title=} {self.author=} and {self.lyrics=} \n")
#         print(f"New song made - {self.title} - {self.author} \n")
 
#     def sing(self, max_lines=-1):
#         if self.title and self.author:
#             print(self.title, "-", self.author)
#             print('♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪')
#         if self.lyrics and max_lines == -1:
#             for i in self.lyrics:
#                 print(i)
#             print('')
#         else:
#             if len(self.lyrics) >= max_lines:
#                 for num in range(max_lines):
#                     print(self.lyrics[num])
#             else:
#                 print('Sorry, there are not enough lines to print')
#             print('')
#         return self
 
#     def yell(self, max_lines=-1):
#         if self.title and self.author:
 
#             print(self.title.upper(), "-", self.author.upper())
#             print('♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪')
#         if self.lyrics and max_lines == -1:
#             for i in self.lyrics:
#                 print(i.upper())
#             print('')
#         else:
#             if len(self.lyrics) >= max_lines:
#                 for num in range(max_lines):
#                     print(self.lyrics[num].upper())
#             else:
#                 print('Sorry, there are not enough lines to print')
#             print('')
#         return self
 
 
# ziemelmeita = Song("Ziemeļmeita", "Jumprava", [
#     "Gāju meklēt ziemeļmeitu", "Garu, tālu ceļu veicu"])
 
# tuvutuvu = Song("Tuvu Tuvu", "Lādezers", [
#                 "Tuvu tuvu", "tuvāk vēl", "ko vēl var vēlēties"])
 
 
# ziemelmeita.sing(1)
# ziemelmeita.yell(1)
# tuvutuvu.sing().yell()