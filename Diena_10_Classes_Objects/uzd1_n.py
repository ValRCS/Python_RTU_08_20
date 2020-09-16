class Song:
    def __init__(self, title='', author='', lyrics=set()):
        self.title = title
        self.author = author
        self.lyrics = lyrics

    def reference(self):
        if len(self.title) > 0 and len(self.author) > 0:
            return self.title + '-' + self.author
        elif len(self.title) == 0 and len(self.author) > 0:
            return "Nosaukums Nezināms - " + self.author
        elif len(self.title) > 0 and len(self.author) == 0:
            return self.title + " - Autors nezināms"
        else:
            return "Nosaukums Nezināms - Autors nezināms"

    def sing(self, rep=1, max_lines=-1):
        print(self.reference())

        for i in range(rep):
            n = 0
            for line in self.lyrics:
                print(str(line))
                n += 1
                if n == max_lines:
                    break

        print('')
        return self

    def yell(self, rep=1, max_lines=-1):
        print(self.reference())

        for i in range(rep):
            n = 0
            for line in self.lyrics:
                print(str(line).upper())
                n += 1
                if n == max_lines:
                    break

        print('')
        return self


ziemelmeita = Song("Ziemeļmeita", "Jumprava", [
                   "Gāju meklēt ziemeļmeitu", "Garu, tālu ceļu veicu"])
ziemelmeita.sing(2).yell(max_lines=1)


vardi = ['Tavās acīs dziestot kvēl', 'Kurtizāņu ugunskurs',
         'Un tev sevis mazliet žēl', 'Ka šīs liesmas vairs nevienu nenoburs']
kurtizani = Song('Kurtizāņu ugunskurs', 'Dakota', vardi)
kurtizani.sing().yell(max_lines=2)


class Rap(Song):
    def __init__(self, title='', author='', lyrics=set()):
        self.title = title
        self.author = author
        self.lyrics = lyrics

    def break_it(self, max_lines=1, drop='yeah'):
        n = 0
        if max_lines == -1:
            max_lines = len(self.lyrics)

        print(self.reference())
        while n != min(max_lines, len(self.lyrics)):
            print((' ' + drop.upper() + ' ').join(self.lyrics[n].split(' ')))
            n += 1
        return self


zrap = Rap("Ziemeļmeita", "Jumprava", [
           "Gāju meklēt ziemeļmeitu", "Garu, tālu ceļu veicu"])
zrap.break_it(2, "yah")

vardi = ['Kad barojām pīles, asaras krita tev lielas kā ozola zīles',
         'Laiki met lokus, dažreiz saule slēpjas kastaņu kokos',
         'Kā jūrnieki rumu tu gribi Munameģi, es braukšu uz Karakumu',
         'Ar sarkanām neļķēm, laiks atvadīties, ir rudens, ļaudis klīst pa vientuļām peļķēm']
Rudens = Rap("Rudens", "Prāta Vētra/Brainstorm", vardi)
# Rudens.break_it(-1, "jā")

print('')
Rudens.break_it(-1, "jā").sing().yell(1).break_it(drop="yo")
