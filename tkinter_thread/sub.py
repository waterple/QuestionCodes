from tkinter import *
import threading
from time import sleep

class Window:
    def __init__(self):
        self.run = True
        self.app = Tk()
        
        self.btn = Button(self.app, text='crash')
        self.btn.bind('<Button-1>', lambda e : self.crash())
        self.btn.pack()

    def thread(self):
        self.th = threading.Thread(target=self.work, args=(True,))
        self.th.daemon = True
        self.th.start()

    def work(self, running=True):
        while self.run:
            print('    work')
            sleep(.1)

    def crash(self):
        self.run = False
        self.app.destroy()