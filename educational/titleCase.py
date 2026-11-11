import re 
def getTitleCase(text):
    #Creation of the dictionary and lists
    lowerChars = "azertyuiopqsdfghjklmwxcvbn"
    upperChars = "AZERTYUIOPQSDFGHJKLMWXCVBN"

    dictOfConversion = {}
    inversedDictOfConversion = {v: k for k, v in dictOfConversion.items()}



    count = 0
    for char in lowerChars:
        dictOfConversion[char] = upperChars[count]
        count += 1

    #Creation of the regex pattern, capture the words in text
    checkText = re.compile("[a-zA-Z,!]*")
    processedText = checkText.findall(text)


    #Process the words found
    
    result = []

    for word in processedText:
        count = 1
        if word != "":
            titleLetter = word[0]
        if titleLetter in lowerChars:
            word = word.replace(titleLetter, dictOfConversion.get(titleLetter), 1)
        for char in word:
            if char is word[0]:
                continue
            elif char in upperChars:
                word = word.replace(word[count], inversedDictOfConversion.get(char), 1)
                count += 1
        result.append(word)
    finalResult =" ".join(result)
    print(finalResult)
    return finalResult


getTitleCase("HELLO")
getTitleCase("hello")


assert getTitleCase('Hello, world!') == 'Hello, World!'

assert getTitleCase('HELLO') == 'Hello'

assert getTitleCase('hello') == 'Hello'

assert getTitleCase('hElLo') == 'Hello'

assert getTitleCase('') == ''

assert getTitleCase('abc123xyz') == 'Abc123Xyz'

assert getTitleCase('cat dog RAT') == 'Cat Dog Rat'

assert getTitleCase('cat,dog,RAT') == 'Cat,Dog,Rat'

 

import random

random.seed(42)

chars = list('abcdefghijklmnopqrstuvwxyz1234567890 ,.')

for i in range(1000):

    random.shuffle(chars)

    assert getTitleCase(''.join(chars)) == ''.join(chars).title()
    