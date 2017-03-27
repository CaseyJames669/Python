"""
Assignment 4: Enter scores, find highest, and average
"""
__author__ = "Casey Bladow"
__date__ = "10/6/12"


import sys
numScores = eval(input("Please enter the number scores you will be entering:"))

if numScores <= 0:
	sys.exit()

total = 0
ct = 0
highscore = 0
lowscore = 100

while ct in range(0,numScores):

    name = input("Please enter the students name: ")
    score = eval(input("Please enter the students score: ")

    if score < 0
        print("Error: Number must be between 0 and 100")
        sys.exit()
if (score > 100):
    print("Error: Number must be between 0 and 100")
    sys.exit()

total += score

if ct == 0:
    lowscore = score
    lowname = name
    highscore = score
    highname = name
	

	# see if score > highscore
if score > highscore:
    highscore = score
    highname = name

	# see if score < lowscore
if score < lowscore
    lowscore = score
    lowname = name
	
ct += 1

print("\t Category \t Score \t Name")
print("\t Highest \t", highscore, "\t ", highname)
print("\t Lowest \t", lowscore, "\t ", lowname)
print("Number of Scores: ", numScores)
average = total / numScores
print("Average of Scores: ", average) 


