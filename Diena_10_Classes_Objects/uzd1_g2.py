# Vitautam
# Definējiet klasi Song
# Klases construktora vajag būt trīs papildu 3 parametriem(self un vēl 3!)
# title pēc noklusējuma tukša string
# author pēc noklusējuma tukšs string
# lyrics pēc noklusējuma tukšs tuple
# konstruktors saglabātu šos trīs parametrus
# un papildu izdrukātu uz ekrāna "New Song made" - (pamēģiniet arī izdrukāt šeit author un title!)

class Song:
    def __init__(self, title='', author='', lyrics=()):
        self.title = title
        self.author = author
        self.lyrics = lyrics
        self.sep = ''

        if title and author:
            self.sep = '–'

        if title or author:
            print(f"Jauna dziesma tapa: {self.author} {self.sep} {self.title}")

    def print_title_author(self):
        if self.title or self.author:
            print(f"{self.author} {self.sep} {self.title}")

# Uzrakstiet metodi sing kas izdrukā dziesmu pa rindiņai uz ekrāna,
# vispirms izdrukājot autoru un title, ja tie ir.
    def sing(self):
        self.print_title_author()

        for l in self.lyrics:
            print(str(l))
        print()
        return self

# Uzrakstiet metodi yell kas izdrukā dziesmu ar lieliem burtiem pa rindiņai uz ekrāna,
# vispirms izdrukājot autoru un title, ja tie ir.
    def yell(self):
        self.print_title_author()

        for l in self.lyrics:
            print(str(l).upper())
        print()
        return self


class_zm = Song("Ziemeļmeita", "Jumprava",
                ("Gāju meklēt ziemeļmeitu", "Garu, tālu ceļu veicu"))
class_zm.sing().yell()

class_zm = Song("", "", ("Gāju meklēt ziemeļmeitu", "Garu, tālu ceļu veicu"))
class_zm.sing().yell()


class Rap(Song):
    def __init__(self, *args):
        super(Rap, self).__init__(*args)

    def break_it(self, max_lines=1, drop='yeah'):
        # if max_lines = -1, set all lines
        max_lines = (max_lines == -1) and len(self.lyrics) or max_lines

        for line in self.lyrics[:max_lines]:
            print(str(line).replace(
                ' ', ' ' + drop.upper() + ' ') + ' ' + drop.upper())

        print()
        return self


class_rap_zm = Rap("Ziemeļmeita", "Jumprava",
                   ("Gāju meklēt ziemeļmeitu", "Garu, tālu ceļu veicu"))
class_rap_zm.break_it(-1, 'Ō').break_it(1, 'ai')

class_rap_zm = Rap(
    "", "", ("Gāju meklēt ziemeļmeitu", "Garu, tālu ceļu veicu"))
class_rap_zm.break_it(3, 'Ō').break_it(-1, 'ai')

songs = [Song(f"Song {n}", "ACDC", ["ROCK", "ON"]) for n in range(5)]
songs[2].yell().sing().print_title_author()
raps = [Rap(f"Song {n}", "ACDC", ["ROCK", "ON"]) for n in range(5)]
raps[3].yell().sing().break_it(2, drop="yaaah").print_title_author()
