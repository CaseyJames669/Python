#prompt for input
N = eval(input(
    "Enter a number between 0 and 1000: "))

#Extract values
A=N%10   #Pulls A
N=N//10  #Removes digit

B=N%10 
N=N//10

C=N%10   #Removing C is not needed

#Adding digits
total = A + B + C

#Display
print("The sum of the digits is ", total)
