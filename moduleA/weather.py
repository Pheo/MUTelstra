# -*- coding: utf-8 -*-
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
from geocoding import geocoding

APIkey = '3bd5c94e9cb2db2c267b0d78623ccd1b'

def getWeatherGPS(lat, lng):
	'gets weather based on GPS coordinates of a location'
	url = \
	'http://api.openweathermap.org/data/2.5/weather?lat={}&lon={}'.format(lat, lng)
	decoder = json.JSONDecoder()
	json_object = urllib.urlopen(url).read()
	weather, param_list = processWeatherDetails(json_object)
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

    return weather, param_list,

def createLocationID(cityID, param=None):
    'creates a database entry with CityID for a location.'
    if type(param) = tuple:
        
        
    if type(param) = str:
        
    return

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


