# Reverse Geocoding
# UoM Telstra M2M Challenge 2013
# R. Yang
#
################################################################################
import urllib2
import sys

# Geonames user details
user = 'uomtelstra'

# Geonames API URL 
site1 = 'api.geonames.org/findNearbyPostalCodes?'

def main(lat, lng):
    params = urllib.urlencode({
        'lat':lat,
        'lng':lng,
        'radius':1,
        'style':'SHORT'
        'country':'au'
        'username':'uomtelstra'
    })
    response = urllib2.urlopen(site1, params).read()
    print response

if __name__ == '__main__':
    try:
        main(sys.argv[1], sys.argv[2])
    except IndexError:
        print 'input geonames.py [lat] [lng]'
