#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
ZetCode Tkinter tutorial

This script shows a simple window
on the screen.

Author: Jan Bodnar
Last modified: November 2015
Website: www.zetcode.com
"""

from Tkinter import Tk, Frame, BOTH
from ttk import Button, Style


class myApp(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent, background="white")
        self.parent = parent
        self.initUI()
    
    def initUI(self):
        w = self.parent.winfo_screenwidth()/2
        h = self.parent.winfo_screenheight()/2

        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()

        x = (sw - w)/2
        y = (sh - h)/2

        self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))

        self.parent.title("myApp")
        self.style = Style()
        self.style.theme_use("default")

        self.pack(fill=BOTH, expand=1)

        quitButton = Button(self, text="Quit",
            command=self.quit)
        quitButton.place(x=w/2, y=h/2)
        


        
        

def main():
  
    root = Tk()
    #
    app = myApp(root)
    root.mainloop()  


if __name__ == '__main__':
    main()