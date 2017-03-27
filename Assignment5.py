"""
Assignment 5: Financial application: compare loans with various interest rates
"""
__author__="Casey Bladow"
__date__="10/16/12"

continueLoop = 'Y'


loanAmount = eval(input("Please enter your loan amount: "))
while loanAmount < 0 or loanAmount == 0:
    loanAmount = eval(input("error -- Please a enter a POSITIVE loan amount\n\t that is GREATER then zero: "))
    
loanPeriod = eval(input("Please enter the loan period (in years): "))
while loanPeriod < 0 or loanPeriod == 0:
    loanPeriod = eval(input("error -- Please enter a POSITIVE loan period\n\t that is GREATER then zero (in years): "))
interestRate = 4.875
print("Interest Rate \t Monthly Payment \t Total Payment")
while interestRate < 8.000:
    interestRate = (interestRate + .125)
    monthlyPayment = loanAmount*(interestRate/1200)/(1-1/(1+(interestRate/1200))**(loanPeriod*12))
    totalPayment = monthlyPayment*loanPeriod*12
    print(format((interestRate/100),".3%"),"\t\t",format(monthlyPayment,".2f"),"\t\t",format(totalPayment,".2f"))

continueLoop = input("If you would like to enter a new loan amount and/or loan period\n\t enter Y, otherwise enter X to exit: ")
while continueLoop != 'X':
    loanAmount = eval(input("Please enter your loan amount: "))
    while loanAmount < 0 or loanAmount == 0:
        loanAmount = eval(input("error -- Please a enter a POSITIVE loan amount\n\t that is GREATER then zero: "))
    
    loanPeriod = eval(input("Please enter the loan period (in years): "))
    while loanPeriod < 0 or loanPeriod == 0:
        loanPeriod = eval(input("error -- Please enter a POSITIVE loan period\n\t that is GREATER then zero (in years): "))
    interestRate = 4.875
    print("Interest Rate \t Monthly Payment \t Total Payment")
    while interestRate < 8.000:
        interestRate = (interestRate + .125)
        monthlyPayment = loanAmount*(interestRate/1200)/(1-1/(1+(interestRate/1200))**(loanPeriod*12))
        totalPayment = monthlyPayment*loanPeriod*12
        print(format((interestRate/100),".3%"),"\t\t",format(monthlyPayment,".2f"),"\t\t",format(totalPayment,".2f"))
    continueLoop = input("If you would like to enter a new loan amount and/or loan period\n\t enter Y, otherwise enter X to exit: ")
