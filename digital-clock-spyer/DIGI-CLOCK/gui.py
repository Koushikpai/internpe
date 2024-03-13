from tkinter import Tk, font
from clock import Clock

class GUI:
    def __init__(self, width=200, height=200):
        self.root = Tk()
        self.root.geometry(f"{width}x{height}")
        self.root.title('Digital Clock')
        # Define the font size
        self.font = font.Font(size=40)
        self.clock = Clock(self.root, font=self.font)

   # Pack the time and date labels
        self.clock.time_label.pack()
        self.clock.date_label.pack()

    def run(self):
        self.clock.update_clock()
        self.root.mainloop()

if __name__ == "__main__":
    gui = GUI(500, 120)
    gui.run()
