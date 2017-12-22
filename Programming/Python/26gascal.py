import locale

locale.setlocale(locale.LC_MONETARY, '')

print "Thank you for using GasCal! We hope you find it useful!"
car_type = raw_input("What type of car do you have? ")
if car_type == "Lamborghini Veneno" or car_type == "Ferrari Pininfarina Sergio":
    print "Wow, you got da bling bling!"
miles_driven = float(raw_input("How many miles have you driven on your %s? " % (car_type)))
price_of_gas = float(raw_input("What is the price per gallon of your preferred gasoline? ").replace("$", ""))
gallons_per_tank = float(raw_input("How many gallons can your car's gas tank hold? "))
if car_type == "Lamborghini Veneno" and gallons_per_tank != 23.8:
    print "Wrong! You don't really own a Lamborghini Veneno!"
    quit()

print "Thank you! This is your cost(assuming your tank is completely empty), miles per gallon, and cost per mile driven."

print "Cost of gas: " + locale.currency((gallons_per_tank * price_of_gas), grouping=True)
print "Miles per gallon: " + str(miles_driven / gallons_per_tank) + " miles"
print "Cost per mile: " + locale.currency(price_of_gas / (miles_driven / gallons_per_tank), grouping=True)
