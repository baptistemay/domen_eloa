import random


def printHandshakes(persons):
    shakes = []
    startingPoint = 0
    for firstPerson in range(len(persons) - 1):
        startingPoint += 1
        for secondPerson in range(startingPoint, len(persons)):
            if persons[firstPerson] == persons[secondPerson]:
                continue
            else:
                personOrder = random.randint(0, 100)
                if personOrder < 50 :
                    shakes.append(f"{persons[firstPerson]} shakes hands with {persons[secondPerson]}")
                else:
                    shakes.append(f"{persons[secondPerson]} shakes hands with {persons[firstPerson]}")
    for x in range(random.randint(0, 150)):
        random.shuffle(shakes)
    listedShakes = "\n".join(shakes)

    print(listedShakes)
    print(f"""
Total handshakes : {len(shakes)} for {len(personsCount)} persons.
""")
    return len(shakes)

personsCount = ["Zophie", "Camilla", "Pazuzu", "Joachim", "Esther",
"Kayin", "Karl", "Malvina", "Earl", "Jessie", "Max", "Jim", "Gabriel",
"Dupont avec un T", "Dupond avec un D", "Jolyne", "Joseph", "Samantha",
"Ludovic", "La belle soeur", "Le Capitaine Crochet", "Yann", "Jill",
"Rebecca", "Fedor", "Rin, croquette de la lune", "Jesper", "Debian"]
printHandshakes(personsCount)

exitCommand = input(f"""
Press Enter to quit :
""")


"""

assert printHandshakes(['Alice', 'Bob']) == 1

assert printHandshakes(['Alice', 'Bob', 'Carol']) == 3

assert printHandshakes(['Alice', 'Bob', 'Carol', 'David']) == 6

"""