"""
Assignment 7: Craps the computer game
rolls two dice and depending what you roll
decides whether you win or not...
"""
#Win/Loss counter not functioning properly.
#Handing in this version in case i get stuck at work all night...
__author__="Casey Bladow"
__date__="11/14/12"

def rollTheDice(diList):
    #1st dice roll between 1 and 6
    diList[0]=random.randint(1,6)
    diList[1]=random.randint(1,6)

def sumTheDice(di1,di2):
    #adds the dice together and gives you the sum(total)
    total = di1 + di2
    return total

def printResult(total,di1,di2):
    wins=[]
    loss=[]
    #preconditions: your sum will be 2 <= i <= 12
    total = sumTheDice(di1,di2)
    #IF A 2,3 OR 12 ARE ROLLED
    if total == 2 or total == 3 or total == 12:
        print("You rolled",di1,"+",di2,"=",total)
        print("You lose")
        #COUNTER HERE
        loss.append(1)
        return loss
            
    #IF A 7 OR 11 ROLLED
    elif total == 7 or total == 11:
        print("\nYou rolled",di1,"+",di2,"=",total)
        print("You Win")
        #COUNTER HERE
        wins.append(1)
        return wins
            
    #WHEN ANYTHING ELSE IS ROLLED
    else:
        print("\nYou rolled",di1,"+",di2,"=",total)
        #Assigns the total value to point
        point = total
        ct = 0
        while True:
            #Will only print the point value ONCE
            if ct == 0:
                print("Point is", point)
                ct =+ 1
            #Rolls two new random dice between 1 and 6
            #assigns the values d3 and d4
            di3=random.randint(1,6)
            di4=random.randint(1,6)
            #finds the total of the new dice, calling the sumTheDice function
            total = sumTheDice(di3,di4)
            print("\nThis time you rolled",di3,"+",di4,"=",total)
            if total == 7:
                print("You Lose")
                #COUNTER HERE
                loss.append(1)
                return loss
                break
            if total == point:
                print("You Win")
                #COUNTER HERE
                wins.append(1)
                return wins
                break
    
#main program junk
import random
total = 0
point = 0
win=0
loss=0
wins=[]
loss=[]

#Assign di1 and di2 to random numbers from rollTheDice(diList)
#it works. DO NOT TOUCH
roll1 = 0
roll2 = 0
myRoll=[roll1,roll2]
rollTheDice(myRoll)
di1=myRoll[0]
di2=myRoll[1]

def printFinal(xwin,xloss):
    print("Total Wins:",xwin,", Total Losses:",xloss)
  
def main():
    xwin=0
    xloss=0
    results=[xwin,xloss]
    #Roll for the 1st time
    rollTheDice(myRoll)
    #find the first sum
    total = sumTheDice(di1,di2)
    #run through the if,elif and else
    printResult(total,di1,di2)
    #ask to continue
    con = input("\nDo you want to continue? \n 'X' to exit, anything else to continue...")
    #while continueing and rolling again
    while con != 'X':
        #new roll, new total, new results
        di3=random.randint(1,6)
        di4=random.randint(1,6)
        total = sumTheDice(di3,di4)
        printResult(total, di3, di4)
        #ask if they want to continue again
        con = input("\nDo you want to continue? \n 'X' to exit, anything else to continue...")
    #COUNTERS NOT WORKING!!!
    print("\nTotal Wins:",wins,", Total Losses:",loss)
    

main()
