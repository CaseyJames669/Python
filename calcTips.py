#prompt for multiple variables
sub, grat = eval(input(
    "Enter the subtotal and a gratuity rate: "))

#calculations
grat = grat/100
gratuity = sub*grat
total = sub+gratuity

#Display it all
print("The gratuity is ", round(gratuity, 2),
      "and the total is ", round(total, 2))

##NOTE: rounding is done inside print string##

      

