import sys, time

pSymbol = "#"
def drawPyramid(height):
    currentLine = 1
    blankSpaces = (height - (currentLine * 2) + 1)
    for x in range(height):
        print((" " * (blankSpaces)) + (pSymbol * ((currentLine * 2) - 1)) + (" " * (blankSpaces)))
        currentLine += 1
        blankSpaces -= 1
    exitingTheProgram = input("Press Enter to quit :")
    goodbye()


def goodbye():
    time.sleep(4)
    sys.exit()
try:
    sys.argv[1] = int(sys.argv[1])
except:
    print("Command passed must be an integer.")
    goodbye()
if len(sys.argv) == 2:
    givenHeight = sys.argv[1]
    drawPyramid(givenHeight)
elif len(sys.argv) != 2:
    print("You must enter one and only one command.")
    goodbye()
else:
    print("Sorry, an error occured.")
    goodbye()