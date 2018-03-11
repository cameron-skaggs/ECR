#GUI Basics
from tkinter import *
from ECR import Ecr

class Application(Frame):
    def __init__(self, master):
        # initialize the frame
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        # Initiate Labels
        self.labelECR = Label(self, text="ECR")
        self.labelInit = Label(self, text="Initiator")
        self.labelOwner = Label(self, text="Owner")
        self.labelStatus = Label(self, text="Status")
        # variable for option menu
        variable = StringVar(self)
        variable.set("Initializing")
        # Initiate entries
        self.ecr = Entry(self)
        self.init = Entry(self)
        self.owner = Entry(self)
        self.status = OptionMenu(self, variable, "Initializing", "Ownership", "Routing", "CAB Processing")

        #Pushing the "Enter Button will create an ECR
        self.printButton = Button(self, text="Enter ECR", command=lambda:
        self.create_ecr(self.ecr.get(), self.init.get(), self.owner.get(), variable.get()))
        self.quitButton = Button(self, text="Quit", command=self.quit)

        # format the grid
        self.labelECR.grid(row=0, column=0)
        self.ecr.grid(row=0, column=1)
        self.labelInit.grid(row=1, column=0)
        self.init.grid(row=1, column=1)
        self.labelOwner.grid(row=2, column=0, sticky=W)
        self.owner.grid(row=2, column=1)
        self.labelStatus.grid(row=3, column=0)
        self.status.grid(row=3, column=1)
        self.printButton.grid(row=4, column=1)
        self.quitButton.grid(row=5, column=1)

    '''This function is for my own personal 
    benefit to ensure I'm capturing the right data
    will not be used in the final product'''
    def create_ecr(self, nummber, initiator, owner, status):
        ecr = Ecr(nummber,initiator, owner, status)
        self.display = Label(self, text=nummber)
        self.display.grid(row=6, column=1)
        print(nummber)
        print(ecr.get_owner())
        print(initiator)
        print(ecr.get_status)


root = Tk()
root.title("ECR Documentation")
root.geometry("250x170")
app = Application(root)
root.mainloop()
