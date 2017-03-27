def rollTheDice(diList):
    diList[0]=random.randint(1,6)
    diList[1]=random.randint(1,6)

def sumTheDice(di1,di2):
    total = di1 + di2
    return total

def printResult(total,di1,di2):
    #preconditions: your sum will be 2 <= i <= 12
    total = sumTheDice(di1,di2)
    #IF A 2,3 OR 12 ARE ROLLED
    if total == 2 or total == 3 or total == 12:
        print("You rolled",di1,"+",di2,"=",total)
        print("You lose")
        totalLosses =+ 1
        ans = input("\nEnter 'X' to roll again or Anything else to exit:")
        if ans == 'X':
            print("Your Win/Loss ratio is: ", totalWins,"Wins and",totalLosses,"Losses")
            printFinal()
        else:    
            rollagain()
            
    #IF A 7 OR 11 ROLLED
    elif total == 7 or total == 11:
        print("\nYou rolled",di1,"+",di2,"=",total)
        print("You Win")
        totalWins =+ 1
        ans = input("\nEnter 'X' to roll again or Anything else to exit:")
        if ans == 'X':
            print("Your Win/Loss ratio is: ", totalWins,"Wins and",totalLosses,"Losses")
            printFinal()
        else:    
            rollagain()
            
    #WHEN ANYTHING ELSE IS ROLLED
    else:
        print("\nYou rolled",di1,"+",di2,"=",total)
        rollTheDice(myRoll)
        point = total
        ct = 0
        while True:
            #Will only print the point value ONCE
            if ct == 0:
                print("Point is", point)
                ct =+ 1
            di3=random.randint(1,6)
            di4=random.randint(1,6)
            total = sumTheDice(di3,di4)
            print("\nThis time you rolled",di3,"+",di4,"=",total)
            if total == 7:
                print("You Lose")
                totalLosses =+ 1
                ans = input("\nEnter 'X' to roll again or Anything else to exit:")
                if ans == 'X':
                    print("Your Win/Loss ratio is: ", totalWins,"Wins and",totalLosses,"Losses")
                    printFinal()
                    break
                else:    
                    rollagain()
                    break
            if total == point:
                print("You Win")
                totalWins =+ 1
                ans = input("\nEnter 'X' to roll again or Anything else to exit:")
                if ans == 'X':
                    print("Your Win/Loss ratio is: ", totalWins,"Wins and",totalLosses,"Losses")
                    printFinal()
                    break
                else:    
                    rollagain()
                    break
            

def rollagain():
    di3=random.randint(1,6)
    di4=random.randint(1,6)
    total = sumTheDice(di3,di4)
    printResult(total, di3, di4)
    ans = input("\nEnter 'X' to roll again or Anything else to exit:")
    if ans == 'X':
        printFinal()
    else:    
        rollagain()

def printFinal():
    print("Thanks for using this application.")
    data = input("Please hit ENTER to exit program.")
    
#main program junk
import random
import sys
total = 0
totalWins = 0
totalLosses = 0
point = 0

#Assign di1 and di2 to random numbers from rollTheDice(diList)
roll1 = 0
roll2 = 0
myRoll=[roll1,roll2]
rollTheDice(myRoll)
di1=myRoll[0]
di2=myRoll[1]

def main():
    rollTheDice(myRoll)
    printResult(total,di1,di2)

main()
