import copy

def rot13(text):
    alphabetWithLowerChars = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    alphabetWithUpperchars = alphabetWithLowerChars.upper()
    rot13Dict = {}

    count = 1
    for char in range(26):
        rot13Dict[alphabetWithLowerChars[- (count)]] = alphabetWithLowerChars[- (count) - 13]
        count += 1
    count = 1
    for char in range(26):
        rot13Dict[alphabetWithUpperchars[- (count)]] = alphabetWithUpperchars[- (count) - 13]
        count += 1
    
    
    count = 0
    textToConvert = list(copy.copy(text))
    for char in textToConvert:
        current = rot13Dict.get(char, char)
        textToConvert[count] = current
        count += 1
    result = "".join(textToConvert)
    result = str(result)
    print(f"""

- - - - - - - - - - - - - - -

Dictionary used for encryption was : {rot13Dict}

Text was : {text}

Text once processed is : {result}

- - - - - - - - - - - - - - -
    
""")

    return result

#'rot13("Test")


assert rot13('Hello, world!') == 'Uryyb, jbeyq!'

assert rot13('Uryyb, jbeyq!') == 'Hello, world!'

assert rot13(rot13('Hello, world!')) == 'Hello, world!'

assert rot13('abcdefghijklmnopqrstuvwxyz') == 'nopqrstuvwxyzabcdefghijklm'

assert rot13('ABCDEFGHIJKLMNOPQRSTUVWXYZ') == 'NOPQRSTUVWXYZABCDEFGHIJKLM'