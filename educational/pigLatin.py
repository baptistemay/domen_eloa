


def pig_it(text):
    import re
    wordsSearch = re.compile(r"[a-zA-Z]*|!|\?|\.")
    wordsInText = re.findall(wordsSearch, text)
    result = []
    exceptionsChar = [",", "!", ".", "?"]
    for word in wordsInText:
        if len(word) == 0:
            continue
        if word in exceptionsChar:
            result.append(word)
        else:
            buffer = word[0]
            word = (word[1:] + buffer + "ay")
            result.append(word)
    result = " ".join(result)
    result = str(result)
    print(result)
    return result

pig_it(input("Enter the sentence to convert\n    : "))

input("Press ENTERR to quit.")