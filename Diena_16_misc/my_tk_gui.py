import tkinter as tk # this is in standard library


class Application(tk.Frame):
    count = 5
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()


    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi #binding say_hi method to click
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")
        self.result = tk.Label(self)
        self.result["text"] = f"Result {self.count}"
        self.result.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")
        self.count += 1
        self.result["text"] = f"Result {self.count}" # hand made binding of hi button and result label


root = tk.Tk()
app = Application(master=root)
app.mainloop()
