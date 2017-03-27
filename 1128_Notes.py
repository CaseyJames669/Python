#2
name = "John Smith"
lastName, firstName = name.rsplit(' ')
print(lastName, firstName)
fullName = lastName + " " + firstName
print(fullName)

#3
str1 = "hi"
str2 = "high"
ans = str2.find(str1)
print(ans)

str1 = "gh"
str2 = "high"
ans = str2.find(str1)
print(ans)

str1 = "x"
str2 = "high"
ans = str2.find(str1)
print(ans)

#4
passwd=input("Enter a password:")
if len(passwd) >= 8:
    if passwd.isalnum():
        ct = passwd.count("0"or"1"or"2"or"3"or"4"or"5"or"6"or"7"or"8"or"9")
        if ct == 2:
            print("You have enter a valid password.")    
else:
    print("Invalid Password")
