def getChessSquareColor(column, row):
    if column >= 8 or row >= 8:
        return ""
    elif column % 2 == row % 2:
        return "white"
    else:
        return "black"


x = input("Enter the coordonate of the column here : ")
y = input("Enter the coordonate of the row here : ")
print(getChessSquareColor(int(x), int(y)))



assert getChessSquareColor(0, 0) == 'white'

assert getChessSquareColor(1, 0) == 'black'

assert getChessSquareColor(0, 1) == 'black'

assert getChessSquareColor(7, 7) == 'white'

assert getChessSquareColor(0, 8) == ''

assert getChessSquareColor(2, 9) == ''
