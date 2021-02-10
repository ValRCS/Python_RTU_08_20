# Definējiet klasi Song
# Klases construktora vajag būt trīs papildu 3 parametriem(self un vēl 3!)
# title pēc noklusējuma tukša string
# author pēc noklusējuma tukšs string
# lyrics pēc noklusējuma tukšs tuple
# konstruktors saglabātu šos trīs parametrus
# un papildu izdrukātu uz ekrāna "New Song made" - (pamēģiniet arī izdrukāt šeit author un title!)
# Uzrakstiet metodi sing kas izdrukā dziesmu pa rindiņai uz ekrāna, vispirms izdrukājot autoru un title, ja tie ir.
# Uzrakstiet metodi yell kas izdrukā dziesmu ar lieliem burtiem pa rindiņai uz ekrāna, vispirms izdrukājot autoru un title, ja tie ir.
# Bonuss: uztaisiet lai sing un yell varam izsaukt vairākas reizes (ķēdejot)
# Bonuss: uztaisiet papildu parametru max_lines, kas izdrukā tikai noteiktu rindiņu skaitu gan sing gan yell. Labāk taisiet ar kādu default vērtību piem. -1 , pie kuras tad izdrukā visas rindas.
# Par ķēdēšano bija šeit: https://www.das.lv/platforma/mod/page/view.php?id=1794
# Izveidojiet vairākas dziesmas ar dziesmu tekstiem
# Piemērs:
# ziemelmeita = Song("Ziemeļmeita", "Jumprava", ["Gāju meklēt ziemeļmeitu","
# Garu, tālu ceļu veicu"])
# ziemelmeita.sing(1).yell()
# Rezultāts uz ekrāna:
# Ziemeļmeita - Jumprava
# Gāju meklēt ziemeļmeitu
# Ziemeļmeita - Jumprava
# GĀJU MEKLĒT ZIEMEĻMEITU
# GARU, TĀLU CEĻU VEICU
#
# 1.B
# Tie kas jūtas komfortabli, uztaisiet Rap klasi kas manto no Song
# Papildu metode break_it ar diviem noklusētiem parametriem max_lines un drop vienādu ar "yeah", kura līdzīga sing, bet pievienot drop aiz katra vārda...
# zrap = Rap("Ziemeļmeita", "Jumprava", ["Gāju meklēt ziemeļmeitu","
# Garu, tālu ceļu veicu"])
# zrap.break_it(1, "yah")
# Ziemeļmeita - Jumprava
# Gāju YAH meklēt YAH ziemeļmeitu YAH
 
class Song:
    def print_name(self):
        if self.title != "":
            if self.author != "":
                print(f"{self.title} - {self.author}")
            else:
                print(f"{self.title}")
        else:
            if self.author != "":
                print(f"Unknown song name - {self.author}")
        return self
 
    def __init__(self,title="",author="",lyrics=()):
        self.title = title
        self.author = author
        self.lyrics = list(lyrics)
        print(f"New Song Made: {author} - {title}")
 
    # could be some efficiency by reusing same __print_lyrics function
    def __print_lyrics(self, lyrics):
        for line in lyrics:
            print(line)

    def sing(self, max_lines=-1):
        print(f"{self.title} - {self.author}")
        lyrics = self.lyrics
        if max_lines != -1:
            lyrics = lyrics[:max_lines]
        self.__print_lyrics(lyrics)

        return self
 
    def yell(self, max_lines=-1):
        print(f"{self.title} - {self.author}")
 
        for index, x in enumerate(self.lyrics):
            print(x.upper())
            if index == (max_lines - 1):
                break
        return self
 
 
my_song = Song("Ziemeļmeita", "Jumprava", [
               "Gāju meklēt ziemeļmeitu", "Garu, tālu ceļu veicu"])
my_song.sing(1).yell()
 
class Rap(Song):
    def break_it(self, max_lines=-1, drop="yeah"):
        """
        prints drop after each word in lyrics
        max_lines specificy how many lines of lyrics will be printed
        """
        self.print_name()

        for index, line in enumerate(self.lyrics):
            words = line.split(" ")
            for word in words:
                print(f"{word} {drop.upper()} ", end="")
            print()
            if index == (max_lines - 1):
                break
        return self
 
ziemelmeita = Song("Ziemeļmeita", "Jumprava", ["Gāju meklēt ziemeļmeitu","Garu, tālu ceļu veicu"])
ziemelmeita.sing(1).yell()
zrap = Rap("Ziemeļmeita", "Jumprava", ["Gāju meklēt ziemeļmeitu","Garu, tālu ceļu veicu"])
zrap.break_it(1, "yah")
ziemelmeita.sing(50)
my_song = Rap('Use My Voice', 'Evanescence', ['Whether you like it or not', 'You\'re gonna take what I got', 'If we can\'t talk about it', 'we\'ll just keep drowning in it'])
my_song.break_it(2).sing(3).yell()
my_song.break_it(drop="Wow")
