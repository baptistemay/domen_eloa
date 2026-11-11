

def getUppercase(text):
    charsLower = "azertyuiopqsdfghjklmwxcvbn"
    charsUpper = "AZERTYUIOPQSDFGHJKLMWXCVBN"


    dictOfConvert = {}
    count = 0
    for x in range(len(charsLower)):
        dictOfConvert[charsLower[count]] = charsUpper[count]
        count += 1
    

    count = 0
    result = []
    for checkedCharacter in str(text):
        if checkedCharacter in charsLower:
            checkedCharacter = dictOfConvert.get(checkedCharacter)
            result.append(checkedCharacter)
        else:
            result.append(checkedCharacter)
        count += 1
    result = "".join(result)
    print(result)
    return result

getUppercase("done")

assert getUppercase('Hello') == 'HELLO'

assert getUppercase('hello') == 'HELLO'

assert getUppercase('HELLO') == 'HELLO'

assert getUppercase('Hello, world!') == 'HELLO, WORLD!'

assert getUppercase('goodbye 123!') == 'GOODBYE 123!'

assert getUppercase('12345') == '12345'

assert getUppercase('') == ''