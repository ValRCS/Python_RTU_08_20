class Song:
    def __init__(self, title = "", author ="", lyrics = ()):
        self.title = title
        self.author = author
        self.lyrics = lyrics
        if self.author and self.title :
            print(f"New Song made: {title} - {author}")
            
    # def _get_max_lines(self, line_count:int):
    #     if line_count and line_count <= len(self.lyrics):
    #        return line_count
    #     else:
    #        return len(self.lyrics)

    def _print_author_title(self):
        if self.author and self.title :
            print(f"***{self.title} - {self.author}***")
        return self

    def _print_rows(self, lines, max_lines=-1):
        if max_lines == -1:
            max_lines = len(lines)
        for row in lines[:max_lines]:
            print(row)
        print()
       
    def sing(self, max_lines=-1):
        self._print_author_title()
        self._print_rows(self.lyrics, max_lines)
        return self

    
    def yell(self, max_lines=-1):
        self._print_author_title()
        upper = [row.upper() for row in self.lyrics]
        self._print_rows(upper, max_lines)
        return self

title = "Thunder Without Rain"
author = "Brainstorm"
lyrics = ["It's like a thunder without rain,",
    "And like a week without sunday,",
    "Oh, like a book without last page,",
    "You want to buy a happy faith.","A storm without rain,",
    "Without any destruction.",
    "It's a good old game,",
    "Million pleasures, but no satisfaction."]
 
song =  Song(title, author, lyrics)

song.sing(2).yell(3).sing()
song.yell()

class Rap(Song):
    # we use __init__ constructor from Song
    
    def break_it(self, max_lines:int, drop = "Yeah"):
        self._print_author_title()
        rap_lines = [row.replace(" ", f" {drop.upper()} ") for row in self.lyrics]
        self._print_rows(rap_lines, max_lines)
        return self

zrap = Rap(title, author, lyrics)
 
zrap.break_it(3, "yah").yell(2).sing(4)