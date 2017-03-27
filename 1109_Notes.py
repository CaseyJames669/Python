def rollTheDice(di1,di2):
    import random
    di1 = random.randint(1,7)
    di2 = random.randint(1,7)
    return a,b
rollTheDice(a,b)
print(a,b)

def sumTheDice(di1,di2):
    sum = di1 + di2

def printResult(sum,di1,di2):
    preconditions: your sum will be 2 <= i <= 12
    sum = di1 + di2
    if sum == 2 or sum == 3 or sum == 12:
        print("You rolled",di1,"+",di2,"=",(sum))
        print("You lose")
        totalLosses += 1
    elif sum == 7 or sum == 11:
        print("You win")
        totalWins += 1
    else:
        ##############print("undecided -- under construction")
        point <-- sum
        print what they originally rolled
        rollTheDice(sum,di1,di2)
        while True:
            rollTheDice(sum,di1,di2)
            print what they rolled this time
            total = sumTheDice(di1,di2)
            if total == 7:
                totalLosses += 1
                print"You lose"
                break
            if total = point:
                totalWins += 1
                print "You Win"
                break
        
#main program
initialize totalWins, totalLosses
while loop - user wants to continue
    roll the dice
    calculate the total
    print result
    ask the user to continue
    ans = eval(input("Do you to continue? Y or N"))
    if ans != 'Y':

print total wins/losses
