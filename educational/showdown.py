import random
import sys
def _tc():
    true_damage = random.randint(1,100)
    if true_damage <= 10:
        true_damage = None
    elif true_damage <= 35:
        true_damage = 1
    else:
        true_damage = 0
    return true_damage


def restart():
    print("ENTER 'Y' for REVENGE")
    revenge = input("")
    if revenge == "y" or revenge == "Y":
        print("!!! REVENGE !!!")
        player1.health = 20
        player2.health = 17
        _combat()
    elif revenge == "TOUTMANGE2" or revenge == "toutmange2":
        revenge == "TOUTMANGE2"
        print("""    Here comes the legend ...
        
        Fucking ...
        
            TOUTMANGE2 !!!    
            """)
        player1.health = 20
        player1.attack = 4
        player2.health = 17

    elif revenge == "PROUTIERE" or revenge == "proutiere":
        print(""" ... prout ...
             prout ...
                     prout ?""")
        player1.health = 20
        player2.attack = 5
        player2.health = 17

    else:
        sys.exit()
        

class player:
    def __init__(self, pseudo, health, attack):
     self.pseudo = pseudo
     self.health = health
     self.attack = attack

    def get_pseudo(self):
        return self.pseudo
    
    def get_health(self):
        return self.health

    def get_attack(self):
        tc = _tc()
        if tc == 1:
            return self.attack * 2
        elif tc == None:
            return self.attack * 0
        else:
            return self.attack

    def damage(self, damage):
        self.health -= damage
        print(f'{self.pseudo} took {damage} damage ! Health at {self.health} !')
        if self.health <= 0:
            print(f"{self.pseudo} died . . .")
            restart()


player1 = player("Eloa", 20, 3)
print(f"Bienvenue à {player1.get_pseudo()}")
player2 = player("Migi", 17, 4)
print(f"Bienvenue à {player2.get_pseudo()}")
print(f"""Attributs :
Player 1 - {vars(player1)}
Player 2 - {vars(player2)}""")

begin = input("Press 'ENTER' to begin :")
print("FIGHT")
def _combat():
    turns = random.randint(1,101)
    while True:
        if turns < 50:
            player1.damage(player2.get_attack())
            blow = input("Press ENTER to attack !")
            if blow == True:
                _combat()
            else:
                _combat()
        else:
            player2.damage(player1.get_attack())
            blow = input("Press ENTER to attack !")
            if blow == True:
                _combat()
            else:
                _combat()

_combat()