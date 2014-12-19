from tkinter import *
import random
import time

'''
How do i spell 'threw' as in 'I threw it into his face'?
Like that *takes a min to write threw*
'''

root = Tk()
HEIGHT = 400
WIDTH = 400

score = 0

triesLeft = 25

canvas = Canvas(root, height=HEIGHT, width=WIDTH)
running = True


canvas.pack()

class Util:
    def __init__(self):
        self.file = open("words.txt", "r")
        self.words = self.file.readlines()
        self.file.close()

util = Util()

word = util.words[random.randint(0, len(util.words))-1]
word_bits = list(word.replace("\n", ""))
temp_aray = []

found_chars = {}


def loop():
    while running:
        canvas.update()

def drawInitialShit():
    canvas.delete(ALL)
    amountOfLines = len(word_bits)
    tags = []
    for x in range(0, amountOfLines):
        TAG = "_".join([word_bits[x], str(x)])
        tags.append(TAG)
        #print (TAG)

    x = 10
    for string in tags:
        x = x + 20
        canvas.create_rectangle( x, HEIGHT - 40, x + 20, HEIGHT - 20, fill="black", tag=string, outline="blue")
        


def start():
    global word
    global word_bits
    global found_words
    global temp_array
    global found_chars

    global triesLeft
    triesLeft = 25
    
    found_chars = {}
    word = util.words[random.randint(0, len(util.words))]
    word_bits = list(word.replace("\n", ""))
    temp_array = word_bits
    found_words = {}
    drawInitialShit()
    loop()
    root.mainloop()

def keyHandler(event):
    global triesLeft
    global score
    
    charPressed = event.char.lower()
    if charPressed in word_bits:
        for i in range (len(word_bits)):
            if (word_bits[i] == charPressed):
                found_chars[i] = charPressed
                TAG = "_".join([charPressed, str(i)])
                #print ("tag=", TAG)
                canvas.create_text(canvas.coords( TAG )[0] + 6, canvas.coords( TAG )[1]+7,
                                    text=charPressed, fill="white")
        
        
        s = "".join(found_chars.values())
        #print ("{S} is found, {w} is original. Do they equal? {b}".format(S=s, w=word, b=(s==word)))
        if s.replace("\n","") == word.replace("\n",""):
            print ("Congratz, you found the word {w}".format(w=word))
            score = score + 1
            start()
        
    else:
        print("Sorry, char '{CHAR}' is not in the word {WORD}".format(CHAR=charPressed, WORD=""))
        triesLeft = triesLeft - 1
        print ("You have {t1}/{t2} tries left!".format(t1=triesLeft, t2=25))
        if triesLeft <= 0:
            print("Oh no, you loose!!")
            score = score -1
            start()

root.bind("<Key>", keyHandler)

def closeHandler():
    global running
    running = False
    canvas.destroy()
    root.destroy()

root.protocol("WM_DELETE_WINDOW", closeHandler)
    

start()
