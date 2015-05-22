from tkinter import *
import random, time, decimal

#GUI Variables
WIDTH = 400
HEIGHT = 400

root = Tk()

#Might as well let Tkinter automatically adjust GUI size
#root.geometry("{W}x{H}".format(W=WIDTH, H=HEIGHT))

frame = Frame(root)
frame.grid()

operators = { "+" : (lambda x,y: x+y), "-" : (lambda x,y: x-y),
              "/"  :(lambda x,y: x/y), "*" :(lambda x,y: x*y)}
operations = ["+", "-", "/", "*"]

def calcNumber( number1=0, number2=0, operator="+"):
    return operators[operator](number1, number2)

def getAnswer( calcArray ):
    if (len(calcArray)==1): #Reached final number. No need to use reccursion anymore.
        return calcArray[0]
    
    num1 = calcArray[0]
    operator = calcArray[1]
    num2 = calcArray[2]
    
    newNumber = calcNumber(num1, num2, operator)

    print("Just calculated: {n1}{o}{n2}".format(n1=num1, n2=num2, o=operator))
    calcArray.remove(num1)
    calcArray.remove(num2)
    calcArray.remove(operator)
                
    calcArray.insert(0, newNumber)    
    calcArray = getAnswer(calcArray)

def winningAnswer():
    print("Welldone. You got a correct answer!")
def wrongAnswer():
    print("Sorry, that was the wrong answer.. Perhaps you need to brush up on your maths skills?")
    

def createNewQuestion():
    global frame
    frame.destroy()
    frame = Frame(root)

    frame.grid()
    
    print("Forgotten..")
    
    amountOfNumbers = random.randint(2, 10) #Amount of numbers to have e.g (2,2) would equal (number {operator} number2)
    c = 0
    calculateMe = []
    for i in range(amountOfNumbers):
        number = random.randint(1,10) #Get a number
        
        if c == 1: #Time to generate an operator
            c = 0
            operator = operations[random.randint(0,len(operations)-1)]
            calculateMe.append(operator)

        calculateMe.append(number)
        c += 1
    
    myLabel = " ".join(str(x) for x in calculateMe)
    
    Label(frame, text=myLabel).grid()
    
    getAnswer(calculateMe) #Modifies array and only leaves answer
    answer = calculateMe[0]
    rand_num_1 = decimal.Decimal(random.randrange(0,1000))/10
    rand_num_2 = decimal.Decimal(random.randrange(0,1000))/100
    
    answerButton = Button(frame, text=str(answer), command=lambda:[winningAnswer(), createNewQuestion()])
    redHerin1 = Button(frame, text=str(rand_num_1),command=wrongAnswer)
    redHerin2 = Button(frame, text=str(rand_num_2),command=wrongAnswer)

    
    packOrder = random.randint(1,3)
    if packOrder == 1:
        answerButton.grid(row=1)
        redHerin1.grid(row=2)
        redHerin2.grid(row=3)
    elif packOrder == 2:
        redHerin1.grid(row=1)
        answerButton.grid(row=2)
        redHerin2.grid(row=3)
    else:
        redHerin1.grid(row=1)
        redHerin2.grid(row=2)
        answerButton.grid(row=3)
    Button(frame, text="Quit", command=lambda:root.destroy()).grid(row=4)
    
    
def main():
    Button(frame, text="Start", command=createNewQuestion).grid(row=1)
    Button(frame, text="Quit", command=lambda:root.destroy()).grid(row=2)
    
    root.mainloop()
    

if __name__ == "__main__":
    main()
