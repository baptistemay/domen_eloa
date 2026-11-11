import sys, time

def drawbox(size):
    upperBorder = f"{" " * size}+{"-" * ((size * 2) + 1)}+"
    def upperPattern():
        for x in range(size):
            if x == 0:
                print(upperBorder)
            else:    
                print(f"{" " * (size - x)}/{" " * ((size * 2) + 1)}/{" " * (x - 1)}|")
    middleBorder = f"+{"-" * (size * 2)}+{" " * size}+"
    def lowerPattern():
        for x in range(size):
            if x == 0:
                print(middleBorder)
            else:
                print(f"|{" " * (size * 2)}|{" " * (size - x)}/")
    print("""
    
    
    """)
    upperPattern()
    lowerPattern()
    lowerBorder = (f"+{"-" * (size * 2)}+")
    print(lowerBorder)
    goodbye = input("""
    
    
        Press Enter to quit.
    
""")
    sys.exit()



askSize = sys.argv[1]
try:
    askSize == int(askSize)
except ValueError:
    print("The command sent must be an integer.")
    time.sleep(4)
    sys.exit()
if len(sys.argv) != 2:
    print("You must enter one and only one command.")
    time.sleep(4)
    sys.exit()
else:
    drawbox(int(askSize))
    
