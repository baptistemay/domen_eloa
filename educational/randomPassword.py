import random, sys, time

ALL_LOWER = "azertyuiopqsdfghjklmwxcvbn"
ALL_UPPER = "AZERTYUIOPQSDFGHJKLMWXCVBN"
ALL_NUMBER = "1234567890"
ALL_SPECIAL = "~!@#$%^&*()_+."
ALL_CHAR = ALL_LOWER + ALL_UPPER + ALL_NUMBER + ALL_SPECIAL
passLength = int(0)
def askLength():
    global passLength
    passLength = input("""
This script will generate a random password.
Please enter its desired length :
""")
    if passLength.isdecimal() == False :
        print(f"{passLength} is not a correct entry. Please retry with a number")
        askLength()
        return True
    if int(passLength) > 1000:
        print("Length is too big. Please select a lesser number than 1000.")
        askLength()
        return True
def generatePassword(length = passLength):
    length = int(length)
    if length < 12:
        length = 12
    generatedPassword = []
    generatedPassword.append(ALL_LOWER[random.randint(0, int(len(ALL_LOWER) - 1))])
    generatedPassword.append(ALL_UPPER[random.randint(0, int(len(ALL_UPPER) - 1))])
    generatedPassword.append(ALL_NUMBER[random.randint(0, int(len(ALL_NUMBER) - 1))])
    generatedPassword.append(ALL_SPECIAL[random.randint(0, int(len(ALL_SPECIAL) - 1))])
    for x in range(length - 5):
        generatedPassword.append(ALL_CHAR[random.randint(0, int(len(ALL_CHAR) - 1))])
    for x in range(random.randint(0,100)):
        random.shuffle(generatedPassword)
    generatedPassword = "".join((generatedPassword))
    print(f"""
Password generated is {generatedPassword}  
""")
    return generatedPassword
def reset():
    askReset = input("Do you want to reset ? (y/n) :\n")
    if askReset == "y" or askReset == "Y" :
        generatePassword(passLength)
    elif askReset == "n" or askReset == "N":
        print("Goodbye !")
        time.sleep(3.0)
        sys.exit()
    else:
        print(f"Invalid command entered : {askReset}")
        reset()
        return True

askLength()
generatePassword(passLength)
while True:
    reset()


    
