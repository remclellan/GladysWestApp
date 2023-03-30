import io
from email_validator import validate_email

"""
	Student: Raquel McLellan
	Module: gladysUserLogin
	Description: This module validates that the user has entered a valid email address format
"""


def login():
	"""
		Func: Login
		Desc: chest user input to confirm format is a valid email address
	"""

	v = ""

	while (v != True):
		emailAddress = input("Enter user email address: ")
		password = input("Enter user password: ")

		v = validate_email(emailAddress)

		if v:
			return emailAddress
		else:
			print("User email is not a valid. Please try again.")



	
