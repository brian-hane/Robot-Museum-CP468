from Tkinter import *

class FileLoadApplication(Frame):
    def createWidgets(self):
        self.lblFileName = Label(self, text="Enter input file name:")
        self.lblFileName.pack()

        self.txtFileName = Entry(self)
        self.txtFileName.insert(0, "input.txt")
        self.txtFileName.pack()

        self.pControls = Frame(self)
        self.pControls.pack(side=BOTTOM)

        self.btnStart = Button(self, text="Start", command=self.start)
        self.btnStart.pack(in_=self.pControls, side=LEFT)

        self.btnQuit = Button(self, text="Quit", command=self.quit)
        self.btnQuit.pack(in_=self.pControls, side=LEFT)

    def start(self):
        window = Toplevel(self)
        window.fileName = self.txtFileName.get()
        MuseumApplication(window)

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

class MuseumApplication(Frame):
    def createWidgets(self):
        self.fileName = self.master.fileName
        self.lblFileName = Label(self, text=self.fileName)
        self.lblFileName.pack()

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

root = Tk()
root.title("CP468 - Museum Path Planning")
app = FileLoadApplication(root)
app.mainloop()
root.destroy()