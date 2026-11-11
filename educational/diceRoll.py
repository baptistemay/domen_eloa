import random

def rollDice(numberOfDice):
    sum = 0
    for x in range(numberOfDice):
        randomNumber = random.randint(1,6)
        sum += randomNumber
    if sum == 0:
        print("The dice was not rolled")
        return 0
    else:
        print(f"Sum of the dices is {sum}")
        return sum
        
rollDice(2)

"""
assert rollDice(0) == 0

assert rollDice(1000) != rollDice(1000)

for i in range(1000):

    assert 1 <= rollDice(1) <= 6

    assert 2 <= rollDice(2) <= 12

    assert 3 <= rollDice(3) <= 18

    assert 100 <= rollDice(100) <= 600

    """