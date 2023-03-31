import io
import json
import os

"""
	Student: Raquel McLellan
	Module: gladysSatellite
	Description: This module reads the satellite json file from the stored location using relative path to the data 
					and then looks up value based on the coordinates provided to return value for calculations
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
		Func: GPS Value
		Desc: Using coordinates provided looks up value assigned based on selected satellite and returns result for use in other modules
	"""
	# using relative path file leverage os library 
	pathToJSONDataFiles = os.path.realpath(os.path.join(os.path.dirname(__file__),'data'))

	# read the satellite data
	data = readSat(sat, pathToJSONDataFiles)

	# create an empty dictionary
	gpsCoordinates = {}

	# loop json list of data and put each name and birthday into a dictionary
	for elem in data:
    	# fetch name and birthday
		satX = elem["x"]
		satY = elem["y"]
		value = elem["value"]
		
		# set dict key to x,y coordinate comb
		gpsCoordinates[satX,satY] = value

	# user input was showing as string so int() ensures variables are read correctly to return value from dict
	result = gpsCoordinates[int(x),int(y)]
	
	return result