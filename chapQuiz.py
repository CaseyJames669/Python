
x = eval(input("Enter a number: "))
x = x ** 3
print(x)
question = input("Would you like to continue?: (Y or N)")
while question != 'N':
    x = eval(input("Enter a number: "))
    x = x ** 3
    print(x)
    question = input("Would you like to continue?: (Y or N)")
