from tkinter import *
from tkinter import ttk
def __init__(self, link_list, image_list, price_list, city_list):
    self.linkList = link_list
    self.imageList = image_list
    self.priceList = price_list
    self.cityList = city_list
root = Tk()

frame = Frame(root)

labelText = StringVar()

label = Label(frame, textvariable = labelText)
button = Button(frame, text = "Click me")

labelText.set("I am a label")

label.pack()
button.pack()
frame.pack()

root.mainloop()