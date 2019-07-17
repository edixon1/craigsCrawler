from tkinter import *
from PIL import ImageTk, Image
from io import BytesIO
import requests
import os

# def __init__(self, link_list, image_list, price_list, city_list):
#    self.linkList = link_list
#    self.imageList = image_list
#    self.priceList = price_list
#    self.cityList = city_list
linkList = ["https://asheville.craigslist.org/grd/d/weaverville-alpacas/6930923148.html","https://asheville.craigslist.org/grd/d/weaverville-alpacas/6930923148.html","https://asheville.craigslist.org/grd/d/weaverville-alpacas/6930923148.html","https://asheville.craigslist.org/grd/d/weaverville-alpacas/6930923148.html","https://asheville.craigslist.org/grd/d/weaverville-alpacas/6930923148.html","https://asheville.craigslist.org/grd/d/weaverville-alpacas/6930923148.html","https://asheville.craigslist.org/grd/d/weaverville-alpacas/6930923148.html","https://asheville.craigslist.org/grd/d/weaverville-alpacas/6930923148.html","https://asheville.craigslist.org/grd/d/weaverville-alpacas/6930923148.html","https://asheville.craigslist.org/grd/d/weaverville-alpacas/6930923148.html"]
cityList = ["Asheville","Asheville","Charlotte","Weaverville","Charlotte","Asheville","Wilmington", "Raleigh", "Asheville","Waynesville"]
#imageList = ["https://asheville.craigslist.org/grd/d/weaverville-alpacas/6930923148.html","https://asheville.craigslist.org/grd/d/weaverville-alpacas/6930923148.html","https://asheville.craigslist.org/grd/d/weaverville-alpacas/6930923148.html","https://asheville.craigslist.org/grd/d/weaverville-alpacas/6930923148.html","https://asheville.craigslist.org/grd/d/weaverville-alpacas/6930923148.html","https://asheville.craigslist.org/grd/d/weaverville-alpacas/6930923148.html","https://asheville.craigslist.org/grd/d/weaverville-alpacas/6930923148.html","https://asheville.craigslist.org/grd/d/weaverville-alpacas/6930923148.html","https://asheville.craigslist.org/grd/d/weaverville-alpacas/6930923148.html","https://asheville.craigslist.org/grd/d/weaverville-alpacas/6930923148.html"]
priceList = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]







root = Tk()
path = "./TestImages/01.jpg"
img = Image.open(path)
print(type(img))
tImg = ImageTk.PhotoImage(img) #converts to a TK image which can be used in any Tk widget
#canvas = Canvas(root, width = 300, height = 300)
#canvas.pack()
#canvas.create_image(20, 20, anchor=NW, image=tImg)

root.mainloop()