# Requires tkinter installed in Python3
import tkinter as tk

class userInterface(tk.Frame):

    def __init__(self, parent=None):
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

    def files(self):
        self.window1 = tk.Toplevel(self.parent)
        self.window1.geometry("300x150")
       
        self.label_find = tk.Label(self.window1,text="Enter specific word here")
        self.label_find.pack(anchor="center")
        self.entry1 = tk.Entry(self.window1, bd=5,width= 25)
        self.entry1.pack(anchor="center")

        self.label_find2 = tk.Label(self.window1,text="Enter JPEG file name here")
        self.label_find2.pack(anchor="center")
        self.entry2 = tk.Entry(self.window1, bd=5,width= 25)
        self.entry2.pack(anchor="center")

        #def enterCommand():
            #takes the entered values for the jpeg and string
            #runs them through XML file
        

        self.enterbutton = tk.Button(self.window1,text = "Enter")#button command needs to be added
        self.enterbutton.pack(anchor="center")

    def MainWindow(self):
        # Title
        self.parent.title("Privacy Enhancing Application")
        self.pack()

        # Menu
        menuBar = tk.Menu(self.parent)
        self.parent.config(menu=menuBar)

        # Sub-Menu
        file = tk.Menu(menuBar, tearoff=0)
        file.add_command(label="Open", command=self.files)
        #file.add_command(label="Modify", command=None)
        file.add_command(label="Save", command=None)
        file.insert_separator(4)
        file.add_command(label="Exit", command=self.quit)
        menuBar.add_cascade(label="File", menu=file)

        # Sub-Menu
        help = tk.Menu(self.parent, tearoff=0)
        menuBar.add_cascade(label="Help", menu=help)

    



root = tk.Tk()
root.geometry("600x500")
app = userInterface(root)
root.mainloop()
