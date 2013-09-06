# -*- coding: utf-8 -*-
# Reverse Geocoding Script
# UoM M2M University Challenge 2013
# R. Yang
#
# For use with Google Maps API v3
############################################################################
import urllib
import urllib2
import sys
import json

def main(lat, lng):
    url = 'https://maps.googleapis.com/maps/api/geocode/json?&latlng=%s,%s&sensor=true'%(lat,lng)  
    json_output = urllib.urlopen(url).read()
    location = extract_loc(json_output)
    print location 

def extract_loc(json_file):
    decoder = json.JSONDecoder()
    result = decoder.decode(json_file)
    result_l = result[u'results']
    for entry in result_l:
        r2_l = entry[u'address_components']
        for entry2 in r2_l:
            if u'political' in entry2[u'types']:
                location = entry2[u'long_name']
                return location

if __name__ == '__main__':
    try:
        main(sys.argv[1], sys.argv[2])
    except IndexError:
        print 'input geocoding.py [lat] [lng]'
