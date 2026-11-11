

def average(numbers):
    if len(numbers) == 0:
        return None
    else:
        result = 0
        for number in numbers:
            result += number
    average = (result / len(numbers))
    print(f"The average value of the entry is {average} : ")
    return average

assert average([1, 2, 3]) == 2

assert average([1, 2, 3, 1, 2, 3, 1, 2, 3]) == 2

assert average([12, 20, 37]) == 23

assert average([0, 0, 0, 0, 0]) == 0

import random

random.seed(42)

testData = [1, 2, 3, 1, 2, 3, 1, 2, 3]

for i in range(1000):

    random.shuffle(testData)

    assert average(testData) == 2