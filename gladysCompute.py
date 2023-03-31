import io
import os
import math

import gladysSatellite as satellite

"""
	Student: Raquel McLellan
	Module: gladysCompute
	Description: This module calculates distance between current and destination coordinates using satellite data
"""


def gpsAverage(x, y):
	"""
		Func: Average
		Desc: Calculates average of gps coordinates 
	"""
	# formula for value calculation provided in assignment
	valueLat = satellite.gpsValue(x, y, "latitude")
	valueLong = satellite.gpsValue(x, y, "longitude")
	valueAlt = satellite.gpsValue(x, y, "altitude")
	valueTime = satellite.gpsValue(x, y, "time")

	sum = (valueLat + valueLong + valueAlt + valueTime)

	average = (sum / 4)

	return average


def distance(curX, curY, destX, destY):
	"""
		Func: Distance
		Desc: Calculates Distance of Current and Destination coordinates using provided formula in assigment called gpsAverage for average 
	"""

	# formula for calculation provided in assignment; sqrt function from math library
	distance = math.sqrt((gpsAverage(curX, curY)*gpsAverage(curX,curY))+(gpsAverage(destX,destY)*gpsAverage(destX,destY)))

	return distance
