#Exercise 4.13 (Page 105)

#Whats wrong with this??
score = eval(input("Please enter your score: "))
if score >= 60.0:
    grade = 'D'
elif score >= 70.0:
    grade = 'C'
elif score >= 80.0:
    grade = 'B'
elif score >= 90.0:
    grade = 'A'
else:
    grade = 'F'

print("Your grade is a/an",grade)

#The indentation is all wrong.
#Below is how it should have been written

score = eval(input("Please enter your score: "))
if score >= 60.0:
    grade = 'D'
    if score >= 70.0:
        grade = 'C'
        if score >= 80.0:
            grade = 'B'
            if score >= 90.0:
                grade = 'A'
else:
    grade = 'F'

print("Your grade is a/an",grade)
