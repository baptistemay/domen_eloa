def mergeTwoLists(list1, list2):
    result = []
    countList1 = 0
    countList2 = 0
    list1Processed = False
    list2Processed = False

    while countList1 < (len(list1)) and countList2 < (len(list2)):
        
        if list1[countList1] < list2[countList2]:
            result.append(list1[countList1])
            countList1 += 1
        else:
            result.append(list2[countList2])
            countList2 += 1

    if countList1 == (len(list1)):
        list1Processed = True
    else:
        list2Processed = True
    if list1Processed == True:
        result += list2[countList2 : ]
    else:
        result += list1[countList1 : ]
    
    print(f"""
- - - - - - - - - - - - - - -

List were :
{list1}
{list2}

Once merged and sorted, the result is : {result}

""")
    return result

mergeTwoLists(sorted([13,10,4,38,9,6,11,50]),sorted([1,47,2,3,20,5,7,8,]))


assert mergeTwoLists([1, 3, 6], [5, 7, 8, 9]) == [1, 3, 5, 6, 7, 8, 9]

assert mergeTwoLists([1, 2, 3], [4, 5]) == [1, 2, 3, 4, 5]

assert mergeTwoLists([4, 5], [1, 2, 3]) == [1, 2, 3, 4, 5]

assert mergeTwoLists([2, 2, 2], [2, 2, 2]) == [2, 2, 2, 2, 2, 2]

assert mergeTwoLists([1, 2, 3], []) == [1, 2, 3]

assert mergeTwoLists([], [1, 2, 3]) == [1, 2, 3]

