#Exercise 4.9 (Page 122)
#Financial: Compare Costs

wgt1, prc1 = eval(input("Enter weight and price for package 1 (Ex: 50,24.59):"))
wgt2, prc2 = eval(input("Enter weight and price for package 2 (Ex: 25,11.99):"))

total1 = wgt1 / prc1
total2 = wgt2 / prc2

if total1 < total2:
    print("Package 1 is the better deal.")
else:
    print("Package 2 is the better deal.")
