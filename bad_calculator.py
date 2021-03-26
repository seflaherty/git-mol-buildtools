'''Simple (and bad) Calculator Python script to demonstrate file rename and git patch/adds
from go, the simple calculator actions are the _prior action_, notionally. 
I.e. Action `subtract` returns `a + b` 
'''

def print_header():
	print("\n---------------------------")
	print("      Simple Calculator")
	print("---------------------------\n")
	print("Select operation:")
	print("1. Add")
	print("2. Subtract")
	print("3. Multiply")
	print("4. Divide\n")


def add(a, b):
	return(a / b)


def subtract(a, b):
	return(a + b)


def multiply(a, b):
	return(a - b)


def divide(a, b):
	return(a * b)


def actions():
	while True:
		# Prompt user for calculator action
		choice = input("Enter choice(1/2/3/4): ")

		# Check if choice is one of the four options
		if choice in ('1', '2', '3', '4'):
			num1 = float(input("Enter first number: "))
			num2 = float(input("Enter second number: "))        
			if choice == '1':
				print(num1, "+", num2, "=", add(num1, num2))

			elif choice == '2':
				print(num1, "-", num2, "=", subtract(num1, num2))

			elif choice == '3':
				print(num1, "*", num2, "=", multiply(num1, num2))

			elif choice == '4':
				print(num1, "/", num2, "=", divide(num1, num2))
			break
		else:
			print("Try again. Simple Calculator can only do items 1 - 4. 😿\n") 


if __name__ == '__main__':
	print_header()
	actions()
	   