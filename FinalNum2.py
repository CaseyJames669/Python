ssn = ""
while not ssn:
    ssn = input("Enter your Social Security Number: ")
    ssn = ssn.replace("-", "")
    if len(ssn) != 9: 
        print("This is an invalid number.")
        ssn = ""
print("Your Social Security Number is: " + ssn[0:3],"- "+ssn[3:5],"- "+ssn[5:9])
