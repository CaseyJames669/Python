#prompt for price of meal, sales tax, and gratuity percentage
mealPrice, salesTax, gratuity = eval(input(
    "Enter the Meal Cost, Sales Tax Percentage, and Gratuity Percentage you would like to add: "))

#calculations
subTotal = (1+(salesTax/100))*mealPrice

gratuityAmount = (gratuity/100)*subTotal

total = subTotal+gratuityAmount

#This can also be written in one line...
# total = mealPrice+(((salesTax/100)*mealPrice)+((gratuity/100)*mealPrice))


#Display it all
print("Meal Price: $", round(mealPrice, 2),
      "Sales Tax: $", round(salesTax, 2),
      "Subtotal: $", round(subTotal, 2),
      "Gratuity: $", round(gratuityAmount, 2),
      "Total: $", round(total, 2))

##NOTE: rounding is done inside print string##

      

