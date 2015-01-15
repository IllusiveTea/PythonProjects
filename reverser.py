import random

string = ""
revered = ""
iterations = 0

def Shuffle( inString ):
    if not inString:
        return None
    firstArray = list(inString)
    output = list()
    while len(firstArray) > 0:
        randy = random.randint(0, len(firstArray)) -1
        output.append(firstArray[randy])
        del firstArray[randy]
    return "".join(output)

def start():
    global iterations
    global string
    global revered
    interations = 0
    string = input("Enter a string, I will try and reverse it >> ")
    revered = string[::-1]
    print("Trying to find {r} from {s}".format(r=revered, s=string))
    displayString = Shuffle(string)

    while not ( displayString == revered ):
        displayString = Shuffle( displayString ) 
        iterations += 1
        print("Done \"{s}\" in {i}".format(s=displayString, i=iterations))
    print("I have reversed the string \"{ORIG}\" to \"{REV}\" in {I} loops!".format(ORIG=string, REV=displayString, I=iterations))

if __name__ == "__main__":
    start()
