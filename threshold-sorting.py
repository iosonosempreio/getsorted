#!/usr/bin/python
# -*- coding: utf-8 -*-

import Tkinter as tk
from Tkinter import Frame, BOTH
from PIL import ImageTk, Image
import time, os, subprocess

root = tk.Tk()
img = ImageTk.PhotoImage(Image.open("test.jpg"))
panel = tk.Label(root, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")
w=int(round(root.winfo_screenwidth()*0.9))
h=int(round(root.winfo_screenheight()*0.9))

class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, background="white")    
        self.parent = parent
        self.parent.title("getsorted")
        self.pack(fill=BOTH, expand=1)
        self.centerWindow()

    def centerWindow(self):
        # w = self.parent.winfo_screenwidth()*0.9
        # h = self.parent.winfo_screenheight()*0.9
        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()
        
        x = (sw - w)/2
        y = (sh - h)/2
        self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))

def callback(e):
    # take picture
    gp2process = "gphoto2 --capture-image-and-download --filename pics/img%H%M%S.jpg"
    gpout = subprocess.check_output(gp2process, stderr=subprocess.STDOUT, shell=True)
    gpout = gpout.split()
    gpout = gpout[12]
    newPath = gpout
    print "image captured: "+newPath
    # take captured img and resize it
    img0 = Image.open(newPath)
    #print (img0.size[0], img0.size[1])
    widthImg = 400
    heightImg = (widthImg * img0.size[1])/img0.size[0]
    img1 = img0.resize((widthImg, heightImg), Image.ANTIALIAS)
    newPathResized = newPath.replace(".jpg", "-resized.jpg")
    img1.save(newPathResized)
    print "image resized: "+newPathResized
    
    # display resized img
    # img2 = ImageTk.PhotoImage(Image.open(newPathResized))
    # panel.configure(image = img2)
    # panel.image = img2
    # time.sleep(0)

    # sorting process
    # pixelsortSubprocess = "python pixelsort/pixelsort.py " + newPathResized + " -a -45 -i waves -c 30 -o "+newPath.replace(".jpg","")+"-sorted.jpg"
    pixelsortSubprocess = "python pixelsort/pixelsort.py " + newPathResized + " -o "+newPath.replace(".jpg","")+"-sorted.jpg -a -45 -t 0.3 -u 0.7"
    output = subprocess.check_output(pixelsortSubprocess, stderr=subprocess.STDOUT, shell=True)
    output = output.split()
    output = output[-1].replace(')','')
    output = output.replace("'","")
    newPathSorted = output
    time.sleep(0)
    print "image pixels sorted: "+newPathSorted
    # display sorted img
    img3 = ImageTk.PhotoImage(Image.open(newPathSorted))
    panel.configure(image = img3)
    panel.image = img3

root.bind("<Return>", callback)
ex = Example(root)
root.mainloop()
