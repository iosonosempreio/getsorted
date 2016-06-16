#!/usr/bin/python
# -*- coding: utf-8 -*-

from PIL import Image, ImageTk
from Tkinter import Tk, Label, BOTH
from ttk import Frame, Style
import time, os, subprocess

def main():

    root = Tk()
    
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
            self.parent.title("getsorted 0.1 - Lambrock Festival Edition")
            self.pack(fill=BOTH, expand=1)
            Style().configure("TFrame", background="#000")
       
    app = Example(root)

    

    def resizeImgWeightBased(img, finalWidth):
        finalHeight = int(round((finalWidth * img.size[1])/img.size[0]))
##        Different algorithms are: NEAREST, BILINEAR, BICUBIC, LANNCZOS
        resizedImage = img.resize((finalWidth, finalHeight), Image.NEAREST)
        print("final width",resizedImage.size[0],"final height",resizedImage.size[1])
        return resizedImage

    def resizeImgHeightBased(img, finalHeight):
        finalWidth = int(round( (img.size[0]*finalHeight)/img.size[1]  ))
##        Different algorithms are: NEAREST, BILINEAR, BICUBIC, LANNCZOS
        resizedImage = img.resize((finalWidth, finalHeight), Image.NEAREST)
        print("final width",resizedImage.size[0],"final height",resizedImage.size[1])
        return resizedImage
    
    # This is how to display the image, needs to be done once in the main function
    # this way label object and all its friends are defined
    myImg = resizeImgHeightBased(Image.open("lambrock.jpg"), root.winfo_screenheight())
    myImage = ImageTk.PhotoImage(myImg)
    label = Label(root)
    label.configure(image=myImage, bd=0)
    label.image = myImage
    xLabel = (root.winfo_screenwidth() - myImg.size[0])/2
    yLabel = (root.winfo_screenheight() - myImg.size[1])/2
    label.place(x=xLabel, y=yLabel)
    label.update_idletasks()

    def takePictureSortAndDisplay(event):
        
##        take picture
        gp2process = "gphoto2 --capture-image-and-download --filename pics/img%H%M%S.jpg"
        gpout = subprocess.check_output(gp2process, stderr=subprocess.STDOUT, shell=True)
        gpout = gpout.split()
        gpout = gpout[12]
        newPath = gpout
        print "image captured and saved: "+newPath

##        take captured img and resize, display and save it
        myImg = resizeImgHeightBased(Image.open(newPath), root.winfo_screenheight())
        newPathResized = newPath.replace(".jpg", "-resized.jpg")
        myImg.save(newPathResized)
        print "image resized saved: "+newPathResized

        ##        display resized image
        myImg = Image.open(newPathResized)
        myImage = ImageTk.PhotoImage(myImg)
        label.configure(image=myImage)
        label.image = myImage
        xLabel = (root.winfo_screenwidth() - myImg.size[0])/2
        yLabel = (root.winfo_screenheight() - myImg.size[1])/2
        label.place(x=xLabel, y=yLabel)
        label.update_idletasks()

        print "image resized displayed"

        time.sleep(0.2)

        ##        take resized img and resize it to a smaller one in order to accellerate the sorting process
        myImg = resizeImgHeightBased(Image.open(newPathResized), root.winfo_screenheight()/3)
        newPathVerySmall = newPathResized.replace("-resized.jpg", "-verysmall.jpg")
        myImg.save(newPathVerySmall)
        print "image very small saved: "+newPathVerySmall
        
        
##        sorting process
        pixelsortSubprocess = "python pixelsort/pixelsort.py " + newPathVerySmall + " -a -90 -i waves -c 20 -o "+newPath.replace(".jpg","")+"-sorted.jpg"
##        pixelsortSubprocess = "python pixelsort/pixelsort.py " + newPathVerySmall + " -o "+newPath.replace(".jpg","")+"-sorted.jpg -a -90 -i threshold -t 0.3 -u 0.7"
        print "starting to sort"
        output = subprocess.check_output(pixelsortSubprocess, stderr=subprocess.STDOUT, shell=True)
        output = output.split()
        output = output[-1].replace(')','')
        output = output.replace("'","")
        newPathSorted = output
        print "image pixels sorted: "+newPathSorted

##        display sorted image
        myImg = resizeImgHeightBased(Image.open(newPathSorted), root.winfo_screenheight())
        myImage = ImageTk.PhotoImage(myImg)
        label.configure(image=myImage)
        label.image = myImage
        xLabel = (root.winfo_screenwidth() - myImg.size[0])/2
        yLabel = (root.winfo_screenheight() - myImg.size[1])/2
        label.place(x=xLabel, y=yLabel)
        label.update_idletasks()

        print "sorted image displayed"

##        welldone
        time.sleep(0.25)
        print "ready for next round"
    
    root.bind("<Return>", takePictureSortAndDisplay)
    root.bind("<Escape>", lambda e: e.widget.quit())    
    root.mainloop()


if __name__ == '__main__':
    main()
