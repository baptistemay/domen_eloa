
import time, sys
Ties = int(0)
P1Wins = int(0)
P2Wins = int(0)
playBot = True
boValue =
def _tie():
    global Ties
    Ties += int(1)
    print("Tie !")
    return "Tie"
def p1won():
    global P1Wins
    P1Wins += int(1)
    print("P1 won !")
    return "Player one wins"

def p2won():
    global P2Wins
    P2Wins += int(1)
    print("P2 won !")
    return "Player two wins"

def rpsWinner(player1, player2):
    if player1 == player2:
        _tie()
    if player1 == "rock" and player2 == "scissors":
        p1won()
    elif player1 == "rock" and player2 == "paper":
        p2won()
    if player1 == "paper" and player2 == "rock":
        p1won()
    elif player1 == "paper" and player2 == "scissors":
        p2won()
    if player1 == "scissors" and player2 == "paper":
        p1won()
    elif player1 == "scissors" and player2 == "rock":
        p2won()
def play():
    play1 = input("Player one move : ")
    if play1 != "rock" and play1 != "paper" and play1 != "scissors":
        print("Invalid command.")
        play()
        return True
    play2 = input("Player two move : ")
    if play2 != "rock" and play2 != "paper" and play2 != "scissors":
        print("Invalid command.")
        play()
        return True 
    rpsWinner(play1, play2)
    #result = print(val := rpsWinner(play1, play2))
    replay()
    
def replay():
    choice = input("Replay ? (y/n)")
    if choice == "y" or choice == "Y":
        play()
        return True
    elif choice == "n" or choice == "N":
        print("Goodbye !")
        time.sleep(3)
        sys.exit()
    else:
        print("Invalid command.")
        replay()
        return True
def _rules():
    global playBot
    global boValue
    bo9 = int()
    print(f"""
Welcome to "Rock, Paper, Scissors !
By default, the game is set to be played with a bot on the same PC with a total 9.
You can select multiple game modes from here :
- Play with a seonc player : Enter "nobot" if desired : """)
    playBot = input(":   ")
    print(f"""
- 'Best of x' : Change the number of total rounds by entering the desired number.
   If you want the default value, just press 'Enter'
:   """)
    bestOf = input(":")
    if playBot == "nobot" or playBot == "no bot":
        playBot = False
    boValue = bestOf
    


play()



