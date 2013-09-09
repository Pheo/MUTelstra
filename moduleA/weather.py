#-*- coding: utf-8 -*-
# weather.py
# Designed to work with OpenWeatherMap API
# Data belongs to OpenWeatherMap Organisation
# http://www.OpenWeatherMap.org
#
# written by R. Yang
###############################################################################
import urllib
import json
import sys
import MySQLdb
from geocoding import geocoding

APIkey = '3bd5c94e9cb2db2c267b0d78623ccd1b'
hostdet = "localhost"
userdet = "renlord"
passwddet = "renlord"
dbdet = "ids" 

def connectDB():
    'connects to the database in the Virtual Machine'
    db = MySQLdb.connect(host=hostdet,user=userdet,passwd=passwddet,db=dbdet)
    cur = db.cursor()
    return db, cur

def closeDB(db, cur):
    'closes and commits all changes to the DB'
    cur.close()
    db.commit()
    db.close()

def getWeatherGPS(lat, lng):
    'gets weather based on GPS coordinates of a location'
    url = \
    'http://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&APPID={}'.format(
        lat, lng, APIkey)
    decoder = json.JSONDecoder()
    json_object = urllib.urlopen(url).read()
    db, cur = connectDB()
    query = "SELECT LocID FROM ads_location WHERE\
		 GPS_Lat = %s AND GPS_Long = %s" %(lat, lng)
	has_city = cur.execute(query)
	if has_city:
		weather, param_list = getWeatherID(cityID)
	else:
    	cityID = getCityID(json_object) #put this into DB
    	weather, param_list = processWeatherDetails(json_object)
		query = "INSERT INTO ads_location SET CityID=%d, GPS_Lat=%f, GPS_Long=%f" %(cityID, lat, lng)
    # query if there's a CityID with this Lat, Lng
        #if there is:
        # weather, param_list = getWeatherID(cityID)
    # else
    return weather, param_list

def getWeatherLocation(address):
    'gets weather based on the address of the location'
    lat, lng = geocoding(address)
    lat = float('%.2f' %lat)
    lng = float('%.2f' %lng)
    weather, param_list = getWeatherGPS(lat, lng)
    return weather, param_list

def getWeatherID(cityID):
    'gets weather based on the city id'
    url = \
    'http://api.openweathermap.org/data/2.5/weather?id={}&APPID={}'.format(cityID, 
        APIkey)
    decoder = json.JSONDecoder()
    json_object = urllib.urlopen(url).read()
    weather, param_list = processWeatherDetails(json_object)
    return weather, param_list

def getCityID(json_object):
    'extracts City ID from the json object'
    decoder = json.JSONDecoder()
    data = decoder.decode(json_object)
    return data[u'id']

def processWeatherDetails(json_object):
    'process the JSON object from the API'
    param_list = ['temp', 'cond', 'wind', 'humidity']
    weather_conds = [u'Mist', u'Clouds', u'Clear', u'Rain']
    decoder = json.JSONDecoder()
    # In the event there's no json_object. Returns false
    try:
        weather = decoder.decode(json_object)
    except ValueError:
        sys.exit()

    weather1 = weather[u'weather'][0]
    weather2 = weather[u'main']
    weather3 = weather[u'wind']
    weather_d = {}
    weather_d['temp'] = KtoC(int(weather2[u'temp']))
    weather_d['cond'] = getCondEnum(weather1[u'main'])

    weather_d['wind'] = float(weather3[u'speed'])
    weather_d['humidity'] = int(weather2[u'humidity'])
    return weather_d, param_list

def updateWeather():
    return

def KtoC(kelvin):
    return (kelvin - 273)

def getCondEnum(cond):
    weather_conds = [u'Mist', u'Clouds', u'Clear', u'Rain']
    enum_l = [u'Mist', u'Clouds', u'Clear', u'Rain', u'Other']

    if cond not in weather_conds:
        return enum_l.index(u'Other')
    else:
        return enum_l.index(cond)

def main():
    return


