sal = eval(input("Please enter your salary: "))
yrs = eval(input("How long did you work there? "))
newsal = 0
if yrs > 5:
    newsal = ((sal * .02) + sal)
else:
    newsal = ((sal * .01) + sal)
print("Original Salary: $", format(sal,".2")
print("Years worked: ", yrs)
print("New salary: $", format(newsal,".2")
