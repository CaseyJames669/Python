"""
Assignment 9:
Grade Calculations and Redirection of Input
This program takes a students name, their 3 test values, 5 quiz values,
drops the lowest of each, and then tells you what the ending grade is.

Preconditions:
    User must enter one name
    Quizes are values between 0-10
    Tests are values between 0-100
"""
__author__ = 'Casey Bladow'
__date__ = '12/11/12'

def calcTestAvg(testScores):
    """Take the 3 test scores, drop the lowest, and then find the average

    Purpose: sum up the remaining test scores and find the average
    Preconditions: 5 test have been entered but the lowest has been removed
    Postconditions: the average of the remaining 4 scores is testAvg
    """
    total = sum(testScores) 
    testAvg = total/len(testScores)
    return testAvg

def calcQuizAvg(quizScores):
    """Find the average of the quiz scores

    Purpose: sum up the remaining quiz scores and find the average
    Preconditions: 3 quiz have been entered but the lowest has been removed
    Postconditions: the average of the remaining 2 scores is quizAvg
    """
    total = sum(quizScores) 
    quizAvg = total/len(quizScores)
    return quizAvg

def getGrade(score):
    """Use the score of the average quizes and tests and return final grade.

    Purpose: using the score of the quiz and test scores, a letter grade will be initiated
    Preconditions: score is evaluated properly from the testAvg and quizAvg
    Postconditions: a letter; A, B, C, D or F will be returned in the place of the score
    """
    if score >= 90.0:
        return 'A'
    if score >= 80.0:
        return 'B'
    if score >= 70.0:
        return 'C'
    if score >= 60.0:
        return 'D'
    else:
        return 'F'
    
def main():
    numStudents = eval(input("How many students will you be entering data for? "))
    for x in range(0,numStudents):
        data = input("Please enter the students name and scores seperated by comma's: ").title()
        grades = data.split(",")
        grades = [s.strip() for s in grades]
        name = grades[0]
        #testScores list initialized
        testScores = grades[1],grades[2],grades[3]
        testScores = [float(s) for s in testScores]
        #quizScores list initialized
        quizScores = grades[4],grades[5],grades[6],grades[7],grades[8]
        quizScores = [float(s) for s in quizScores]
        #lowest test score dropped
        dropTest = testScores.remove(min(testScores))
        testAvg = (sum(testScores))/len(testScores)
        #lowest quiz score dropped
        dropQuiz = quizScores.remove(min(quizScores))
        quizAvg = (sum(quizScores))/len(quizScores)
        #score is figured out here. The .6 and .4 represent a 60/40% ratio.
        #The quizes are then multiplied by ten to add the additional zero
        #and send out the appropriate value.
        score = (testAvg*.6)+((quizAvg*.4)*10)
        print(name + ": Test Average: ", calcTestAvg(testScores),", Quiz Average: ", calcQuizAvg(quizScores), ", Final Grade: ",getGrade(score),".")

if __name__ == '__main__':
    main()
