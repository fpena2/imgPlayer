import webbrowser # Open webpages in browser
import tkinter as tk
from imgDetection import RUN
from tkinter import messagebox


class userInterface(tk.Frame):
    def __init__(self, parent=None):
        tk.Frame.__init__(self, parent)

        # Variables
        self.parent = parent
        self.stringVariable = tk.StringVar()

        # Functions
        self.MainWindow()

        # Main Screen Label
        label = tk.Label(textvariable=self.stringVariable, justify="center")
        label.pack(anchor="nw")

    # Function to over-ride main label
    def textArea(self, value="Select option from menu"):
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
        file.insert_separator(2)
        file.add_command(label="Exit", command=self.quit)
        menuBar.add_cascade(label="File", menu=file)

        # Sub-Menu
        help = tk.Menu(self.parent, tearoff=0)
        help.add_command(label="Github", command=self.openGit)
        help.add_command(label="Documentation", command=self.openDoc)
        help.add_command(label="Version", command=self.showVersion)
        menuBar.add_cascade(label="Help", menu=help)

    def openGit(self):
        webbrowser.open_new("https://github.com/fpena2/imgPlayer")

    def openDoc(self):
        webbrowser.open_new("https://github.com/fpena2/imgPlayer/blob/master/README.md")

    def showVersion(self):
        messagebox.showinfo("About","Version 0.1 Alpha - 11/27/2017")

    # Toplevel windows created when the Open option is seleted from the menu
    def openWindow(self):
        self.window1 = tk.Toplevel(self.parent)
        self.window1.title("Private Information")
        self.window1.geometry("250x150")
        self.window1.resizable(0,0)

        # Private Data
        self.label_find = tk.Label(
        self.window1, text="Enter private data to secure")
        self.label_find.pack(anchor="center")
        self.privateData = tk.Entry(self.window1, bd=5, width=25)
        self.privateData.pack(anchor="center")

        # File
        self.label_find2 = tk.Label(self.window1, text="Enter document name")
        self.label_find2.pack(anchor="center")
        self.fileName = tk.Entry(self.window1, bd=5, width=25)
        self.fileName.pack(anchor="center")

        # Enter button
        # button command needs to be added
        self.enterbutton = tk.Button(
        self.window1, text="Enter", command=self.sendData)
        self.enterbutton.pack(anchor="center")

    # Sends data passed by the user to processing functions
    def sendData(self):
        privateDataString = self.privateData.get()
        documentFilename = self.fileName.get()
        RUN(privateDataString, documentFilename)


root = tk.Tk()
root.geometry("442x278")
img = tk.PhotoImage(file="./resources/logo.png")
panel = tk.Label(root, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")
root.resizable(0,0)
app = userInterface(root)
root.mainloop()
