import io
import os
import re
import math

import gladysCompute as compute
import gladysSatellite as satellite
import gladysUserLogin as userLogin

"""
	Student: Raquel McLellan
	Module: gladysUserInterface
	Description: This module does sets up the main menu the user will select from as well as call to other modules and execute
"""

def is_integer(num):
    """
		Func: test if input is a whole number
		Desc: Intakes user_input for coordinate to confirm entry is a whole number for validation purposes
	"""
    try:
        # Convert it into integer
        val = int(num)
        return True
    except ValueError:
        try:
	    # Convert to float to validate if whole number
            val = float(num)
            return val.is_integer()
        except ValueError:
            return False

def validXNumber():
	"""
		Func: Validate X input
		Desc: Confirms user entry is both whole number and within range for acceptable coordinate
	"""

	validX = ""

	while (validX != True):
		coordinate = input("Enter a numeric x position: ")
		wholeX = is_integer(coordinate)
		if float(coordinate) >= 0 and float(coordinate) <= 99:
			rangeX = True
		else:
			rangeX = False

		if wholeX and rangeX:
			validX = True
			return coordinate
		else:
			validX = False
			print(" Invalid entry. Please use whole numbers between 0 to 99.")


def validYNumber():
	"""
		Func: Validate Y input
		Desc: Confirms user entry is both whole number and within range for acceptable coordinate
	"""

	validY = ""

	while (validY != True):
		coordinate = input("Enter a numeric y position: ")
		wholeY = is_integer(coordinate)
		if float(coordinate) >= 0 and float(coordinate) <= 99:
			rangeY = True
		else:
			rangeY = False

		if wholeY and rangeY:
			validY = True
			return coordinate
		else:
			validY = False
			print("Invalid entry. Please use whole numbers between 0 to 99.")


def runTests():
	"""
		Func: Tests
		Desc: Tests selected linked module functions
	"""

	print("Testing connected modules:")

	# testing gpsValue function from gladysCompute module
	print("Testing gladysCompute module...\n")
	testX = validXNumber()
	testY = validYNumber()
	average = compute.gpsAverage(testX, testY)
	print("average = ", average)

	# testing readSat function from gladysSatellite module
	print("Testing gladysSattelite module...")
	testX = validXNumber()
	testY = validYNumber()
	satName = input("Please enter one of the following options: altitude, latitude, longitude, time: ")
	satChoice = satName.lower()
	data = satellite.gpsValue(testX,testY,satChoice)
	print("Satellite data requested: " + str(data))

	# testing login function from gladysUserLogin
	print("Testing gladysUserLogin module...")
	testUser = userLogin.login()
	print(testUser)

	print("Testing complete!\n")


def start():
	"""
		Func: Start
		Desc: Calls login module to login user (if email valid) and runs app
	"""
	userName = userLogin.login()

	runApp(userName)

def menu(currentX,currentY,destinationX,destinationY, user):
	"""
		Func: Menu
		Desc: Displays menu of choices for user to select from
	"""
	# menu choices
	print("----------------------------------------")
	print("-- Welcome to the Gladys West Map App --")
	print("   Logged In User: " + user )
	print("----------------------------------------")
	print("Current = (" + str(currentX) + ", " + str(currentY) + ")")
	print("Destination = (" + str(destinationX) + ", " + str(destinationY) + ")")
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
	user = userName

	# initialize x,y values with valid integers for current and destination
	currentX = 0
	currentY = 0
	destinationX = 0
	destinationY = 0


	# loop until user types q
	userQuit = False
	while (not userQuit):

		# calls menu procedure
		menu(currentX, currentY, destinationX, destinationY, user)

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
			currentX = validXNumber()
			currentY = validYNumber()

		#allows user to enter coordinates for destination position
		elif firstChar == 'd':
			destinationX = validXNumber()
			destinationY = validYNumber()

		# run function to tell distance between current and destination positions
		elif firstChar == 'm':
			distance = compute.distance(currentX,currentY,destinationX,destinationY)
			print("Distance: " + str(distance) + "\n")
		
		else:
			print("ERROR: " + firstChar + " is not a valid command")

	print("\n")
	print("Thank you for using the Gladys West Map App!")
	print("\n")