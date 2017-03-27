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

#Example 2
"""
def doubleIt(myList):
    myList[0] = myList[0] * 2

myList = [4]
doubleIt(myList)
print(myList[0])
"""

#Example 3
"""
def myAverage(num1, num2, num3):
    myAverage = (num1 + num2 + num3) / 3
    return myAverage
print(myAverage(1,2,3,))
"""
#Example 4 ERROR
"""
def myAverage(numItems):
    sum =0
    for ct in range(0,numItems):
        #ask user for a number
        num = eval(input("Enter a number: "))
        sum = sum + num
    ans=sum/numItems
    return myAverage
print(myAverage(ans))
"""

#Example 5
otPay = 0
payRate = eval(input("Enter your pay rate: "))
hoursWorked = eval(input("Enter hours worked: "))
if hoursWorked > 40:
    tmpHrs = hoursWorked - 40
    otPay = tmpHrs * (payRate * 1.5)
grossPay = (hoursWorked * payRate) + otPay
print("You worked",hoursWorked,"at",payRate,"for a gross pay of",grossPay)

