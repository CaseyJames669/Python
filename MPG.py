gallonsused = eval(input("How many gallons of gas did you use? "))
startingmileage = eval(input("What was your starting mileage? "))
endmileage = eval(input("What was your ending mileage? "))
distancetraveled = endmileage - startingmileage
mpg = (endmileage - startingmileage) /gallonsused
print("Traveling ", distancetraveled, "miles you got ", mpg, " Miles per Gallon.")

