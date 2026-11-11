import random
dico = {}
listOfNumbers = []
def refreshNumbers():
    global listOfNumbers
    for x in range(100000):
        number = random.randint(0,100)
        listOfNumbers.append(number)
def refreshDict():
    dico.clear()

refreshDict()
refreshNumbers()

def mode(numbers):
    global dico
    if len(numbers) == 0:
        print("This list is empty")
        return None
    else:
        for x in numbers:
            if x not in dico:
                dico[x] = 1
            else:
                dico[x] += 1
        print(f"List was {numbers}")
        sorted_dico = dict(sorted(dico.items(),
        key = lambda item: item[1], reverse = True))
        print(f"Processed : {sorted_dico}")
        mode = list(sorted_dico)
        mode = mode[0]
        print(f"The mode of this list is {mode}")
        return mode


mode(listOfNumbers)


"""

assert mode([]) == None
refreshDict()
refreshNumbers()

assert mode([1, 2, 3, 4, 4]) == 4
refreshDict()
refreshNumbers()

assert mode([1, 1, 2, 3, 4]) == 1
refreshDict()
refreshNumbers()


import random

random.seed(42)

testData = [1, 2, 3, 4, 4]

for i in range(1000):

    random.shuffle(testData)

    assert mode(testData) == 4

"""