from tkinter import Tk, Label, Button
import game.blackjack_object as mygame

class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("Black-Jack Game!")

        self.label = Label(master, text="Play Black-Jack")
        self.label.pack()

        self.greet_button = Button(master, text="Start", command=mygame.start_play)
        self.greet_button.pack()
        self.greet_button1 = Button(master, text="Hit", command=mygame.hit)
        self.greet_button1.pack()
        self.greet_button2 = Button(master, text="Stand", command=mygame.stand)
        self.greet_button2.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    # def greet(self):
    #     print("Greetings!")

root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()