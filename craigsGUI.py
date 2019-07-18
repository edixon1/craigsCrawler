from tkinter import *
from PIL import ImageTk, Image
import PIL
from resizeimage import resizeimage
import urllib.request
import shutil
import os
#def __init__(self, link_list, image_link_list, price_list, city_list):
#    self.linkList = link_list
#    self.imageList = image_list
#    self.priceList = price_list
#    self.cityList = city_list
#linkList = ["https://asheville.craigslist.org/grd/d/weaverville-alpacas/6930923148.html","https://asheville.craigslist.org/grd/d/weaverville-alpacas/6930923148.html","https://asheville.craigslist.org/grd/d/weaverville-alpacas/6930923148.html","https://asheville.craigslist.org/grd/d/weaverville-alpacas/6930923148.html","https://asheville.craigslist.org/grd/d/weaverville-alpacas/6930923148.html","https://asheville.craigslist.org/grd/d/weaverville-alpacas/6930923148.html","https://asheville.craigslist.org/grd/d/weaverville-alpacas/6930923148.html","https://asheville.craigslist.org/grd/d/weaverville-alpacas/6930923148.html","https://asheville.craigslist.org/grd/d/weaverville-alpacas/6930923148.html","https://asheville.craigslist.org/grd/d/weaverville-alpacas/6930923148.html"]
#cityList = ["Asheville","Asheville","Charlotte","Weaverville","Charlotte","Asheville","Wilmington", "Raleigh", "Asheville","Waynesville"]
#priceList = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
image_link_list = ['https://images.craigslist.org/00x0x_78IA8DYuBAu_600x450.jpg']
#image_list = []

#def rmimages():
#    os.mkdir('./testImages') #Create the directory where images will be stored


#imgNum = 0
#pathDirs = []
#for i in image_link_list:
#    urllib.request.urlretrieve(i, "./testimages/image" + str(imgNum) + ".jpg") #Save images to the newly created directory
#    imgNum += 1
#    pathDirs.append("./testImages/image" + str(imgNum) + ".jpg")

#shutil.rmtree('./testImages') #Deletes the image directory and its contents



root = Tk()
#for i in pathDirs:
#    img = Image.open(i)
#    tImg = ImageTk.PhotoImage(img) #converts to a TK image which can be used in any Tk widget
    #Need to make a dict which associates strings with canvas items so that I can add the images to the canvas items in a later for loop? (I think)
img = Image.open('./testImages/image0.jpg')


basewidth = 300 #Resizes the images
widthpercent = (basewidth / float(img.size[0]))
hsize = int((float(img.size[1]) * float(widthpercent)))
img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)


tImg = ImageTk.PhotoImage(img)
root.title("CraigsCrawler")
outerFrame = Frame(root, bg = 'white', height = 600, width = 1000)
outerFrame.pack()
innerFrame1 = Frame(outerFrame, bg = 'red')
innerFrame1.grid(row = 0, column = 0, padx = 20, pady = 20)
innerFrame2 = Frame(outerFrame, bg = 'blue', height = 400, width = 400)
innerFrame2.grid(row = 0, column = 1, padx = 20, pady = 20)
label = Label(innerFrame1, image = tImg, padx = 10, pady = 10)
label.pack()
root.mainloop()