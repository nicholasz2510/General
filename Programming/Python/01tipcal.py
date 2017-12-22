# The next three lines of code ask questions for the user to answer.
meal = float(raw_input("What is the cost of your meal? $"))
tax = float(raw_input("What is the tax percentage in your state? (Do not put %) "))
tip = float(raw_input("What percentage would you like to tip? (Do not put %) "))

# The next two lines of code turn the tip and tax input from percentages into decimals.
tip = tip / 100
tax = tax / 100

# These lines of code find the total amount of money.
tax_dollars = meal * tax
subtotal = tax_dollars + meal
tip_dollars = subtotal * tip
total = tip_dollars + subtotal

#This line of code prints the total.
print "The total amount of money you must pay for your meal is: $%.2f" % total
