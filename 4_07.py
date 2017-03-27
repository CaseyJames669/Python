#Exercise 4.11 (Page 104)

x, y = eval(input("Please enter two numbers (Ex:1,2): "))
if x > 2:
    if y > 2:
        z= x+y
        print("z is",z)
    else:
        print("x is",x)
        
#when the input is 3,2 you'll get "x is 3" as your output
#when the input is 3,4 you'll get "z is 7" as your output
#when the input is 2,2 you wont get any output at all and the program ends
