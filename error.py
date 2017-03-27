x = eval(input("enter a number between 0 and 100"))
low = 0
high = 100
while x < low or x > high : 
    print ("Please re-enter a number in the range 0-100")
    x = eval(input("enter a number between 0 and 100"))
