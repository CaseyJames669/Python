#Example 1
"""
def doubleIt(myNum):
    myNum = myNum*2
    print("Inside the function, myNum is: ", myNum)

num=4
print("In the main, before the function is called, num is: ",num)
doubleIt(num)
print("In the main, after the function call, num is :",num)
"""

#Example 3
"""
def doubleIt(myList):
    myList[0] = myList[0] * 2

myList = [4]
doubleIt(myList)
print(myList[0])
"""

#Example 4
"""
def myAverage(num1, num2, num3):
    myAverage = (num1 + num2 + num3) / 3
    return myAverage
print(myAverage(1,2,3,))
"""
#Example 5 ERROR
def myAverage(numItems):
    sum =0
    for ct in range(0,numItems):
        #ask user for a number
        num = eval(input("Enter a number: "))
        sum = sum + num
    ans=sum/numItems
    return myAverage
print(myAverage(ans))
