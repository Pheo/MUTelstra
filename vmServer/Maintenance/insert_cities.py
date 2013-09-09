# UoM Telstra M2M Challenge

# Insert Cities Data into Location table
# Written by Jun Min Cheong (Pheo)

################################################################################

# Example only. Please adapt accordingly

import MySQLdb

# Login Details
hostdet = "localhost"
userdet = "root"
passwddet = "BlueCheese93"
dbdet = "ids"

db = MySQLdb.connect(host=hostdet,user=userdet,passwd=passwddet,db=dbdet)
cur = db.cursor()

f = open("cities.txt").read().split('\n')

# Ignore header line
for line in f[1:]:
	# Ignore country code
	location = line.split('\t')[:-1]
	query = "INSERT INTO ads_location SET LocID=%d,GPS_Lat=%f,GPS_Long=%f,Name='%s'" %(int(location[0]), float(location[2]), float(location[3]), location[1])
	cur.execute(query)




# Always remember to close. Don't leave hanging open conns
cur.close()
db.commit()
db.close()
