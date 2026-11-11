import sys, time
sentenceChoice = ""
def is_pangram(sentence):
    checklist = "azertyuiopqsdfghjklmwxcvbn"
    chk = True
    for x in checklist:
        if x in sentence:
            chk == True
        else:
            chk = False
            break
    if chk == True:
        print(f"'{sentenceChoice}' is a pangram.")
        print()
        return True
    else:
        print(f"'{sentenceChoice}' is not a pangram.")
        print()
        return False

def _start():
    global sentenceChoice
    sentenceChoice  =input("""
Please enter something to check if this is a pangram.
A pangram is a sentence containing all the letters in the alphabet.
Alternatively, you can enter 'q' to quit.
:
""")
    while True:
        if sentenceChoice == "q" or sentenceChoice == "Q":
            print("Goodbye !")
            time.sleep(3)
            sys.exit()
        else:
            is_pangram(sentenceChoice)
            
        _start()
        return True

_start()




