from Employee import *

listSals = []

s1 = Employee(111,"Smith","Joe",45)
print (s1.getFirstName())
s1.setFirstName("Jack")
print(s1.getFirstName(),  s1.getLastName(), s1.getSal())

listSals.append(s1.getSal())

s2 = Employee(222, "Jones", "Jennifer", 30)
print(s2.getFirstName(),  s2.getLastName(), s2.getSal())

listSals.append(s2.getSal())

sumSals = listSals[0] + listSals[1]

avgSals = sumSals/2

print ("Average age of students is: ", avgSals)
