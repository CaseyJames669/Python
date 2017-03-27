#Example 1
#Print backwards
NUMBEROFNAMES = 5
names = []

for x in range(NUMBEROFNAMES):
    name = input("Enter a name: ")
    names.append(name)

print(names[0],names[1],names[2],names[3],names[4])
print(names[4],names[3],names[2],names[1],names[0])

for x in range(4,-1,-1):
    print(names[x])

#Example 2
#Put lists together
grocery = ["apples","oranges","bananas"]
bakery = list(["donuts","muffins"])

grocery.extend(bakery)

print(grocery)

#Example 3
#Put lists together without using .extend
grocery2 = ["apples","oranges","bananas"]
bakery2 = list(["donuts","muffins"])

ct=0

while ct <= 1:
    grocery2.append(bakery2[ct])
    ct += 1

print(grocery2)
