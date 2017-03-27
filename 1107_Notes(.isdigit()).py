def calcAvg(a,b,c):
    lowest = min(a,b,c)
    avg = (a+b+c-(lowest))/2
    return avg

a = input("Please enter a number: ")
b = input("Please enter a number: ")
c = input("Please enter a number: ")

if a.isdigit() and b.isdigit() and c.isdigit(): #ALL 3 MUST be True to continue
    a=eval(a)      #Now that you know they are all digits you
    b=eval(b)      #you can eval the int(s) in the str to
    c=eval(c)      #to digits
    calcAvg(a,b,c)
    ans = calcAvg(a,b,c)
    print(ans)
else:
    print("ERROR")
