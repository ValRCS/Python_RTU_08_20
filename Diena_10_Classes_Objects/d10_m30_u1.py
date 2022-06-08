# Definējiet klasi Song
from tokenize import blank_re


class Song:
    # return tuple from multiline string, seperated by \n
    @classmethod # this works even when no objects are made from Song class
    def str_to_tuple(cls, text):
        if isinstance(text, (list, tuple)):
            return tuple(text)
        elif isinstance(text, str):
            temp = list(str(text).rsplit('\n'))
            for line in range(1, len(temp)):
                if temp[line] == '':
                    temp[line-1] += '\n'
            return [line for line in temp if line != '']
        else:
            return tuple('corrupt lyrics')

    def __init__(self, title="", author="", lyrics=()):
        self.title=title
        self.author=author
        self.lyrics=lyrics

    def print_author_and_title(self):
        # print("Song: "+ self.title + " Author: " + self.author)
        print(f"Song: {self.title} Author: {self.author}")
        return self

    def sing(self, max_lines=0):
        self.print_author_and_title()
        if max_lines == 0:
            lyrics = self.lyrics
        else:
            lyrics = self.lyrics[:max_lines]
        for line in lyrics:
            print(line)
        return self

    def yell(self, max_lines=0):
        self.print_author_and_title()
        if max_lines == 0:
            lyrics = self.lyrics
        else:
            lyrics = self.lyrics[:max_lines]
        for line in lyrics:
            print(str(line).upper())
        return self

ziemelmeita=Song("Ziemeļmeita", "Jumprava", ["Gāju meklēt ziemeļmeitu","Garu, tālu ceļu veicu"])
#ziemelmeita._init_("Ziemeļmeita", "Jumprava", ["Gāju meklēt ziemeļmeitu","Garu, tālu ceļu veicu"])
ziemelmeita.sing(1).yell(2)

blank_song = Song()
blank_song.print_author_and_title()
blank_song.sing().yell()


 
 
new_title = 'Rap Song Title'
new_author = 'Rap Song Author'
new_lyrics = '''Ai jel manu vieglu prātu
Jauns apņēmu līgaviņ`
Ai jel manu vieglu prātu
Jauns apņēmu līgaviņ`'''

new_title = 'Aj, jel manu vieglu prātu'
new_author = 'Ainars Mielavs'
new_lyrics = '''Ai, jel manu vieglu prātu:
Jauns apņēmu līgaviņ`!
Ai, jel manu vieglu prātu:
Jauns apņēmu līgaviņ`!
 
Ne gadiņa nedzīvoju,
Sola kungi karā ņemt.
Ne gadiņa nedzīvoju,
Sola kungi karā ņemt.
 
Es kungiem`i atbildēju:
Vai es viens`i karavīrs.
Es kungiem`i atbildēju:
Vai es viens`i karavīrs.
 
Vēl daža`i māmiņai
Aug deviņi bāleliņ.
Vēl daža`i māmiņai
Aug deviņi bāleliņ.
 
Tie varēja bruņas nesti,
Zobentiņus cilināt.
Tie varēja bruņas nesti,
Zobentiņus cilināt.
 
Ai, jel manu vieglu prātu,
Jauns apņēmu līgaviņ!
Ai, jel manu vieglu prātu,
Jauns apņēmu līgaviņ!'''

# so we call Song.str_to_tuple before we have any songs
song_1 = Song(new_title, new_author, Song.str_to_tuple(new_lyrics))
song_1.yell(4).sing(3).yell()

# 1.B
class Rap(Song):
    def break_it(self, max_lines=0, drop="yeah"):
        self.print_author_and_title()
        if max_lines == 0:
            lyrics = self.lyrics
        else:
            lyrics = self.lyrics[:max_lines]
        for line in lyrics:
            line = str(line).replace(" ", " "+drop+" ")
            print(line)
        return self

# so Rap inherits the Song class method as well
new_rap = Rap(new_title, new_author, Rap.str_to_tuple(new_lyrics))

new_rap.yell(3).break_it(4, "oh yeah")