import sys

def isLeapYear(year):
    entry = int(year)
    
    if entry % 400 == 0:
        print("True")
        return True
    elif entry % 100 == 0 and entry % 400 != 0:
        print("False")
        return False
    elif entry % 4 != 0:
        print("False")
        return False
    else:
        print("True")
        return True

test =input("year : ")

def reset():
    askReset=input("Reset ? (y/n) : ")
    if askReset == "y" or askReset == "Y":
        test =input("year : ")
        isLeapYear(test)
        return True
    else:
        sys.exit()

isLeapYear(test)
while True:
    reset()


assert isLeapYear(1999) == False

assert isLeapYear(2000) == True

assert isLeapYear(2001) == False

assert isLeapYear(2004) == True

assert isLeapYear(2100) == False

assert isLeapYear(2400) == True
