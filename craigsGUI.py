from tkinter import *
import os.path
from PIL import ImageTk, Image
import PIL
import urllib.request
import shutil
import os

def __init__(self, link_list, image_link_list, price_list, city_list):
    addimages()
    self.linkList = link_list
    self.imageList = image_list
    self.priceList = price_list
    self.cityList = city_list

def test_main():
    make_GUI_boxes()

def add_images(): #creates a directory and adds images to it in jpeg format pulled from the URL
    imageNum = 0
    path_dirs = []
    os.mkdir('./craigsImages')
    for i in image_link_list:
        urllib.request.urlretrieve(i, "./craigsimages/image" + str(imageNum) + ".jpg")
        pathDirs.append("./craigsimages/image" + str(imageNum) + ".jpg")
        imageNum += 1

def rm_images():
    shutil.rmtree('') #Deletes the image directory and its contents

def make_gui():
    root = Tk()
    basewidth = 300 #Resizes the images
    abs_dir = os.path.dirname(os.path.abspath(__file__))
    x_grid = 0
    y_grid = 0
    for i in range(len(image_link_list)):
        img = Image.open(os.path.join(abs_dir, 'craigsImages/image' + str(i) + '.jpg'))
        widthpercent = (basewidth / float(img.size[0]))
        hsize = int((float(img.size[1]) * float(widthpercent)))
        img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        #why is this only displaying one?
        inner_frame = Frame(root, bg = 'blue', height = 600, width = 1000)
        label = Label(inner_frame, image = img, padx = 10, pady = 10)
        inner_frame.grid(row = x_grid, column = y_grid)
        print('packing image' + str(i) + 'at ' + str(x_grid) + str(y_grid))
        label.pack()
        if y_grid == 1:
            y_grid == 0
            x_grid += 1
        else:
            y_grid += 1
    root.mainloop()

image_link_list = ['test']
make_gui()
#root.title("CraigsCrawler")
#outerFrame = Frame(root, bg = 'white', height = 600, width = 1000)
#outerFrame.pack()
#innerFrame1 = Frame(outerFrame, bg = 'red', padx = 20, pady = 20, borderwidth = 1)
#innerFrame1.grid(row = 0, column = 0)

#label = Label(innerFrame1, image = tImg, padx = 10, pady = 10)
#label.pack()