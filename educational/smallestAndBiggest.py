
numbersList = [1, 2, 23232, 3]

def getSmallest(numbers):
    if numbers == []:
        print("No entry in the list.")
        return None
    else:
        result = numbers[0]
        for x in range(len(numbers)):
            if numbers[x] < result:
                result = numbers[x]
        print(f"Smallest numbers is {result}.")
        return result

def getBiggest(numbers):
    if numbers == []:
        print("No entry in the list.")
        return None
    else:
        result = numbers[0]
        for x in range(len(numbers)):
            if numbers[x] > result:
                result = numbers[x]
        print(f"Biggest numbers is {result}.")
        return result
getSmallest(numbersList)
getBiggest(numbersList)

assert getSmallest([1, 2, 3]) == 1

assert getSmallest([3, 2, 1]) == 1

assert getSmallest([28, 25, 42, 2, 28]) == 2

assert getSmallest([1]) == 1

assert getSmallest([]) == None
