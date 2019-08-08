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

def addimages(): #creates a directory and adds images to it in jpeg format pulled from the URL
    imageNum = 0
    pathDirs = []
    os.mkdir('./testImages')
    for i in image_link_list:
        urllib.request.urlretrieve(i, "./testimages/image" + str(imageNum) + ".jpg")
        pathDirs.append("./testImages/image" + str(imageNum) + ".jpg")
        imageNum += 1

def rmimages():
    shutil.rmtree('./testImages') #Deletes the image directory and its contents

def make_GUI_boxes(): #creates the widgets inide of the GUI (this allows for a variable number of inputs)
    tk_img_dict = {}
    tk_border_dict = {}
    counter = 0
    abs_dir = os.path.dirname(os.path.abspath(__file__))
    for i in range(len(image_link_list)):
        img = Image.open(os.path.join(abs_dir, 'testImages/image' + str(counter) + '.jpg'))
        tk_img_dict.update({counter: img})


image_link_list = ['https://images.craigslist.org/00x0x_78IA8DYuBAu_600x450.jpg']
test_main()


#linkList = ["https://asheville.craigslist.org/grd/d/weaverville-alpacas/6930923148.html","https://asheville.craigslist.org/grd/d/weaverville-alpacas/6930923148.html","https://asheville.craigslist.org/grd/d/weaverville-alpacas/6930923148.html","https://asheville.craigslist.org/grd/d/weaverville-alpacas/6930923148.html","https://asheville.craigslist.org/grd/d/weaverville-alpacas/6930923148.html","https://asheville.craigslist.org/grd/d/weaverville-alpacas/6930923148.html","https://asheville.craigslist.org/grd/d/weaverville-alpacas/6930923148.html","https://asheville.craigslist.org/grd/d/weaverville-alpacas/6930923148.html","https://asheville.craigslist.org/grd/d/weaverville-alpacas/6930923148.html","https://asheville.craigslist.org/grd/d/weaverville-alpacas/6930923148.html"]
#cityList = ["Asheville","Asheville","Charlotte","Weaverville","Charlotte","Asheville","Wilmington", "Raleigh", "Asheville","Waynesville"]
#priceList = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]


#root = Tk()
#basewidth = 300 #Resizes the images
#widthpercent = (basewidth / float(img.size[0]))
#hsize = int((float(img.size[1]) * float(widthpercent)))
#img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)


#tImg = ImageTk.PhotoImage(img)
#root.title("CraigsCrawler")
#outerFrame = Frame(root, bg = 'white', height = 600, width = 1000)
#outerFrame.pack()
#innerFrame1 = Frame(outerFrame, bg = 'red', padx = 20, pady = 20, borderwidth = 1)
#innerFrame1.grid(row = 0, column = 0)

#label = Label(innerFrame1, image = tImg, padx = 10, pady = 10)
#label.pack()
#root.mainloop()