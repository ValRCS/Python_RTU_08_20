class Song:
 
    def __init__(self, title="", author="", lyrics=()):     
        self.title = title
        self.author = author
        self.lyrics = lyrics
       
    def song_intro(self):
        print(f"Song : {self.title} by {self.author}")
        return self
    
    def sing(self, max_lines=-1):
        self.song_intro()
 
        if max_lines == -1:
            max_lines = len(self.lyrics)

        for text in self.lyrics[:max_lines]:
            print(text)
        
        return self

 
    def yell(self, max_lines=-1):
        self.song_intro()
 
        if max_lines == -1:
            max_lines = len(self.lyrics)

        for text in self.lyrics[:max_lines]:
            print(text.upper())

        return self

my_song = Song("Hey Jude", "The Beatles", ("Na na na nananana", "nannana", "hey Jude.."))

my_song.sing().yell().sing(2)

wewillrockyou = Song("We Will Rock You", "Queen", ["Buddy, you're a boy, make a big noise", "Playing in the street, gonna be a big man someday",
"You gotot mud on your face, you big disgrace", "Kicking your can all over the place, singin'", 
"We will, we will rock you", 
"We will, we will rock you"])
wewillrockyou.sing().yell(2)
print(wewillrockyou.lyrics)

# Task 1B
 
class Rap(Song):
    def break_it(self, max_lines = -1, drop = "yeah"):
        print(f"{self.title} {('by ' + self.author)*(self.author != '')}")
        print()
        last_line = len(self.lyrics) if max_lines == -1 else min(len(self.lyrics), max_lines)
        rap_lyrics = []
        for row in self.lyrics[0:last_line]:
            row = "".join([char for char in row if char.isalnum() or str.isspace(char)]) # remove punctuation - it becomes meaningless if we put drops everywhere...
            rap_lyrics.append(" ".join([word + " " + drop.upper() for word in row.split()])) # add drop after each word
        print(*rap_lyrics, sep = "\n")
        print()
        return self
  
another_song = Rap("Dzeltenie aizkari", "Dālderi", ["Tu tikai skudru nesamin,", "Kas pagalmā veļ baļķi tālā lielceļa garumā", "Tā pastāstīs, kā gurdums izgaist citu rīt", "Viss gurdums ar jau izgaist citurīt."])
another_song.break_it(3,"yah").yell(1)