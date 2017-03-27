"""
Application to simulate playing a game of craps.
A roll of 7 or 11 results in a win.
A roll of 2, 3, or 12 results in a loss.
Any other roll (called a point) results in a win
if the subsequent tosses ultimately match the point
or a loss if a subsequent toss is a 7.
"""
__author__ = "Rhonda Ficek"
__date__ = "11/20/2013"
import random
def rollTheDice(listTossResults):
    """ Generate 2 random integers in the range 1-6
    Purpose:
    Simulate tossing 2 dice by using a random number generator
    Preconditions:
    listTossResults is an existing list that is initially empty
    Postconditions:
    listTossResults will be populated with 2 integers,
    each of which are in the range 1-6, including both endpoints.
    """
    num1 = random.randint(1,6)
    num2 = random.randint(1,6)
    listTossResults.append(num1)
    listTossResults.append(num2)
if __name__ =='__main__':
    tossResults = list()
    rollTheDice(tossResults)
    print(tossResults[0], tossResults[1])
