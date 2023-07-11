miles = 0.0
gallons = 0.0
mpg = 0.0

miles = float(input("Enter the miles driven"))
gallons = float(input("Enter the gallons of fuel used"))
mpg = miles/gallons
print ("You used", format(mpg, '.2f'), "miles per gallon")
