from tkinter import *
import random
import time

WIDTH = 250
HEIGHT = 250
apple = 0
speed = 3
delta_x = speed
delta_y = 0
count = 0
scoretext = 0
deadtext = 0
playAgainWindow = 0
 
direction = "R" #sets direction to stop snake reversing on its self
snake = 0

root = Tk()

w = Canvas(root, width=WIDTH, height=HEIGHT)
w.pack()

running = False

snakeBits = []

class SnakeBit:
    def __init__(self, x, y, width, height, following, canvas, ID):
        self.x = x
        self.y = y
        self.WIDTH = width
        self.HEIGHT = height
        self.following = following
        self.canvas = canvas
        self.canKill = (ID >= 5)
        self.name = "_".join(["part", str(ID)])
        canvas.create_oval(x, y, x+width, y+height, tag=self.name, fill="blue")

        
    def upate_pos_to_following(self):
        newX = self.canvas.coords( self.following )[0]
        newY = self.canvas.coords( self.following )[1]
        canvas = self.canvas
        name = self.name
        canvas.coords(name, newX, newY,
                      newX+ self.WIDTH, newY + self.HEIGHT)

def drawApple(x, y):
    global apple
    apple = w.create_rectangle(x, y, x+10, y+10, fill="green", tag="apple")
    
def eatApple():
    global count
    global snakeBits

    for i in range(0, 4):
        following = "snake"

        if (len(snakeBits) !=0):
            following = "_".join(["part", str(len(snakeBits)-1)])
        
        temp_snake = SnakeBit(-20, -20,
                              8, 8, following, w, len(snakeBits)) # Spawn the snake bit off of the screen to make sure it doesn;t instantly kill player

        snakeBits.append(temp_snake)
    
    w.delete(apple)
    x = random.randint(10, WIDTH-20)
    y = random.randint(10, HEIGHT-20)
    drawApple(x, y)
    count = count + 1
    points = " ".join(["Points", str(count)])
    w.delete("POINTS")
    w.create_text(35, 10, text=points, tag="POINTS")

def eatLeApple(event):
    eatApple()
    

def drawSnake():
    global snake
    snake = w.create_oval(12, 12, 20, 20, fill="black", tag="snake")

def moveRight(event):
    global direction
    if (direction == "L"):
        return
    global delta_x
    global delta_y
    delta_x = speed
    delta_y = 0
    direction = "R"
    pass

def moveLeft(event):
    global direction
    if (direction == "R"):
        return
    global delta_x
    global delta_y
    delta_x = -speed
    delta_y = 0
    direction = "L"
    pass

def moveUp(event):
    global direction
    if (direction == "D"):
        return
    global delta_x
    global delta_y
    delta_x = 0
    delta_y = -speed
    direction = "U"
    pass

def moveDown(event):
    global direction
    if (direction == "U"):
        return
    global delta_x
    global delta_y
    delta_x = 0
    delta_y = speed
    direction = "D"
    pass

def killSnake():
    w.delete(apple)
    w.delete(snake)
    global deadtext
    global scoretext
    global playAgainWindow
    deadtext = w.create_text(WIDTH/2, HEIGHT/2, text="YOU LOST! Your score is...")
    scoretext = w.create_text(WIDTH/2, (HEIGHT/2)+50, text=count)
    playAgain = Button(w, text="Play Again?", command=start)
    playAgainWindow = w.create_window(10, 10, anchor=NW, window=playAgain)


root.bind('<Right>', moveRight)
root.bind('<Left>', moveLeft)
root.bind('<Up>', moveUp)
root.bind('<Down>', moveDown)


def loopMovement():
    global running
    while running:

        currX1 = w.coords("snake")[0]
        currY1 = w.coords("snake")[1]
        currX2 = w.coords("snake")[2]
        currY2 = w.coords("snake")[3]

        #APPLE COORDS
        appleX1 = w.coords(apple)[0]
        appleX2 = w.coords(apple)[1]
        appleY1 = w.coords(apple)[2]
        appleY2 = w.coords(apple)[3]

        
        for i in range( len(snakeBits), 0, -1 ):
            if (not running):
                return
            snakeBits[i -1].upate_pos_to_following()
            nameOfSnakeBit = snakeBits[i -1].name
            co = w.coords(nameOfSnakeBit)
            for o in w.find_overlapping( co[0], co[1],
                                         co[2], co[3]):
                if (o == snake and snakeBits[i -1].canKill):
                    killSnake()
                    running = False
            

        if (currX1 >= WIDTH or currX1 <= 0 or currX2 >= WIDTH or currX2 <= 0):
            killSnake()
            break

        if (currY1 >= HEIGHT or currY1 <= 0 or currY2 >= HEIGHT or currY2 <= 0):
            killSnake()
            break

        objects = w.find_overlapping(currX1, currY1, currX2, currY2)
        for obj in objects:
            if (obj == apple):
                eatApple()
        
        new_x = delta_x
        new_y = delta_y

        w.move(snake, new_x, new_y)

        w.update()
        
        time.sleep(0.025)
        

def start():
    global direction
    global running
    running = True
    direction = "R"
    global count
    global speed
    speed = 3
    count = 0
    global apple
    global snake
    global scoretext
    global playAgainWindow
    global deadtext
    global snakeBits
    snakeBits = []
    
    w.delete(ALL)
    
    x = random.randint(10, WIDTH-20)
    y = random.randint(10, HEIGHT-20)
    drawApple(x, y)
    drawSnake()
    moveRight(None)
    loopMovement()
    root.mainloop()

def closeHandler():
    global running
    running = False
    root.destroy()

root.protocol("WM_DELETE_WINDOW", closeHandler)

start()
