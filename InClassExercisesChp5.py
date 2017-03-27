#1a
"""
sum = 0
ct = 1
for ct in range(10):
    sum += ct
print ("Sum: ", sum, " Count: ", ct)
"""

#1b
"""
ct = 1
sum =0
while ct < 10:
    sum += ct
    ct += 1
print ("Sum: ", sum, " Count: ", ct)
"""

#1c
"""
num = eval(input("Enter a value (Enter -99 to end): "))
sum = 0
while num != -99:
    sum += num
    num = eval(input("Enter a value (Enter -99 to end): "))
print("The sum is", sum)
"""

#1d
"""
num = 0
continueLoop = 'Y'
sum = 0
while continueLoop == 'Y':
    num = eval(input("Please enter a value: "))
    sum += num
    continueLoop = input("Enter Y to continue or N to quit: ")
print("The sum is", sum)
"""

#2a
"""
ct = 1
while ct < 100:
    print(ct)
    ct += 1 #add this
"""

#2b
"""
ct = 0
while ct > -100: #flip less then sign and change to -100
    print(ct)
    ct -= 1
"""

#2c
"""
ct = 0
while ct < 100:
    print (ct)
    ct += 1 #indented wrong
"""

#2d
"""
score = eval(input("Please enter your test score"))
while (score <=0) or (score >= 100):
    #flipped greater/less then symbols, changed and to or
    print("error -- please enter a score from 0 to 100")
    score = eval(input("Please enter your test score"))
"""

#Exercise 3
"""
negnumbers = 0
posnumbers = 0
total = 0
ct = 0
conLoop = 'C'
while conLoop != 'X':
    num = eval(input("Enter a value: "))
    if num < 0:
        negnumbers += 1
    if num > 0:
        posnumbers += 1
    if num != 0:
        total += num
        ct += 1
    conLoop = input("Enter X to exit or C to continue: ")
print("You entered", posnumbers," positive numbers and ",negnumbers," negative numbers.")
average = total / ct
print("The average of these numbers is ",average)
"""
