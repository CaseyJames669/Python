numList = []
x=0
ct=1
num = eval(input("Please enter a number: "))
while num != -999:
    numList.append(num)
    num = eval(input("Please enter a number: "))
print("Sum: ",sum(numList))
if len(numList) == 0:
    print("")
else: print(numList)
