import sys
rowNumber = int(1)
print("  |    1   2   3   4   5   6   7   8   9  10")
print("--+-----------------------------------------")
for rows in range (1, 11):
    print(f"{rowNumber}| ".rjust(4, " "), end="")
    for columns in range (1, 11):
        print(str(int(columns) * int(rows)).rjust(4, " "), end="")
    print()
    rowNumber += 1
def goodbye():
    quit = input("""
Press Enter to quit : 
""")
    if quit == "":
        sys.exit()
    else:
        goodbye()
        return True
goodbye()
