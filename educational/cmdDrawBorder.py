import sys, time

def drawBorder(width, height):
    widthAdjusted = int(width - 2)
    heightAdjusted = int(height - 2)
    print("+" + ("-" * widthAdjusted) + "+")
    for columns in range(heightAdjusted):
        print("|" + (" " * widthAdjusted) + "|")
    print("+" + ("-" * (width - 2)) + "+")
    print("Press Enter to close")
    input()
    sys.exit

def goodbye():
    time.sleep(4)
    sys.exit()
givenWidth = sys.argv[1]
givenHeight = sys.argv[2]
try:
    givenHeight = int(givenHeight)
    givenWidth = int(givenWidth)
except ValueError:
    print("Commands must be integers.")
    goodbye()
if len(sys.argv) != 3:
    print("You must enter two and only two commands.")
    goodbye()
if givenHeight < 2 or givenWidth < 2:
    print("Commands must be number > 2.")
    goodbye()
drawBorder(givenWidth, givenHeight)