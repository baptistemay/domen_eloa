def reverseString(text):
    originaltext = []
    for char in text:
        originaltext.append(char)
    result = originaltext
    result.reverse()
    result = "".join(result)
    
    print(result)
    return result

reverseString("Hello ! How are you ?")


assert reverseString('Hello') == 'olleH'

assert reverseString('') == ''

assert reverseString('aaazzz') == 'zzzaaa'

assert reverseString('xxxx') == 'xxxx'