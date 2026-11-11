import re
with open("madLibs.txt", "w", encoding = "utf-8") as file_creation:
    file_creation.write("Creation of a host file")
def _search_and_replace():
#1 - TODO Search for ADJECTIVE, NOUN, ADVERB, VERB in a text file
    target = input(f"""
    Please enter the name of the target.txt file : """)
    try:
        target = str(target)
    except ValueError:
        print("You must enter text.")
        _search_and_replace()
        return True

    search_ADJECTIVE = re.compile("ADJECTIVE", target)
    search_NOUN = re.compile("NOUN", target)
    search_ADVERB = re.compile("ADVERB", target)
    search_VERB = re.compile("VERB", target)

#2 - TODO Ask the user to replace thoses terms
    if search_ADJECTIVE == True:
        target_ADJECTIVE = input("Enter a word/sentence to replace 'ADJECTIVE' : ")
    if search_ADVERB == True:
        target_ADVERB = input("Enter a word/sentence to replace 'ADVERB' : ")
    if search_NOUN == True:
        target_NOUN = input("Enter a word/sentence to replace 'NOUN' : ")
    if search_VERB == True:
        target_VERB = input("Enter a word/sentence to replace 'VERB' : ")


#3 - TODO Create a new file with the results
    with open(target, "r", encoding = "utf-8") as reader:
        original_text = reader.read()

    with open("madLibs.txt", "w", encoding = "utf-8") as target_FILE :
        target_FILE.write(original_text)

    if search_ADJECTIVE == True:
        re.sub("ADJECTIVE", target_ADJECTIVE, madLibs.txt)
    if search_ADVERB == True:
        re.sub("ADVERB", target_ADVERB, madLibs.txt)
    if search_NOUN == True:
        re.sub("NOUN", target_NOUN, madLibs.txt)
    if search_VERB == True:
        re.sub("VERB", target_VERB, madLibs.txt)
    

#4 - TODO Print the result
    with open("madLibs.txt", "r", encoding = "utf-8") as result:
        result.read()