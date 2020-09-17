class Song:
    def __init__(self, author="Unknown", title="Unknown", lyric="Unknown"):
        self.author = author
        self.title = title
        self.lyric = lyric
        print(f"New Song Made: {self.author} - {self.title}")

    def sing(self, num):
        print(f"{self.author} - {self.title}")
        if num < 0:
            for line in self.lyric:
                print(f"{line}")
        else:
            i = 0
            cnt = len(self.lyric)
            if num > cnt:
                print("Dziesmā nav tik daudz rindu")
            else:
                while i != num:
                    print(f"{self.lyric[i]}")
                    i += 1
        return self

    def yell(self):
        print(f"{self.author} - {self.title}")
        for line in self.lyric:
            print(f"{line.upper()}")
        return self


class Rap(Song):
    def __init__(self, author="Unknown", title="Unknown", lyric="Unknown"):
        super().__init__(author, title, lyric)
        # print(f"New Song Made: {self.author} - {self.title}")


def main():
    ziemelmeita = Song("Jumprava", "Ziemelmeita", [
                       "Gāju meklēt Ziemeļmeitu", "garu tālu ceļu veicu", "un atradu to grāvi beigtu"])
    ziemelmeita.sing(1).sing(2).sing(3).sing(4)

    zrap = Rap("Jumprava", "Ziemelmeita", [
               "Gāju meklēt Ziemeļmeitu", "garu tālu ceļu veicu", "un atradu to grāvi beigtu"])
    zrap.yell()


if __name__ == "__main__":
    main()
