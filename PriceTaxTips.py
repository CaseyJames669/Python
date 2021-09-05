#prompt for price of meal, sales tax, and gratuity percentage
mealPrice, salesTax, gratuity = eval(input(
    "Enter the Meal Cost, Sales Tax Percentage, and Gratuity Percentage you would like to add: "))

#calculations
#calculates the original price times the tax percentage, and adds them together
subTotal = (1+(salesTax/100))*mealPrice

#calculates the tip amount that will be added to the subtotal - post-tax
gratuityAmount = (gratuity/100)*subTotal

#adds the subtotal and tip amount together, and creates a new variable equating the total
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

      

