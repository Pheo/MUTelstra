# Ad Manager
#

import sys
import MySQLdb

from weather import *


def updateAll():
	db, cur = connectDB()
	cur2 = db.cursor()
	# iterate through the Weather Table, update weather for each location.
	query = "SELECT LocID FROM ads_weather"
	cur.execute(query)
	for e in cur:
		LocID = e[0]
		query = "SELECT GPS_Lat, GPS_Long FROM ads_location WHERE LocID = %d" %(LocID)
		cur2.execute(query)
		for f in cur2:
			GPS_Lat = f[0]
			GPS_Long = f[1]
			Weather, Param_List = getWeatherGPS(GPS_Lat, GPS_Long)
			query = "UPDATE ads_weather SET Temp = %d, Cond = %d, Wind = %f,\
				 Humidity = %d WHERE LocID = %d"\
				 % (Weather['temp'], Weather['cond'], Weather['wind'],\
					 Weather['humidity'], LocID)
	return

def pushAllSign():
	# iterate through Weather Table, CALL push2sign(data) to push the 
	# weather data to all signs with the location ID of the current entry.
	

	return

def push2sign(data, dest):
	# push the data in argument to the relevant sign. 
	return

def main():
	updateAll()
	return

if __name__ == '__main__':
	main()

