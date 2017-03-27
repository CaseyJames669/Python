flength, ilength = eval(input("Please enter the length of room in ft, in: "))
fwidth, iwidth = eval(input("Please enter the width of the room in ft, in: "))
sqyards = ((((flength * fwidth)/3)+((ilength*iwidth)/36))/3)
taxrate = .065
costpersqyrd = eval(input("Please enter the cost of the carpet per sq. yard: "))
carpetcost = costpersqyrd * sqyards
taxamt = carpetcost * taxrate
totalcost = taxamt + carpetcost
print("The total square yards of your room is ", sqyards)
print("The cost of the carpet is ", round(carpetcost, 2))
print("The taxed amount is ", round(taxamt, 2))
print("The total cost is ", round(totalcost, 2))
