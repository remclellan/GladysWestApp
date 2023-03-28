import io
import json

"""
	Student: Gabriel Solomon
	Module: gladysSatellite
	Description: This module does …
"""


def readSat(sat, pathToJSONDataFiles):
	"""
		reads satellite data from a json file
		Students do NOT need to change the readSat function.
	"""

	# data file path
	fileName = sat + "-satellite.json"
	filePath = pathToJSONDataFiles + "/" + fileName

	# open the file
	try:
		fileHandle = open(filePath)
	except IOError:
		print("ERROR: Unable to open the file " + filePath)
		raise IOError

	# print("filePath = ", filePath)

	# read the file
	data = json.load(fileHandle)

	return data


def gpsValue(x, y, sat):
	"""
		document your function definition here. what does it do?
	"""

	"""
		This first part of this function to read satelite data only read 
		satellite data. students need to change the pathToJSONDataFiles 
		variable so it works on your computer.

		this is *windows* path, not a mac path.
		if you do not know what a path (on a computer) is, you should use google and
		youtube to learn, or come to office hours so I can explain it to you.

		students will need to change this pathToJSONDataFiles variable to point to
		where you have the data files stoed on your computer.  If you do not
		change it, the code will not "work".

		You can/should remove this long comment before you submit your work.  
		I'm just giving advice to try to help you. Good luck!  -Gabriel :)
	"""
	pathToJSONDataFiles = "/data"

	# read the satellite data
	data = readSat(sat, pathToJSONDataFiles)

	"""
		delete the remaining code *in this function* and replace it with
		your own code. add more code to do what the assignment asks of you.

		tip: here is where students need to look through the data variable
		read from the satellites and find a matching x,y to return the value.
		to understand better, open and look at the json satellite data in
		vs code.
	"""
	value = 1234

	return value
