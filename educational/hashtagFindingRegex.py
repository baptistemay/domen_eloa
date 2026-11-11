import re, sys, time

def askSentence():
    askForSentence = ""
    askForSentence = input("""
This script will check for all hashtags in the sentence you enter
: 
""")
    def get_hashtags(askForSentence):
        chkHashtags = re.compile(r"#[^\s]*")
        hashtagsFound = chkHashtags.findall(askForSentence)
        print(f"""
Here are the hashtags found :
{hashtagsFound}
""")
        restartGetHashtags = input("""
If you want to quit, press Enter.
Else, enter anything to restart the script.
""")
        if restartGetHashtags:
            askSentence()
            get_hashtags(askForSentence)
            return True
        else:
            print("Goodbye !")
            time.sleep(2)
            sys.exit()
    get_hashtags(askForSentence)
askSentence()