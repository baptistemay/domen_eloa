import sys, time

try:
    sys.argv[1] = int(sys.argv[1])
    sys.argv[2] = int(sys.argv[2])
except ValueError:
    print("""
Commands must be numbers.
""")
    time.sleep(4)
    sys.exit()
if len(sys.argv) > 3:
    print("""
The given number of commands is not correct (width, height).
""")
    time.sleep(4)
    sys.exit()

if int(sys.argv[1]) == 0 or int(sys.argv[2]) == 0:
    print("""
Empty result.
""")
    time.sleep(4)
    sys.exit()
givenWidth = int(sys.argv[1])
givenHeigth = int(sys.argv[2])

def drawTriangle(width, height):
    for x in range(height):
        for x in range(width):
            print("#", end="")
        print()

drawTriangle(givenWidth, givenHeigth)

goodbye = input("Press Enter to exit")