"""
Assignment 6: Help menu for a menu-driven application
that maintains a list of employees - Part 1
Using functions def main(), showMenu(), etc...
"""
__author__="Casey Bladow"
__date__="11/05/12"

#The menu itself
def showMenu():
    print("\nEmployee Maintence")
    print("1) Add a New Employee")
    print("2) Print Employee Roster")
    print("3) Delete an Employee")
    print("4) Sort Employee Roster by Last Name")
    print("5) Find an Employee")
    print("6) Change Employee Name")
    print("7) Exit")
    choice = eval(input("Enter your choice (1-7): "))
    return choice

#What happens when 1 is chosen
def addEmployee():
    name = input("\nEnter the new employees name (ex: Doe, John): ")
    empList.append(name)
    tmpName = input("\nIf you have more names to add do so now, \notherwise enter x to go back to the main menu: ")
    while tmpName != 'x':
        empList.append(tmpName)
        tmpName = input("\nIf you have more names to add do so now, \notherwise enter x to go back to the main menu: ")

#What happens when 2 is chosen
def printEmployeeList():
    if len(empList) == 0:
        print("\nERROR - There are no names in your employee manifest.")
        print("You will now be sent back to the main menu.")
        main()
    elif len(empList) != 0:
        print("\nBig D's Bar And Grill")
        for ct in range(len(empList)):
            print(empList[ct])
        
#What happens when 3 is chosen
def deleteEmployee():
                            #No names in list error
    if len(empList) == 0:
        print("\nERROR - There are no names in your employee manifest.")
        print("You will now be sent back to the main menu.")
        main()
                            #Gets name
    name = input("\nPlease enter the name of the employee you would like removed: ")
                            #If name IS NOT in list
    while name not in empList and name != 'x':
        print("\nERROR - That name is not in your manifest.")
        name = input("\nPlease enter the name of the employee you would like removed,\notherwise enter x to go back to the main menu: ")
                            #If name IS IN list
    while name in empList and name != 'x':
        empList.remove(name)
        print(name, "has been removed from the employee manifest.")
        name = input("\nPlease enter the name of the employee you would like removed,\notherwise enter x to go back to the main menu: ")
#What happens when 4 is chosen
def sortEmployeeList():
    empList.sort()
    print("\nYour manifest has been sorted.")
    print("You will now be sent back to the main menu.")

def linearSearch(empList, key): #created a search def to find the location of a name
    for i in range(len(empList)):
        if key == empList[i]:
            return i
    return -1

def findEmp():
    #No employees on list
    if len(empList) == 0:
        print("\nERROR - There are no names in your employee manifest.")
        print("You will now be sent back to the main menu.")
        main()
    name = input("\nPlease enter the name of the employee you would like to search for: ")
                #if name is in the list
    while name in empList and name != 'x':
        i=linearSearch(empList, name)
        print(name, i+1)
        name = input("\nPlease enter another name, or 'x' to exit: ")
        
                #while name is not in the list
    while name not in empList and name != 'x':
        print("\nERROR - The name you entered is not located in your manifest.")
        name = input("Please enter another name, or 'x' to exit: ")

def changeEmployee():
    #No employees on list
    if len(empList) == 0:
        print("\nERROR - There are no names in your employee manifest.")
        print("You will now be sent back to the main menu.")
        main()
    name = input("\nPlease enter the name of the employee you would like to replace: ")

    while name in empList and name != 'x':
        name = name
        newName = input("Please enter the new name: ")
        empList.remove(name)
        empList.append(newName)
        name = input("\nPlease enter another name, or 'x' to exit: ")

    while name not in empList and name != 'x':
        print("\nERROR - The name you entered is not located in your manifest.")
        name = input("Please enter another name, or 'x' to exit: ")

        
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
    elif choice == 5:
        findEmp()
        main()
    elif choice == 6:
        changeEmployee()
        main()
    elif choice == 7: #Ends app
        print("\nThanks for using this application.")
        data = input("Please hit ENTER to exit program.")
    else: #Prints error and forces correct selection
        print("Invalid Choice: Please select 1-7\n")
        main()

empList = []        
main()
