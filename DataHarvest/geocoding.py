# -*- coding: utf-8 -*-
# Reverse Geocoding Script
# UoM M2M University Challenge 2013
# R. Yang
#
# For use with Google Maps API v3
############################################################################
import urllib
import json

def reverse_geocoding(lat, lng):
    url = 'https://maps.googleapis.com/maps/api/geocode/json?&latlng=%s,%s&sensor=true'%(lat,lng)  
    json_output = urllib.urlopen(url).read()
    decoder = json.JSONDecoder()
    result = decoder.decode(json_output)
    result_l = result[u'results']
    for entry in result_l:
        r2_l = entry[u'address_components']
        for entry2 in r2_l:
            if u'political' in entry2[u'types']:
                location = entry2[u'long_name']
    return location

def geocoding(address):
    url = 'https://maps.googleapis.com/maps/api/geocode/json?&address={}&sensor=true'.format(address)
    json_output = urllib. urlopen(url).read()
    decoder = json.JSONDecoder()
    result = decoder.decode(json_output)
    try:
        result_l = result[u'results'][0][u'geometry'][u'location']
    except:
        return False
    return result_l[u'lat'], result_l[u'lng']

