import random

#Assumes the list will have 2 items
def rollDi(someList):
    someList[0]=random.randint(1,6)
    someList[1]=random.randint(1,6)

#main program
roll1 = 0
roll2 = 0
myRoll=[roll1,roll2]
rollDi(myRoll)
roll1=myRoll[0]
roll2=myRoll[1]
print(roll1,roll2)
