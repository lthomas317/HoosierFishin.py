from os import system
system('pip install Pillow')
from tkinter import *
import os
from PIL import Image

root = Tk()
root.geometry("500x750")
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
                  Indiana and any nearby states.
                  Click "Restart" to reset the program.""", bg = "sky blue")
  myLabel.pack()

myButton = Button(root, text = "About this app", command = myClick, fg = "black", bg = "white")
myButton.pack()

def myClick():
  myLabel = Label(root, text = """
                  A few of the best fishing
                  spots in Indiana are
                  Patoka Lake,
                  White River,
                  St. Joseph River,
                  Morse Reservoir, and
                  Sundance Lake. """, bg = "sky blue")
  myLabel.pack()

myButton = Button(root, text = "Indiana", command = myClick, fg = "black", bg = "white")
myButton.pack()

def myClick():
  myLabel = Label(root, text = """
                  A few of the best fishing
                  spots in Illinois are
                  the Mississippi River,
                  Lake Michigan,
                  Heidecke Lake,
                  Lake Springfield, and
                  Evergreen lake.
                  """, bg = "sky blue")
  myLabel.pack()

myButton = Button(root, text = "Illinois", command = myClick,     fg = "black", bg = "white")
myButton.pack()

def myClick():
  myLabel = Label(root, text = """
                  A few of the best fishing
                  spots in Michigan are
                  Manistee River,
                  Grand River,
                  Saginaw Bay,
                  Lake Erie, and of course,
                  Lake Michigan. """, bg = "sky blue")
  myLabel.pack()

myButton = Button(root, text = "Michigan", command = myClick,     fg = "black", bg = "white")
myButton.pack()

def myClick():
  myLabel = Label(root, text = """
                  A few of the best fishing
                  spots in Ohio are
                  Lake Erie,
                  Ohio River,
                  Seneca Lake,
                  Hoover Reservoir, and
                  Alum Creek. """, bg = "sky blue")
  myLabel.pack()

myButton = Button(root, text = "Ohio", command = myClick,     fg = "black", bg = "white")
myButton.pack()

def myClick():
  myLabel = Label(root, text = """
                  A few of the best fishing
                  spots in Kentucky are
                  Taylorsville Lake,
                  Lake Cumberland,
                  Nolin River Lake,
                  Ohio River, and
                  Rough River Lake. """, bg = "sky blue")
  myLabel.pack()

myButton = Button(root, text = "Kentucky", command = myClick,     fg = "black", bg = "white")
myButton.pack()

def restart_program():
  python = sys.executable
  os.execl(python, python, * sys.argv)

myButton = Button(root, text = "Restart", command = restart_program, fg = "black", bg = "white")
myButton.pack()
root.mainloop()
