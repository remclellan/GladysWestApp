import io
import os

import gladysCompute as compute
import gladysSatellite as satellite
import gladysUserLogin as userLogin

"""
	Student: Raquel McLellan
	Module: gladysUserInterface
	Description: This module does sets up the main menu the user will select from as well as call to other modules and execute
"""


def runTests():
	"""
		Func: Tests
		Desc: Tests some module functions
	"""

	print("running a few tests")

	# testing gpsValue function from gladysCompute module
	average = compute.gpsAverage(4, 5)
	print("average = ", average)

	# testing readSat function from gladysSatellite module
	print("Testing sat module")

	# testing login function from gladysUserLogin
	testUser = userLogin.login()
	print(testUser)


def start():
	"""
		logs the user in, and runs the app
	"""

	userName = userLogin.login()

	runApp(userName)

def menu():
	"""
		Func: Menu
		Desc: Displays menu of choices for user to select from
	"""
	# menu choices
	print("----------------------------------------")
	print("-- Welcome to the Gladys West Map App --")
	print("----------------------------------------")
	print("[c] set current postion")
	print("[d] set destination position")
	print("[m] map distance between")
	print("[t] run module tests")
	print("[q] quit app")
	print("----------------------------------------")
	print("\n")

def runApp(userName):
	"""
		runs the app
	"""

	# loop until user types q
	userQuit = False
	while (not userQuit):

		# calls menu procedure
		menu()

		# get first character of input
		userInput = input("Enter a command:")
		lowerInput = userInput.lower()
		firstChar = lowerInput[0:1]

		# menu choices, use a switch-like if-elif control structure

		# quit
		if firstChar == 'q':
			userQuit = True

		# run some tests (this is part 1 of 2)
		elif firstChar == 't':
			runTests()
		
		# allows user to enter coordinate for current position
		elif firstChar == 'c':
			currentX = input("Enter x for current position: ")
			currentY = input("Enter y for current position: ")

		#allows user to enter coordinates for destination position
		elif firstChar == 'd':
			destinationX = input("Enter x for destination position: ")
			destinationY = input("Enter y for destination position: ")

		# run function to tell distance between current and destination positions
		elif firstChar == 'm':
			print("Distance: ")
		
		else:
			print("ERROR: " + firstChar + " is not a valid command")

	print("\n")
	print("Thank you for using the Gladys West Map App!")
	print("\n")