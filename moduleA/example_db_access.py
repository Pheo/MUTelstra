# UoM Telstra M2M Challenge

# Example database access code 
# Written by Jun Min Cheong (Pheo)

################################################################################

# Example only. Please adapt accordingly

import MySQLdb

# Login Details
hostdet = "localhost"
userdet = "renlord"
passwddet = "renlord"
dbdet = "ids"

db = MySQLdb.connect(host=hostdet,user=userdet,passwd=passwddet,db=dbdet)
cur = db.cursor()

# Standard MySQL query
query = "SELECT * FROM Advertisment WHERE Name = 'Coca Cola'"
cur.execute(query)

# cur is a 'list' of rows. Hence the "for e in cur"
for e in cur:
	print e

# Always remember to close. Don't leave hanging open conns
cur.close()
db.close()
