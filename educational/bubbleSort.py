

def bubbleSort(numbers):

    for x in range(len(numbers)):
        for y in range(len(numbers)):
            if numbers[x] < numbers[y]:
                numbers[x], numbers[y] = numbers[y], numbers[x]
    

    print(f"""

    Sorted list is : {numbers}
    
    
""")
    return numbers


assert bubbleSort([2, 0, 4, 1, 3]) == [0, 1, 2, 3, 4]

assert bubbleSort([2, 2, 2, 2]) == [2, 2, 2, 2]