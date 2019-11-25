# A math calculator

# imports math module
import math

# prints welcoming text
print "Welcome to this calculator!"

# loops program
while True:
	# asks questions
	operator = raw_input("What operator would you like to use? (+, -, x, /, mod, ^, %, sqrt) ")
	if operator == '+':
		num1 = float(raw_input("What is your augend? "))
		num2 = float(raw_input("What is your addend? "))
	elif operator == '-':
		num1 = float(raw_input("What is your minuend? "))
		num2 = float(raw_input("What is your subtrahend? "))
	elif operator == 'x':
		num1 = float(raw_input("What is your multiplicand? "))
		num2 = float(raw_input("What is your multiplier? "))
	elif operator == '/':
		num1 = float(raw_input("What is your dividend? "))
		num2 = float(raw_input("What is your divisor? "))
	elif operator == 'mod':
		num1 = float(raw_input("What is your first operand? "))
		num2 = float(raw_input("What is your second operand? "))
	elif operator == '^':
		num1 = float(raw_input("what is your base? "))
		num2 = float(raw_input("What is your index? "))
	elif operator == '%':
		num1 = float(raw_input("What is your percentage (Do not include % sign)? "))
		num2 = float(raw_input("What is your number? "))
	elif operator == 'sqrt':
		num1 = float(raw_input("what is your number? "))
	elif operator == '!':
		num1 = float(raw_input("what is your number? "))

	# does math
	if operator == '+':
		print num1 + num2
	elif operator == '-':
		print num1 - num2
	elif operator == 'x':
		print num1 * num2
	elif operator == '/':
		print num1 / num2
	elif operator == '^':
		print num1 ** num2
	elif operator == '%':
		print num1 / 100 * num2
	elif operator == 'mod':
		print num1 % num2
	elif operator == 'sqrt':
		print math.sqrt(num1)
	# alerts user if don't input valid symbol for operator
	else:
		print "Please input a valid symbol as an operator(+, -, x, /, mod, ^, %, sqrt)."

	# a way to end program
	programEnder = True
	while programEnder:
		to_stop = raw_input("Please input continue or done. ")
		if to_stop == 'continue':
			print "Great!"
			programEnder = False
		elif to_stop == 'done':
			print "Thank you for using this calculator! Have a good day!"
			quit()
		else:
			programEnder = True
