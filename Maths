from tkinter import *

def triNums(mainMenu, maxNum=100):
    numbers = []
    for n in range(1,maxNum):
        tn = n * ((n +1)/2)
        numbers.append(int(tn))
        if (tn > 1000):
            break
    #print (numbers)
    mainMenu.text.set(" ".join(["Triangle Numbers:",str(numbers)]))

def penNums(mainMenu, maxNum=100):
    numbers = []
    for n in range(1,maxNum):
        pn = n * (((3*n) -1)/2)
        numbers.append(int(pn))
        if (pn > 1000):
            break
    #print (numbers)
    mainMenu.text.set(" ".join(["Pentagonal Numbers:",str(numbers)]))

def hexNums(mainMenu, maxNum=100):
    numbers = []
    for n in range(1,maxNum):
        hn = n * ((2*n) -1)
        numbers.append(int(hn))
        if (hn > 1000):
            break
    #print (numbers)
    mainMenu.text.set(" ".join(["Hexagonal Numbers:",str(numbers)]))

def createHelp():
    helpRoot = Tk()
    helpApp = HelpMenu(helpRoot)
    helpRoot.mainloop()

class MainMenu():
    def __init__(self, parent):
        self.parent = parent
        self.triButton = Button(self.parent, text="Triangle Numbers", command=lambda: triNums(self), bg="black", fg="white")
        self.penButton = Button(self.parent, text="Pentagonal Numbers", command=lambda: penNums(self), bg="red", fg="black")
        self.hexButton = Button(self.parent, text="Hexagonal Numbers", command=lambda: hexNums(self))
        self.helpButton = Button(self.parent, text="Help", command=createHelp)
        self.exitButton = Button(self.parent, text="Exit", command=self.destroy)
        self.text = StringVar()
        self.label = Label(self.parent, textvariable=self.text, wraplength=300)
        
        self.triButton.pack()
        self.penButton.pack()
        self.hexButton.pack()
        self.label.pack()
        self.helpButton.pack()
        self.exitButton.pack()
    def destroy(self):
        print("Exiting program")
        self.parent.destroy()   

class HelpMenu():
    def __init__(self, parent):
        self.parent = parent
        self.exitButton = Button(self.parent, text="Done", command=self.destroy)
        self.text = "\r\n".join([
            "Hello and welcome to the number generator",
            "To use, please click the button that corresponds with the sequence of numbers you want generating",
            "The formulea to calculate the Triangle numbers is Tn = n(n+1)/2. The first five are (1, 3, 6, 10 and 15)",
            "The formulea to calculate the Pentagonal numbers is Pn = n(3n-1)/2. The first five are (1, 5, 12, 22 and 35)",
            "The formulea to calculate the Hexagonal numbers is Hn = n(2n-1). The first five are (1, 6, 15, 28 and 45)"])
        self.label = Label(self.parent, text=self.text)
        self.label.pack()
        self.exitButton.pack()
    def destroy(self):
        print("Exiting Help")
        self.parent.destroy()

def main():
    root = Tk()
    root.geometry("300x300")
    app = MainMenu(root)
    root.mainloop()

if __name__ == '__main__':
    main()
