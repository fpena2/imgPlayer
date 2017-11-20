#gui parameters: names for folders
from tkinter import *
import tkinter.messagebox



top = Tk()
top.title("Information Scrambler")
top.geometry("500x250")

myFrame = Frame(top)
myFrame.grid()


def Message1():
    tkinter.messagebox.showinfo("Important Message","Enter folder name")

def Message2():
    tkinter.messagebox.showinfo("Important Message","Enter a number")

def Message2():
    tkinter.messagebox.showinfo("Important Message","Enter a number")


#-----------Folder Section--------------------
label = Label(myFrame,text="Folder Finder")
label.grid(row=0,column=0)

button1 = Button(myFrame, text="?", command=Message1)
button1.place(x=0,y=0)

button2 = Button(myFrame, text="?", command=Message2)
button2.grid(row=5,column=1)

entry1 = Entry(myFrame, bd=2)
entry1.grid(row=1,column=0)


entry2 = Entry(myFrame, bd=2)
entry2.grid(row=2,column=0)


entry3 = Entry(myFrame, bd=2)
entry3.grid(row=3,column=0)

entry4 = Entry(myFrame, bd=2)
entry4.grid(row=4,column=0)

entry5 = Entry(myFrame, bd=2)
entry5.grid(row=5,column=0)
#--------------------------------------------

#--------------Image Section-----------------







top.mainloop() 











'''
lbls = []
btns = []
etys = []


label = Label(myFrame, text="Folders")
lbls.append(label)
#label.pack(side=TOP)
lbls[0].pack()
for i in range(3):
    etys.append(Entry(myFrame, bd=5))
    etys[-1].pack(side=TOP)
#etys.append(entry)


#entry.pack(side=TOP)
    
#etys[1].pack(side=BOTTOM)

btn=Button(etys[-1],text="!",command = Message)
btn.pack(side=RIGHT)

#label2 = Label(top,text = "Image")
#label2.pack(side=RIGHT)
'''
