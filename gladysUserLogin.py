import io
import re

"""
	Student: Raquel McLellan
	Module: gladysUserLogin
	Description: This module validates that the user has entered a valid email address format
"""

def validate_email(email):
	if re.match(r"[^@]+@[^@]+\.[^@]+", email):
		return True
	else:
		return False


def login():
	"""
		Func: Login
		Desc: chest user input to confirm format is a valid email address
	"""

	valid = ""

	while (valid != True):
		emailAddress = input("Enter user email address: ")
		password = input("Enter user password: ")

		valid = validate_email(emailAddress)

		if valid:
			return emailAddress
		else:
			print("User email is not a valid. Please try again.")



	
