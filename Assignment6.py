"""
Assignment 6: Help menu for a menu-driven application
that maintains a list of employees - Part 1
Using functions def main(), showMenu(), etc...
"""
__author__="Casey Bladow"
__date__="10/31/12"

#The menu itself
def showMenu():
    print("Employee Maintence")
    print("1) Add a New Employee")
    print("2) Print Employee Roster")
    print("3) Delete an Employee")
    print("4) Sort Employee Roster by Last Name")
    print("5) Exit")
    choice = eval(input("Enter your choice (1-5): "))
    return choice

#What happens when 1 is chosen
def addEmployee():
    print("Adds an employee to the roster.\n")

#What happens when 2 is chosen
def printEmployeeList():
    print("Prints employee roster.\n")

#What happens when 3 is chosen
def deleteEmployee():
    print("Removes an employee from the roster.\n")

#What happens when 4 is chosen
def sortEmployeeList():
    print("Sorts employee roster by last name.\n")

#Initiates what the main def is    
def main():
    choice = showMenu()
    if choice == 1:
        addEmployee()
        main() #All of these return the app to run again until 5 is selected
    elif choice == 2:
        printEmployeeList()
        main()
    elif choice == 3:
        deleteEmployee()
        main()
    elif choice == 4:
        sortEmployeeList()
        main()
    elif choice == 5: #Ends app
        print("Thanks for using this application. Please hit enter to exit.")
    else: #Prints error and forces correct selection
        print("Invalid Choice: Please select 1-5\n")
        main()
        
main()
