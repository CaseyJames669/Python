"""
3.9
Financial application: payroll
"""
__author__ = "Casey Bladow"
__date__ = "9/13/12"

name = input("Please enter your name: ")
hours = eval(input("Please enter the number of hours you worked this week: "))
payrate = eval(input("Please enter your hourly wage: "))
fedtax = eval(input("Please enter the current federal tax withholding rate: "))
statax = eval(input("Please enter the current state tax withholding rate: "))

print("Employee Name: ", name)
print("Hours worked: ", round(hours, 2))
print("Pay Rate: $", round(payrate, 2))

grosspay = payrate * hours

print("Gross Pay: $", round(grosspay,2))

fedwith = fedtax * grosspay
stawith = statax * grosspay
totalde = fedwith + stawith

print("Deductions: \n"
      "\t Federal Withholding (", fedtax * 100, "%): $", round(fedwith, 2), '\n',
      "\t State Withholding (" , statax * 100, "%): $", round(stawith, 2), '\n',
      "\t Total Deductions: $", round(totalde, 2))
netpay = grosspay - totalde
print("Net Pay: $", round(netpay, 2))

if hours > 40:
    othrs = hours - 40
    otwage = othrs * (payrate * 1.5)
    print("Overtime Hours: ", othrs)
    print("Overtime Pay: ", otwage)
