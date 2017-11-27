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
        label = tk.Label(textvariable=self.var, justify = "center")
        label.pack(anchor="nw")

    # Function to over-ride main label
    def textArea(self, value= "Select option from menu"):
        self.stringVariable.set(value)

    def MainWindow(self):
        # Tittle
        self.parent.title("Privacy Enhancing Application")
        self.pack()

        # Menu
        menuBar = tk.Menu(self.parent)
        self.parent.config(menu=menuBar)

        # Sub-Menu
        file = tk.Menu(menuBar, tearoff=0)
        file.add_command(label="Open", command=None)
        file.add_command(label="Modify", command=None)
        file.add_command(label="Save", command=None)
        file.insert_separator(4)
        file.add_command(label="Exit", command=self.quit)
        menuBar.add_cascade(label="File", menu=file)

        # Sub-Menu
        help = tk.Menu(self.parent, tearoff=0)
        menuBar.add_cascade(label="Help", menu=help)



root = tk.Tk()
root.geometry("600x500")
app = Hospital(root)
root.mainloop()
