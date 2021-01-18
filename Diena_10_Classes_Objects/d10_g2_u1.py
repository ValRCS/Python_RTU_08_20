class Song:
 
    def __init__(self, author, title , album, lyrics = ()):
        self.author = author
        self.title = title
        self.album = album
        self.lyrics = lyrics
        self.print_header()
 
    def print_header(self):
        if self.title == "":
            self.title = 'Unknown'
        if self.author == "":
            self.author = 'Unknown'
        print(f'{self.title} - {self.author} - {self.album}')
    
    def print_lyrics(self, lyrics, max_lines = -1, is_yell = False, is_break = False, drop = ''):
        if max_lines < 0:
            max_lines = len(lyrics)
        if is_break:
            for line in lyrics[:max_lines]:
                for word in line.split():
                    print(word, end = f' {drop.upper()} ')
                print()
        elif is_yell:
            [print(line.upper()) for line in lyrics[:max_lines]]
        else:
            [print(line) for line in lyrics[:max_lines]]
 
    def sing(self, max_lines = -1):
        self.print_header()
        self.print_lyrics(self.lyrics, max_lines)
        return self
 
    def yell(self, max_lines = -1):
        self.print_header()
        self.print_lyrics(self.lyrics, max_lines, is_yell = True)
        return self


class Rap(Song):
    def break_it(self, max_lines = -1, drop = 'yeah'):
        self.print_header()
        self.print_lyrics(self.lyrics, max_lines, is_break = True, drop = drop)
        return self

mysong = Song("Ziemeļmeita", "Jumprava", "Jumprava 1", ["Gāju meklēt ziemeļmeitu","Garu, tālu ceļu veicu", "Lēni un par vēlu nācu", "Meklējot šo ziemeļmalu"])
mysong.sing(1).yell()

aha = Rap('"The Sun Always Shines on TV"','A-HA', 'Hunting High And Low', ['Touch me', 'How can it be?', 'Believe me', 'The sun always shines on TV'])
aha.sing(2).break_it(drop="Yo")
