#!/usr/bin/python
# -*- coding: utf-8 -*-

from PIL import Image, ImageTk
from Tkinter import Tk, Label, BOTH
from ttk import Frame, Style

def main():

    class Example(Frame):
      
        def __init__(self, parent):
            Frame.__init__(self, parent)    
            self.parent = parent
            self.initUI()
            
        def initUI(self):
            w = self.parent.winfo_screenwidth()/1
            h = self.parent.winfo_screenheight()/1
            sw = self.parent.winfo_screenwidth()
            sh = self.parent.winfo_screenheight()
            x = (sw - w)/2
            y = (sh - h)/2
            self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))
            self.parent.title("Cool Positioning")
            self.pack(fill=BOTH, expand=1)
            Style().configure("TFrame", background="#000")     
         
    def changeImage(event):
        #print "clicked at", event.x, event.y, "typed ", event.char
        if event.char == "1":
            print event.char
            myImg = resizeImg(Image.open("bardejov.jpg"), root.winfo_screenwidth())
            myImage = ImageTk.PhotoImage(myImg)
            label = Label(root, image=myImage)
            label.image = myImage
            xLabel = (root.winfo_screenwidth() - myImg.size[0])/2
            yLabel = (root.winfo_screenheight() - myImg.size[1])/2
            label.place(x=xLabel, y=yLabel)

        if event.char == "2":
            print event.char
            myImg = resizeImg(Image.open("rotunda.jpg"), root.winfo_screenwidth())
            myImage = ImageTk.PhotoImage(myImg)
            label = Label(root, image=myImage)
            label.image = myImage
            xLabel = (root.winfo_screenwidth() - myImg.size[0])/2
            yLabel = (root.winfo_screenheight() - myImg.size[1])/2
            label.place(x=xLabel, y=yLabel)

        if event.char == "3":
            print event.char
            myImg = resizeImg(Image.open("mincol.jpg"), root.winfo_screenwidth())
            myImage = ImageTk.PhotoImage(myImg)
            label = Label(root, image=myImage)
            label.image = myImage
            xLabel = (root.winfo_screenwidth() - myImg.size[0])/2
            yLabel = (root.winfo_screenheight() - myImg.size[1])/2
            label.place(x=xLabel, y=yLabel)

    def resizeImg(img, finalWidth):
        finalHeight = int(round((finalWidth * img.size[1])/img.size[0]))
        resizedImage = img.resize((finalWidth, finalHeight), Image.ANTIALIAS)
        #print("final width",resizedImage.size[0],"final height",resizedImage.size[1])
        return resizedImage
        
    root = Tk()   
    app = Example(root)
    
    # This is how to display the image, needs to be done once in the main function
    # this way label object and all its friends are defined
    myImg = resizeImg(Image.open("bardejov.jpg"), root.winfo_screenwidth())
    myImage = ImageTk.PhotoImage(myImg)
    label = Label(root, image=myImage)
    label.image = myImage
    xLabel = (root.winfo_screenwidth() - myImg.size[0])/2
    yLabel = (root.winfo_screenheight() - myImg.size[1])/2
    label.place(x=xLabel, y=yLabel)
    
    root.bind("<Key>", changeImage)
    root.bind("<Escape>", lambda e: e.widget.quit())    
    root.mainloop()


if __name__ == '__main__':
    main()