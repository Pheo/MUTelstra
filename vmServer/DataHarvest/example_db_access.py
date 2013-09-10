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

# show tables in database 
print "\nShow tables in ids database"
query = "SHOW tables"
cur.execute(query)
# cur is a 'list' of rows. Hence the "for e in cur"
for e in cur:
	print e

# show table schema 
print "\nShow structure of ads_advertisment table"
query = "DESCRIBE ads_advertisment"
cur.execute(query)
for e in cur:
	print e

# select rows from a table 
print "\nSelect rows from ads_advertisment table"
query = "SELECT * FROM ads_advertisment WHERE Name = 'Coca Cola'"
cur.execute(query)
for e in cur:
	print e


# Always remember to close. Don't leave hanging open conns
cur.close()
db.close()
