# Smart Ads Algorithms
#
# Designed and Written by R. Yang
#
# Alpha build
#
# Trivial and simple implementation of relevancy computation
# Future builds will focus on proper statistical distributions and
# Data mining concepts to improve relevancy computation.
#
# Future implementations include: 
# Poisson Modelling for Weather Condition Scoring with seasonal adjustments
# Modelling Time Scores and Temperature Scores using normal distrubtion with
# seasonal adjustments
# Data Mining functions that will load data into database
# Bias estimation for advertisers. Identifies what params advertisers desire 
###############################################################################
import sys
import math
import datetime
import time
import MySQLdb

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
    return

def getTime():
	'gets the current time based on system time'

	t = time.ctime()
	t = time.split()
	t = time[3]
	t = time.split(':')
	t = time[0]

	return t

def computeAll():
	'computes relevance for all the advertisements in ads_advertisment'
	db = connectDB()
	c = db.cursor()
	c1 = db.cursor()

	t = getTime()

	q = 'SELECT * FROM ads_advertisment'
	c.execute(q)

	for e in c:
		q1 = 'SELECT AdLocID FROM ads_adlocation WHERE AdID = %d'%(e[0])
		c1.execute(q1)
		e1 = c1.fetchone()
		q2 = 'SELECT * FROM ads_weather WHERE LocID =%d'%(e1[0])
		c2 = db.cursor()
		c2.execute(q2)
		weather = c2.fetchone()
		c2.close()
		computeRelevance(db, adID, weather, time)

	c1.close()
	c.close()
	closeDB(db)
	return

def computeRelevance(db, adID, weather, time):
	'computes the relevance for an advertisement and updates the entry \
		in the advertisement table'
	c = db.cursor()
	c1 = db.cursor()

	q = 'SELECT * FROM ads_advertisment WHERE AdID = %d'%(adID)
	q1 = 'SELECT AdLocID FROM ads_adlocation WHERE AdID = %d'%(adID)

	c.execute(q)
	c1.execute(q1)

	adLocID = c1.fetchone()[0]
	c1.close()

	e = c.fetchone()
	dtemp = e[5]
	dcond = e[6]
	dwind = e[7]
	dhumidity = e[8]
	dtime = e[9]

	tempScore = computeTemperatureScore(db, dtemp, weather[1])
	condScore = computeConditionScore(db, dcond, weather[2])
	windScore = computeWindScore(db, dwind, weather[3])
	humidityScore = computeHumidityScore(db, dhumidity, weather[4])
	timeScore = computeTimeScore(db, dtime, time)

	relevance = float(tempScore + condScore + windScore + humidityScore 
					+ timeScore) / 5

	# insert new score into DB
	q = 'UPDATE ads_advertisment \
		 SET Rel=%f \
		 WHERE AdID=%d'%(relevance, adID)
	c.execute(q)

	c.close()

	return

def computeTemperatureScore(db, dtemp, temp):
	'computes the temperature score considering discriminatory confidence \
		interval'

	# get discriminatory confidence
	c = db.cursor()

	query = 'SELECT TempAVG, TempLQ, TempHQ \
			 FROM ads_trivialweather \
			 WHERE Season=%d'%(getSeason())

	if(c.execute(query) >= 1):
		tempData = c.fetchone()
	else:
		# database failed 
		return 0

	# compute discriminated score
	if(tempData[1] <= dtemp <= tempData[2]):
		score = 1 - (getDFactor * 
			(fabs(dtemp - temp) / (tempData[2] - tempData[1])))
	else:
		# normal scoring
		score = 1 - (fabs(dtemp - temp) / (tempData[2] - tempData[1]))
	
	# FUTURE DATA MINING ADDITION
	# logScoring()
	# mineBias()

	c.close()

	return score

def computeConditionScore(db, dcond, cond):
	'computes the condition score considering the discriminatory confidence \
		interval'

	c = db.cursor()

	query = 'SELECT MistP, CloudsP, ClearP, RainP \
			 FROM ads_trivialweather \
			 WHERE Season=%d'%(getSeason())

	if(c.execute(query) >= 1):
		condData = c.fetchone()
	else:
		# database failed 
		return 0

	# discrimination applies to all weather events. 
	# the lesser the probability of the event, the least discrimination is 
	# applied when determining the condition score.
	# NOTE: This is a general case.
	# Realistically, this will be modelled using Poisson Distribution, but
	# I simply don't have the time to model it now.
	if(dcond == cond):
		score = 25 * condData[cond]
	else:
		score = 0

	c.close()

	return score

def computeHumidityScore(db, dhumidity, humidity):
	'computes humidity score considering the discriminatory confidence \
		interval'
	
	c = db.cursor()

	query = 'SELECT HumidityAVG, HumidityLQ, HumidityHQ \
			 FROM ads_trivialweather \
			 WHERE Season=%d'%(getSeason())

	if(c.execute(query) >= 1):
		hData = c.fetchone()
	else:
		return 0

	# compute discriminated score
	if(hData[1] <= dhumidity <= hData[2]):
		score = 1 - (getDFactor * 
			(fabs(dhumidity - humidity) / (hData[2] - hData[1])))
	else:
		# normal scoring
		score = 1 - (fabs(dhumidity - humidity) / (hData[2] - hData[1]))

	return score

def computeWindScore(db, dwind, wind):
	'compute wind score considering the discriminatory confidence interval'

	c = db.cursor()

	query = 'SELECT WindAVG, WindLQ, WindHQ \
			 FROM ads_trivialweather \
			 WHERE Season=%d'%(getSeason())

	if(c.execute(query) >= 1):
		wData = c.fetchone()
	else:
		return 0

	# compute discriminated score
	if(wData[1] <= dwind <= wData[2]):
		score = 1 - (getDFactor * 
				(fabs(dwind - wind) / (wData[2] - wData[1])))
	else:
		# normal scoring
		score = 1 - (fabs(dwind - wind) / (wData[2] - wData[1]))

	return score

def computeTimeScore(db, dtime, time):
	'compute the time score considering the discriminatory confidence \
		interval'

	# time discrimination is an interesting one.
	# Ideally, we would want to discriminate based on the usage pattern
	# of sign users, so we could normalise abuse attempts where 
	# advertisers attempt to lock in popular times that actually cost 
	# cheap.
	# In future implementations, we do not discriminate time, but we 
	# would apply premium charges on time blocks which correlate with
	# high usage patterns

	if(fabs(dtime - time) < 4):
		score = (float(fabs(dtime - time)) / 4.0) * 25
	else:
		score = 0

	return score

def getSeason():
	'gets the current season based on the date time'
	SPRING = 0
	SUMMER = 1
	AUTUMN = 2
	WINTER = 3

	dateClass = datetime.date
	date = str(dateClass.today( ))
	date = date.split('-')

	month = date[1]
	day = date[2]

	if (month == 9 or month == 10 or month == 11):
		return SPRING
	elif (month == 12 or month == 1 or month == 2):
		return SUMMER
	elif (month == 3 or month == 4 or month == 6):
		return AUTUMN
	else:
		return WINTER

	return

def getDFactor():
	'gets the discrimination factor'
	# in trial
	return 4

# FUNCTIONS BELOW ARE NOT AVAILABLE FOR PROTOTYPE
def logScoring():
	'logs scoring history of the advertisement and its penalties'

	return

def mineBias():
	'mines instances of discrimination for future dFactor adjustments'

	return


# MAIN 
def main():
	computeAll()
	updateAll()

if __name__ == '__main__':
	main()


