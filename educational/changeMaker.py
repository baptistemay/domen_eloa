

def makeChange(amount):

    change = {}

    totalToChange = amount
    print(f"\nGiven amount was : {totalToChange}.")
    print("processing ...")
    while totalToChange > 0:
        if totalToChange >= 25: #quarters
            totalToChange -= 25
            buffer = change.get("quarters", 0)
            buffer += 1
            change["quarters"] = buffer

        elif totalToChange >= 10: #dimes
            totalToChange -= 10
            buffer = change.get("dimes", 0)
            buffer += 1
            change["dimes"] = buffer
            
        elif totalToChange >= 5: #nickels
            totalToChange -= 5
            buffer = change.get("nickels", 0)
            buffer += 1
            change["nickels"] = buffer

        elif totalToChange >= 1: #pennies
            totalToChange -= 1
            buffer = change.get("pennies", 0)
            buffer += 1
            change["pennies"] = buffer
        else :
            break

    print ("Done !")    
    print(f"Needed change is : {change}")
    print("\n - - - - - - - - - - - - -")
    return change

#makeChange()


assert makeChange(30) == {'quarters': 1, 'nickels': 1}

assert makeChange(10) == {'dimes': 1}

assert makeChange(57) == {'quarters': 2, 'nickels': 1, 'pennies': 2}

assert makeChange(100) == {'quarters': 4}

assert makeChange(125) == {'quarters': 5}