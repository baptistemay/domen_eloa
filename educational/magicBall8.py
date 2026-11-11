

wizard = [
"Certainly.",
"You should doubt about that.",
"No.",
"Not in a foreseeable future.",
"Surely in time.",
"Not in the way you think.",
"Sort of.",
"I see that clearly.",
"It's the opposite.",
"Yes.",
"Quit that thought.",
"Only in dreams.",
"It will not be as much as you would want to.",
"You will.",
"You already know that.",
"In a sense, nobody can.",
"Somebody you know will.",
"Forget that.",
]
import sys
import random
def _ask():
    _ask_me = input("Ask me any question written as 'Will I / Should I . . .', stranger (Or 'y' to quit). : ")
    if _ask_me == "y" or _ask_me == "Y":
        print("Goodbye !")
        sys.exit()
    if "fuck" in _ask_me or "Fuck" in _ask_me:
        print("Here is the only future I see : Fuck you.")
        sys.exit()
    elif "Will" not in _ask_me and "will" not in _ask_me and "Should" not in _ask_me and "should" not in _ask_me:
        print("Learn to respect a rule, moron.")
        _ask()
    else:
        fate = random.randint(0, (len(wizard) - 1))
        print(wizard[fate])
        close = str.lower(input("Enter 'y' to quit or \
press Enter if you wish to continue : "))
        if close == 'y':
            print("Farewell, stranger.")
            sys.exit
        elif "?" in close:
            print("Ask your questions when you're invited to do so, please.")
            _ask()
        elif int(len(close)) > 7:
            print("I didn't ask to hear about your life. Next time just enter 'y' \
if you want to ask me something else or leave.")
            _ask()
        elif close != "y" or close != "Y" and len(close) > 5:
            print("'y' to quit or just Enter to continue. Nevermind.")
            _ask()
        else:
            _ask()

_ask()