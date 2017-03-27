import random
def rollTheDice():
        die1 = random.randrange(1,7)
        die2 = random.randrange(1,7)
        sum = die1 + die2
        print("Player rolled", die1, "+", die2, "=", sum)
        return sum
       
val = rollTheDice()

def printResults():
    if val == 7 or val == 11:
            gameStatus = "WON"
    elif val == 2 or val == 3 or val == 12:
            gameStatus = "LOST"
    else:
            gameStatus = "CONTINUE"
            myPoint = val
            print("Point is", myPoint)
           
    while gameStatus == "CONTINUE":
            sum = rollTheDice()
            if sum == myPoint:
                    gameStatus = "WON"
            elif sum == 7:
                    gameStatus = "LOST"
    if gameStatus == "WON":
            print("Player wins")
    else:
            print("Player loses")

def main():
    printResults()
    con = input("Would you like to continue? \n'X' to continue, ANYTHING ELSE TO EXIT")
    while con != 'X':
        main()
main()
