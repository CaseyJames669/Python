"""
Assignment 4: Enter scores, find highest, and average
"""
__author__="Casey Bladow"
__date__="10/6/12"

import sys
numScores = eval(input("Please enter the number of scores you will be entering:"))

while numScores <= 0:
    numScores = eval(input("Please enter a number greater than zero, \n\tOr enter 0 (zero) to exit the program: "))
    if numScores == 0:
        sys.exit()

total = 0
ct = 0
highscore = 0
lowscore = 0

while ct < numScores:
        name = input("Please enter the students name: ")
        score = eval(input("Please enter the students score: "))
        while score < 0 or score > 100:
            score = eval(input("Please enter a score between 0 and 100: "))
        total += score
        ct += 1
        if ct == 1:
            lowscore = score
            lowname = name
            highscore = score
            highname = name
            secondhighscore = score
            secondhighname = name
        if score > secondhighscore:
            secondhighscore = highscore
            secondhighname = highname
            if score > highscore:
                highscore = score
                highname = name
        if score < lowscore:
            lowscore = score
            lowname = name

print("Test Scores")
print("\t Category \t\t Score \t\t\t Name")
print("\t Highest \t\t", highscore, "\t\t\t ", highname)
print("\t 2nd Highest \t\t", secondhighscore, "\t\t\t ", secondhighname)
print("\t Lowest \t\t", lowscore, "\t\t\t ", lowname)
print("Number of Scores: ", numScores)
average = total / numScores
average /= 100
print("Average of Scores: "+ format(average,"10.1%")) 
