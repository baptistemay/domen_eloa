first_number = int(input("Enter the first number : "))
last_number = int(input("Enter the last number : "))

def fizzBuzz():
    for number in range(first_number, last_number + 1):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz", end= " ")
        elif number % 3 == 0:
            print("Fizz", end = " ")
        elif number % 5 == 0:
            print("Buzz", end = " ")
        else:
            print(number, end = " ")
fizzBuzz()