"""
4.21
Comprehensive: Find anyday of the week by entering day, month, year.
"""
__author__ = "Casey Bladow"
__date__ = "10/25/12"


import math
yr = eval(input("Please enter the year: (Ex: 2012) "))
mth = eval(input("Please enter the month: (Ex: 1-12) "))
if mth == 1:
    mth = 13
    yr =+ 1
if mth == 2:
    mth = 14
    yr =+ 1
dymth = eval(input("Please enter the day of the month: (Ex: 1-31) "))
yr = yr%100
cent = math.floor(yr/100)
dywk = ( dymth + math.floor((26*(mth+1))/10) + yr + math.floor(yr/4) + math.floor(cent/4) + 5 * cent)%7
if dywk == 0:
    print ("Day of the week is Saturday")
elif dywk == 1:
    print ("Day of the week is Sunday")
elif dywk == 2:
    print ("Day of the week is Monday")
elif dywk == 3:
    print ("Day of the week is Tuesday")
elif dywk == 4:
    print ("Day of the week is Wednesday")
elif dywk == 5:
    print ("Day of the week is Thursday")
elif dywk == 6:
    print ("Day of the week is Friday")
    
