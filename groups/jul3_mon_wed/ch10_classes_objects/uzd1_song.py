class Song:
    """Class for representing a song
    Attributes:
        title (str): Song title
        author (str): Song author
        lyrics (tuple): Song lyrics
        Methods:
        sing (int): Sing the song
        yell (int): Yell the song
    Examples:
        >>> ziemelmeita = Song("Ziemeļmeita", "Jumprava", ["Gāju meklēt ziemeļmeitu","Garu, tālu ceļu veicu"])
    """	

    def __init__(self, title = "", author = "", lyrics = ()) -> None:
        self.title = title
        self.author = author
        self.lyrics = lyrics
        print(f"New Song made! Song title is {title}, author - {author}")

    # let's make a private function to print title and author with optiona upper flag
    # so since we will need to use this Rap class, we will make it protected
    # so we can use it in the child class
    def _print_title_author(self, upper = False): # single _ means protected by convention
        buffer = ""
        if self.title:
            buffer += "Title: " + self.title
        if self.author:
             if buffer:
                    buffer += ", "
             buffer += "Author: " + self.author
        if upper:
            print(buffer.upper())
        else:
            print(buffer)

    def sing(self, max_lines = -1):
        """Sing the song
        Args:
            max_lines (int, optional): Number of lines to sing. Defaults to -1.
        Returns:
            self
        """
        self._print_title_author()
        
        if max_lines == -1:
            max_lines = len(self.lyrics)
        for line in self.lyrics[:max_lines]:
                print(line)
        return self
    def yell(self, max_lines = -1):
        self._print_title_author(upper=True)
        
        if max_lines == -1:
            max_lines = len(self.lyrics)
        for line in self.lyrics[:max_lines]:
                print(line.upper())
        return self

 
 
ziemelmeita = Song("Ziemeļmeita", "Jumprava", ["Gāju meklēt ziemeļmeitu","Garu, tālu ceļu veicu"])
ziemelmeita.sing(1).yell()
 
tautumeita = Song("Sijā auzas tautu meita", lyrics= ["Sijā auzas tautu meita dod manam kumeļam", "Nesijāšu ne es došu netīk manam prātiņam", "Tam sijāšu tam es došu kas tīk manam prātiņam"])
tautumeita.sing().yell(2).yell(1)
 
meita = Song("Raudāja māte, raudāja meita", 
             "Raimonds Pauls", 
             lyrics= ["Par to, ka viļņi liedagā tā kā atmiņas krīt", 
                      "Par to, ka vēju modinās saule vientuļa rīt", 
                      "Par to, ka nepārnāks tas, kurš aizgājis", 
                      "Par to, ka bezgalīgas ir tikai debesis"])
meita.sing().yell(0).sing(3)

class Rap(Song):
  # we have everything from Song class already
  def break_it(self, max_lines=-1, drop="yeah"):
    # self.__print_title_author()
    # we need to __print_title_author() but it is private in Song class
    # so we need to copy it here
    # if we had private Song method __print_title_author() then we need this
    # self._Song__print_title_author() # this shows how nothing is truly private in Python
    # a little bit hacky, but we can use the fact that we know that __print_title_author() is private
    # so Python achieves privacy by mangling the name of the function
    # instead we can use regular method _print_title_author() which is protected
    self._print_title_author()
 
    print("\nDziesmas vārdi:")
    if max_lines == -1:
        max_lines = len(self.lyrics)
 
    for line in self.lyrics[:max_lines]:
        rap_list = []
        words = line.split()
        for word in words:
            rap_list += [word, drop] # could have used rap_list.extend([word, drop])
        rap_row_string = " ".join(rap_list) # we join our list into a string
        print(rap_row_string)
    return self


stefania = Rap("Stefania", "Kalush Orchestra", ("Стефанія мамо, мамо Стефанія", "Розквітає поле, а вона сивіє", "Заспівай мені мамо колискову", "Хочу ще почути твоє рідне слово", "Вона мене колисала дала мені ритм", "І напевне силу волі не забрати в мене, бо дала вона"))

stefania.break_it(2, "yo").yell(3)