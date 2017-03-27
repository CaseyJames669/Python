#Exercise 1
#Runs the entered scored, doubles them, and prints them
"""
def doubleList(someList):
    for ct in range(len(someList)):
        someList[ct] = someList[ct] * 2


#main program
test1Scores=[90,70,40]
doubleList(test1Scores)
print(test1Scores)
"""
#Exercise 2
#does the same as above but also creates a ct so that
#the results print in a running list style instead of one
#right after the other
"""
def doubleList(someList):
    for ct in range(len(someList)):
        someList[ct] = someList[ct] * 2


#main program
test1Scores=[90,70,40]
doubleList(test1Scores)
for ct in range(len(test1Scores)):
    print(test1Scores[ct])
"""
#Exercise 3
#essentially doing the same thing as the above example
#but creating the list and calling the function in
#different manners
"""
def doubleList():
    for ct in range(len(test1Scores)):
        test1Scores[ct] = test1Scores[ct] * 2


#main program
test1Scores=[90,70,40]
doubleList()
for ct in range(len(test1Scores)):
    print(test1Scores[ct])
"""
#Exercise 4
#the doubleList function was never called so it
#just print what it was given
"""
def doubleList():
    tmpList = list()
    for ct in range(len(test1Scores)):
        tmpList.append(test1Scores[ct] * 2)


#main program
test1Scores=[90,70,40]
doubleList()
for ct in range(len(test1Scores)):
    print(test1Scores[ct])
"""
#Exercise 5
#this time the doubleList function was ran and then the
#list was ran through the function and was printed
"""
def doubleList():
    tmpList = list()
    for ct in range(len(test1Scores)):
        tmpList.append(test1Scores[ct] * 2)
    return(tmpList)

#main program
test1Scores=[90,70,40]
test1Scores = doubleList()
for ct in range(len(test1Scores)):
    print(test1Scores[ct])
"""
