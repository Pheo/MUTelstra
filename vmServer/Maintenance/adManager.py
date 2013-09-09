# Ad Manager
#

import sys
import MySQLdb

from weather import *

hostdet = "localhost"
userdet = "renlord"
passwddet = "renlord"
dbdet = "ids" 

def connectDB():
    'connects to the database in the Virtual Machine'
    db = MySQLdb.connect(host=hostdet,user=userdet,passwd=passwddet,db=dbdet)
    return db

def closeDB(db):
    'closes and commits all changes to the DB'
    db.commit()
    db.close()

def updateAll():
	db, cur = connectDB()
	# iterate through the Weather Table, update weather for each location.

	return

def pushAllSign():
	# iterate through Weather Table, CALL push2sign(data) to push the 
	# weather data to all signs with the location ID of the current entry.

	return

def push2sign(data, dest):
	# push the data in argument to the relevant sign. 
	return

def main():

	return

if __name__ == '__main__':
	main()

