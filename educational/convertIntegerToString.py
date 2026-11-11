def startScript():
    numberChoice = input("""
This script will mimic the native 'str' function in python.
Please enter the desired integer to process:

""")
    try:
        numberChoice == int(numberChoice)
    except ValueError:
        print("Your input must be an integer.")
        startScript()
        return True
    convertIntToStr(int(numberChoice))

def endOrRestartScript():
    end_restart = input("""
Press ENTER to restart or "q" to quit
:
""")
    if end_restart == "q" or end_restart == "Q":
        import sys, time
        print("Goodbye !")
        time.sleep(4)
        sys.exit()
    elif end_restart == "":
        startScript()
        return True
    else:
        print("Invalid command.")
        endOrRestartScript()
        return True

def convertIntToStr(num):
    #Prevents "" for 0
    if num == 0:  
        return "0"

    #Creates a dictionary with equivalent keys/values
    strList = ["0","1","2","3","4","5","6","7","8","9"]
    CONVERTEDDICT = {}
    count = 0
    for strNumber in strList:
        CONVERTEDDICT[strNumber] = count
        count += 1
    CONVERTEDDICT = {value : key for key, value in CONVERTEDDICT.items()}

    #Appends the last digit in num via iteration
    convertedIntListToStr = []
    count = 0
    numberToConvert = num
    def actualConversion(numberToConvert):
        while True:
            actualNumberProcessed = numberToConvert % 10
            convertedIntListToStr.append(CONVERTEDDICT[actualNumberProcessed])
            numberToConvert = numberToConvert // 10
            if numberToConvert == False:
                break
        convertedIntListToStr.reverse()
        result = "".join(convertedIntListToStr)
        print(f"""
Converted to string : '{result}'
""")
        return result
    actualConversion(numberToConvert)
    endOrRestartScript()
    return True

startScript()






""" VALID
for i in range(-10000, 10000):

    assert convertIntToStr(i) == str(i)
"""