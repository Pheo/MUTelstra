# UoM Telstra M2M Challenge
# HMTL Information Extractor
# for use with PTV Website
################################################################################
import urllib
import time

from HTMLParser import HTMLParser

# Important HTML Tags
LINK = "href"
TITLE = "title"

# Custom Omissions
blocked_urls = ["timetables/", "disruptions/", "tickets/myki/"]

# Keywords 

# Regular Expressions

# HTML Parser
class ptvHTMLParser(HTMLParser):
  def handle_starttag(self, tag, attrs):
    blocking = False
    if tag == "a" and attrs[0][0] == TITLE and attrs[1][0] == LINK:
      for url in blocked_urls:
        if url == attrs[1][1]:
          blocking = True
          break
      if not blocking:
        #TEMPORARY
        print attrs[0][1]
        print attrs[1][1]

  def handle_endtag(self, tag):
    return

  def handle_data(self, data):
    if toggle_data == True:
      print data

# Data Processing Function
"""
Function: build_output
PARAM:
  @ ptvdata, DICTIONARY data set.
  @ key, what is your data part of?
  @ data, concatenates your current data to lists of data existing for the given
          key.

RETURN:
  [currently] prints formated output according to what you have supplied.
"""
def build_output(ptvdata, key, data):
  while(True):
    try:
      ptvdata[key] = ptvdata[key].append(data)
      break
    except KeyError:
      ptvdata[key] = []  
      
# Main Module
page = urllib.urlopen("http://ptv.vic.gov.au/disruptions/")
page = page.read()

parser = ptvHTMLParser()

ptvdata = {}

toggle_data = False

parser.feed(page)




