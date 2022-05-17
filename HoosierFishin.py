from os import system
system('pip install Pillow')
from tkinter import *
import os
from PIL import Image

root = Tk()
root.geometry("550x800")
root.configure(bg = "sky blue")
root.title("Welcome to Hoosier Fishin'!")

im = Image.open("crappie.png")
print(im.size, im.width, im.height)
print(im.format, im.info)
print(im.mode)

for i in range(10):
  im.show()

im.save("crappie.png")

def myClick():
  myLabel = Label(root, text = """
                   This application shows some
                  of the best fishing areas in
                  Indiana and its bordering states.
                  It also lists some of the most popular
                  fish to catch for each location.
                  
                  When you are finished reading, click "Restart" to clear the text.""", bg = "sky blue")
  myLabel.pack()

myButton = Button(root, text = "About this app", command = myClick, fg = "black", bg = "white")
myButton.pack()

def myClick():
  myLabel = Label(root, text = """
                  Best fishing spots in Indiana:
                  
                  Patoka Lake (Largemouth Bass, Channel Catfish, Flathead Catfish)
                  
                  White River (Bluegill, Largemouth Bass, Flathead Catfish)
                  
                  St. Joseph River (Smallmouth and Largemouth Bass, Walleye)
                  
                  Morse Reservoir (Largemouth Bass, Channel Catfish, Striped Bass)
                  
                  Sundance Lake (Bluegill, Redear, Channel Catfish) """, bg = "sky blue")
  myLabel.pack()

myButton = Button(root, text = "Indiana", command = myClick, fg = "black", bg = "white")
myButton.pack()

def myClick():
  myLabel = Label(root, text = """
                  Best fishing spots in Illinois:
                  
                  Mississippi River (Crappie, Walleye, Sauger)
                  
                  Lake Michigan (Lake Trout, Rainbow Trout, Brown Trout)
                  
                  Heidecke Lake (Muskellunge, Smallmouth Bass, Walleye)
                  
                  Lake Springfield (Channel Catfish, Largemouth Bass, Freshwater Drum)
                  
                  Evergreen Lake (Largemouth Bass, Muskellunge, Saugeye)""", bg = "sky blue")
  myLabel.pack()

myButton = Button(root, text = "Illinois", command = myClick,     fg = "black", bg = "white")
myButton.pack()

def myClick():
  myLabel = Label(root, text = """
                  Best fishing spots in Michigan:
                  
                  Manistee River (Steelhead, Salmon, Trout)
                  
                  Grand River (Steelhead, Smallmouth Bass, Northern Pike)
                  
                  Saginaw Bay (Best for Walleye)
                  
                  Lake Erie (Sheepshead, Rock Bass, Pink Salmon)
                  
                  Lake Michigan (Coho Salmon, Pink Salmon, Lake Whitefish) """, bg = "sky blue")
  myLabel.pack()

myButton = Button(root, text = "Michigan", command = myClick,     fg = "black", bg = "white")
myButton.pack()

def myClick():
  myLabel = Label(root, text = """
                  Best fishing spots in Ohio:
                  
                  Lake Erie (Steelhead, Walleye, Yellow Perch)
                  
                  Ohio River (Largemouth Bass, Smallmouth Bass, Sauger)
                  
                  Seneca Lake (Bluegill, Bullhead Catfish, Channel Catfish)
                  
                  Hoover Reservoir (Blue Catfish, Walleye, Saugeye)
                  
                  Alum Creek (Largemouth Bass, Smallmouth Bass, Channel Catfish) """, bg = "sky blue")
  myLabel.pack()

myButton = Button(root, text = "Ohio", command = myClick,     fg = "black", bg = "white")
myButton.pack()

def myClick():
  myLabel = Label(root, text = """
                  Best fishing spots in Kentucky:
                  
                  Taylorsville Lake (Crappie, White Bass, Hybrid Stripers)
                  
                  Lake Cumberland (Crappie, Walleye, Bream)
                  
                  Nolin River Lake (Largemouth Bass, Crappie, Walleye)
                  
                  Ohio River (Largemouth Bass, Sauger, Walleye)
                  
                  Rough River Lake (Black Bass, Hybrid Striped Bass, Gizzard Shad) """, bg = "sky blue")
  myLabel.pack()

myButton = Button(root, text = "Kentucky", command = myClick,     fg = "black", bg = "white")
myButton.pack()

def restart_program():
  python = sys.executable
  os.execl(python, python, * sys.argv)

myButton = Button(root, text = "Restart", command = restart_program, fg = "black", bg = "white")
myButton.pack()
root.mainloop()
