""" This is a solution for the "Comma Formatted Numbers" exercice by Ai Sweigart. ("https://inventwithpython.com/pythongently/exercise33/")
Given I did want to evaluate certain things while coding it, there is no funtion used.
Also, I thought that the occasional non-triplet group was meant to be at the end.
I am no accustomed to this sort of notation; it would have been a problem for
an application, but for the sake of the exercice and what I worked on, I did it that way, and keep it as such.
"""

import random


#Create number
floatNumber = False
randomizer = random.randint(0,10)
number = random.randint(0,(10000000000000000000000000000000000000000000000000000000 // random.randint(1,10)))
if randomizer > 5:
    number = number * ((random.randint(1, 10) * (random.randint(1,10))))
else:
    number * (number % random.randint(1,10))
number = str(number)
if random.randint(1,10) > 5:
    number = list(number)
    number.append(".")
    for x in range(0,random.randint(1,100)):
        random.shuffle(number)
    number = "".join(number)
if number[0] == "." or number[-1] == ".":
    while number[0] == "." or number[-1] == ".":
        random.shuffle(number)
    number = str(number)
numberCopy = number


#Check if float
if "." in number:
    floatNumber = True
    count = int(0)
    for x in number:
        if x == ".":
            break
        else:
            count += 1
    dotNumbers = number[count:int(-1)]
    number = number[0:(count)]


#Check number of "xxx,"
chunks = (len(number) // 3)
rest = (len(number) - (chunks * 3))
rest = -(rest)
if rest != 0:
    lastNumbers = number[rest:]
else:
    lastNumbers = "None"


#Convert the number
startSlice = 0
endSlice = 3
result = []
for x in range(chunks):
    result.append(number[startSlice:endSlice])
    startSlice += 3
    endSlice += 3
if rest != 0:
    result.append(number[(rest):])
result = ",".join(result)
if floatNumber == True:
    result = result + dotNumbers


#Display the number
print(f"""

[Number was : {numberCopy}]
""")
print(f"RESULT is : {result}")
print()
print(f"""
~~~~~~~~~~~~~~
Last number after the last comma was : {lastNumbers}
The 'Rest' value corresponding  was : {rest}
~~~~~~~~~~~~~~
""")


goodbye = input(" --- Press 'Enter' to leave --- ")