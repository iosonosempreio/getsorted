#test gphoto2

#!/usr/bin/python

import subprocess

from PIL import Image

# gpout = subprocess.check_output("gphoto2 --get-file 2690", stderr=subprocess.STDOUT, shell=True);

# print(gpout)

# imageFile = gpout.split()[3]

imageFile = "test.jpg"

# open an image file (.bmp,.jpg,.png,.gif) you have in the working folder
im1 = Image.open(imageFile)

print(im1.size[0])
print(im1.size[1])

# adjust width and height to your needs
width = 800
height = (width * im1.size[1])/im1.size[0]


# use one of these filter options to resize the image
    # cubic spline interpolation in a 4x4 environment
im5 = im1.resize((width, height), Image.ANTIALIAS)    # best down-sizing filter
ext = ".jpg"

im5.save(imageFile)

print(imageFile + " resized")

# output = subprocess.check_output("python pixelsort/pixelsort.py " + imageFile + " -a -45 -i waves -c 30", stderr=subprocess.STDOUT, shell=True)

output = subprocess.check_output("python pixelsort/pixelsort.py " + imageFile + " -i threshold -t 0.2 -u 0.6", stderr=subprocess.STDOUT, shell=True)

