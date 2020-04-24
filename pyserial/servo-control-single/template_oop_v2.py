#from tkinter import Tk, Label, Button, StringVar
import tkinter as tk
from tkinter import ttk

class MyFirstGUI:
    LABEL_TEXT = [
        "This is our first GUI!",
        "Actually, this is our second GUI.",
        "We made it more interesting...",
        "...by making this label interactive.",
        "Go on, click on it again.",
    ]
    def __init__(self, master, *args, **kwargs):
        self.master = master
        master.title("A simple GUI")

        self.label_index = 0
        self.label_text = tk.StringVar()
        self.label_text.set(self.LABEL_TEXT[self.label_index])
        self.label = tk.Label(master, textvariable=self.label_text)
        self.label.bind("<Button-1>", self.cycle_label_text)
        self.label.pack()

        self.greet_button = tk.Button(master, text="Greet", command=self.greet)
        self.greet_button.pack()

        self.close_button = tk.Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def greet(self):
        print("Greetings!")

    def cycle_label_text(self, event):
        self.label_index += 1
        self.label_index %= len(self.LABEL_TEXT) # wrap around
        self.label_text.set(self.LABEL_TEXT[self.label_index])

if __name__ == "__main__":

    root = tk.Tk()
    my_gui = MyFirstGUI(root)
    root.mainloop()