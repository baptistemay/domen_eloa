
def writeToFile(filename, text):
    with open(filename, "w") as file:
        file.write(text)
        print("Registered.")

def appendToFile(filename, text):
    with open(filename, "a") as file:
        file.write(text)
        print("Registered.")        

def readFromFile(filename):
    with open(filename, "r") as file:
        result = file.read()
        print(result)

def _manager():
    _command = input("""
    Enter '/w' if you want to create a new file.
    Enter '/a' if you want to append an existing file.
    Enter '/r' if you want to read an existing file.
     :   """)
    if _command == "/w":
        _newfile = input("Enter a name for the new file : ")
        _newfile_text = input("Enter your text : ")
        writeToFile(_newfile, _newfile_text)
    elif _command == "/a":
        _appendfile = input("Enter the name of the file you want to append : ")
        _appendfile_text = input("Enter the text you want to add : ")
        appendToFile(_appendfile, _appendfile_text)
    elif _command == "/r":
        _readfile = input("Enter the file name's you want to read : ")
        readFromFile(_readfile)
    else:
        print("Error")


_manager()


