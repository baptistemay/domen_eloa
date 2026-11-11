import random, sys
randomList = [10]
def reload():
    choice = input("Press enter if you want to reload or enter something to quit : ")
    if choice == "":
        randomizer()
        median(randomList)
    else:
        sys.exit()

def randomizer():
    global randomList
    randomList.clear()
    for x in range(50):
        number = random.randint(0,5000)
        randomList.append(number)
    print(f"""
Generated numbers are:

{randomList}
""")
    return randomList

randomizer()

def median(numbers):
    numbers.sort()
    lengthOfList = len(numbers)
    if lengthOfList == 0:
        print("List is empty")
        return None
    elif lengthOfList % 2 != 0:
        while lengthOfList > 1:
            del numbers[0]
            del numbers[-1]
            lengthOfList -= 2
        else:
            result = numbers[0]
            print(f"median is {result}")
            reload()

    else:
        while lengthOfList > 2:
            del numbers[0]
            del numbers[-1]
            lengthOfList -= 2
        else:
            result = (numbers[0] + numbers[1]) / 2
            try :
                float(result)
            except:
                int(result)

            print(f"median is {result}")
            print()
            reload()



median(randomList)




"""
assert median([]) == None

assert median([1, 2, 3]) == 2

assert median([3, 7, 10, 4, 1, 9, 6, 5, 2, 8]) == 5.5

assert median([3, 7, 10, 4, 1, 9, 6, 2, 8]) == 6

import random

random.seed(42)

testData = [3, 7, 10, 4, 1, 9, 6, 2, 8]

for i in range(1000):

    random.shuffle(testData)

    assert median(testData) == 6


"""