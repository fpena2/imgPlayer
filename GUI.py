# Requires tkinter installed in Python3
import tkinter as tk
from tempMatch import RUN

class userInterface(tk.Frame):
    def __init__(self, parent = None):
        tk.Frame.__init__(self, parent)

        # Variables
        self.parent = parent
        self.stringVariable = tk.StringVar()

        # Functions
        self.MainWindow()

        # Main Screen Label
        label = tk.Label(textvariable=self.stringVariable, justify = "center")
        label.pack(anchor="nw")

    # Function to over-ride main label
    def textArea(self, value= "Select option from menu"):
        self.stringVariable.set(value)

    def MainWindow(self):
        # Title
        self.parent.title("Privacy Enhancing Application")
        self.pack()

        # Menu
        menuBar = tk.Menu(self.parent)
        self.parent.config(menu=menuBar)

        # Sub-Menu
        file = tk.Menu(menuBar, tearoff=0)
        file.add_command(label="Open", command=self.openWindow)
        file.add_command(label="Save", command=None)
        file.insert_separator(3)
        file.add_command(label="Exit", command=self.quit)
        menuBar.add_cascade(label="File", menu=file)

        # Sub-Menu
        help = tk.Menu(self.parent, tearoff=0)
        menuBar.add_cascade(label="Help", menu=help)


    def openWindow(self):
        self.window1 = tk.Toplevel(self.parent)
        self.window1.title("Private Information")
        self.window1.geometry("250x150")

        # Private Data
        self.label_find = tk.Label(self.window1,text="Enter private data to secure")
        self.label_find.pack(anchor="center")
        self.privateData = tk.Entry(self.window1, bd=5,width= 25)
        self.privateData.pack(anchor="center")

        # File
        self.label_find2 = tk.Label(self.window1,text="Enter document name")
        self.label_find2.pack(anchor="center")
        self.fileName = tk.Entry(self.window1, bd=5,width= 25)
        self.fileName.pack(anchor="center")

        # Enter button
        self.enterbutton = tk.Button(self.window1, text = "Enter", command = self.sendData )#button command needs to be added
        self.enterbutton.pack(anchor="center")


    def sendData(self):
        privateDataString = self.privateData.get()
        documentFilename = self.fileName.get()
        RUN(privateDataString, documentFilename)


root = tk.Tk()
root.geometry("400x300")
app = userInterface(root)
root.mainloop()
