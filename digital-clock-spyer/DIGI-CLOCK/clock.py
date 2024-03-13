import time
from tkinter import Label

class Clock:
    def __init__(self, root, font=None):
        self.root = root
        self.font= "Arial 40"
        self.time_label = Label(root, font=self.font)
        self.date_label = Label(root, font=self.font)
        self.time_label.pack()
        self.date_label.pack()

    def update_clock(self):
        current_time = time.strftime('%I:%M:%S %p')
        current_date = time.strftime('%d-%m-%Y')
        self.time_label.config(text=f"{current_time}")
        self.date_label.config(text=f"{current_date}")
        self.root.after(1000, self.update_clock)

