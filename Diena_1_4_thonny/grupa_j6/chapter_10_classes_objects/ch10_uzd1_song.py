class Song:
    song_type = "Pop" # default value
    # crucial point is to pass the default lyrics as a tuple
    # passing a list as default will cause problems
    # all instances will share the same list!!!
    # if i pass lyrics, I can pass a list then
    def __init__(self, title="", author="", lyrics=()):
        self.title = title
        self.author = author
        self.lyrics = lyrics
        print(f"New song created!")
        self._print_title_author()
 
    # with _ we indicate that this method is for internal use only
    # however it is not a private method
    # outside the class we can still call it
    def _print_title_author(self):
        if self.title != "":
            print(f"Song: {self.title}")
        if self.author != "":
            print(f"Author: {self.author}")
        if self.song_type != "":
            print(f"Type: {self.song_type}")

    def sing(self,maxlines=-1):
        self._print_title_author()
        if maxlines == -1:
            maxlines = len(self.lyrics)
        self.print_lyrics(self.lyrics[:maxlines])
        return self
 
    def yell(self, maxlines=-1):
        self._print_title_author()
        if maxlines == -1:
            maxlines = len(self.lyrics)
        # for line in self.lyrics[:maxlines]:
        #     print(line.upper())
        self.print_lyrics([line.upper() for line in self.lyrics[:maxlines]])
        return self
    
    # let's add whisper method
    def whisper(self, maxlines=-1):
        self._print_title_author()
        if maxlines == -1:
            maxlines = len(self.lyrics)
        # for line in self.lyrics[:maxlines]:
        #     print(line.lower())
        self.print_lyrics([line.lower() for line in self.lyrics[:maxlines]])
        # i think loop is better here
        return self
    
    # we could make a generic print_lyrics method
    # but it is not necessary
    def print_lyrics(self, lyrics):
        for line in lyrics:
            print(line)
        return self
    
    def clean_and_split(self,max_lines=0):
        # cleaned=self.lyrics.replace("\r","").strip().split("\n")
        cleaned=[line.strip() for line in self.lyrics if line.strip() != ""]
        return cleaned[0:max_lines] if max_lines > 0 else  cleaned
    
# let's make a song
song1 = Song("Happy Birthday", "Unknown", 
             ("Happy birthday to you", 
              "I don't want to get sued", 
              "So I'll stop right there"))

song1.sing()
song1.yell(1).sing(2)

lyrics = (
    "Empty spaces, what are we living for?",
    "Abandoned places, I guess we know the score",
    "On and on, does anybody know what we are looking for?",
    "Another hero, another mindless crime",
    "Behind the curtain, in the pantomime",
    "Hold the line, does anybody want to take it anymore?",
    "",
    "The show must go on",
    "The show must go on, yeah",
    "Inside my heart is breaking",
    "My makeup may be flaking",
    "But my smile, still, stays on",
    "",
    "Whatever happens, I'll leave it all to chance",
    "Another heartache, another failed romance",
    "On and on, does anybody know what we are living for?",
    "I guess I'm learning (I'm learning), I must be warmer now",
    "I'll soon be turning (turning, turning, turning), 'round the corner now",
    "Outside the dawn is breaking",
    "But inside in the dark, I'm aching to be free",
    "",
    "The show must go on",
    "The show must go on, yeah",
    "Ooh, inside my heart is breaking",
    "My makeup may be flaking",
    "But my smile, still, stays on",
    "",
    "Yeah-yeah",
    "Whoa-ooh, whoa-ooh, whoa-ooh",
    "My soul is painted like the wings of butterflies",
    "Fairytales of yesterday will grow but never die",
    "I can fly (fly, fly, fly), my friends"
)
 
 
show_must = Song("Show must go on", "Queen", lyrics)
show_must.sing(3).yell(5).whisper(2)

class Rap(Song):
    song_type = "Rap"
    # we can access song_type with self.song_type
    
    # we could write our own constructor
    # then we might want to call parent constructor
    def __init__(self, title="", author="", lyrics=()):
        # we might want to call parent constructor to set the attributes
        # super().__init__(title,author,lyrics)
        # or
        Song.__init__(self,title,author,lyrics)
        # so we use this if we want some costum construction logic
        print(f"New rap created!")
        # self._print_title_author() no need since we call parent constructor
        # in our case this was not necessary since our parent constructor was good enough

    def break_it(self,max_lines=0,drop="YEAH"):
        clean_lyrics=self.clean_and_split(max_lines)
        self._print_title_author()
        for line in clean_lyrics:
            # for vards in line.split():
            #     print(f"{vards} {drop} ",end="")
            # below avoids the extra space at the end
            rap_line = " ".join([f"{vards} {drop}" for vards in line.split()])
            print(rap_line)
            # print() 
        return self

rap1 = Rap("Ziemeļmeita","Jumprava",
           ("Gāju meklēt ziemēļmeitu",
            "Tālu garu ceļu veicu",
            "Pāri ledus laukam, pāri jūrai"))

# rap1.sing(2).break_it(2,"AHH")
