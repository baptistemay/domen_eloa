
def getCostOfCoffee(numberOfCoffees, pricePerCoffee):
    total = 0
    totalNumberOfCoffees = numberOfCoffees
    while numberOfCoffees >= 9:
        numberOfCoffees -= 9
        total += (pricePerCoffee * 8)
    total += (numberOfCoffees * pricePerCoffee)
    if total == 2.50:
        print(f"Total price is {float(total)}$ for {totalNumberOfCoffees} cup of coffee.")

    if total == int(total):
        print(f"Total price is {int(total)}$ for {totalNumberOfCoffees} cups of coffee.")
        return total
    else:
        print(f"Total price is {float(total)}$ for {totalNumberOfCoffees} cups of coffee")      
        return total
import random
randomNumber = random.randint(0,1000)
getCostOfCoffee(randomNumber, 2.50)


"""

assert getCostOfCoffee(7, 2.50) == 17.50

assert getCostOfCoffee(8, 2.50) == 20

assert getCostOfCoffee(9, 2.50) == 20

assert getCostOfCoffee(10, 2.50) == 22.50

 

for i in range(1, 4):

    assert getCostOfCoffee(0, i) == 0

    assert getCostOfCoffee(8, i) == 8 * i

    assert getCostOfCoffee(9, i) == 8 * i

    assert getCostOfCoffee(18, i) == 16 * i

    assert getCostOfCoffee(19, i) == 17 * i

    assert getCostOfCoffee(30, i) == 27 * i

"""