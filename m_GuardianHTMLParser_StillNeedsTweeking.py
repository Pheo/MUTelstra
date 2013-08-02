# -*- coding: utf-8 -*- 
#
# UoM Telstra M2M Challenge
# HMTL Information Extractor
# for use with Guardian Website (mobile version)
# James Cocks, using a template by Renlord Y.
# Note there are still some bugs when the parser encounters unicode, but
# I think I'll post it up here for others to look at - I've been struggling to
# fix it for a fair while unsuccessfully.
################################################################################
import urllib
import time

from HTMLParser import HTMLParser

# Custom Omissions
blocked_urls = ["uk-news/", "world/", "commentisfree/", "sport/", \
                "football/", "lifeandstyle/", "culture/", "business/", \
                "travel/", "technology/", "environment/", "top-stories/"]
          
parserToggle = False
          
#Blocked data
BlockedData = ['About this site',  'Help', 'Contact us', 'Feedback',\
               'Terms ', '&', ' conditions','Privacy policy','Cookie policy']
unwantedTitleChars = '&nbsp;'#don't want this in the News titles


# HTML Parser
class GuardianHTMLParser(HTMLParser):
   ####### news = {'Name' : '', 'Picture' : ''}
    articleIsFeature = False #in the HTML, a 'feature' article has a
                             #different markup layout than non-features.
    attrsType = ''
    #toggle_mode = 0
    parserToggle = False
    showNextImage = False   #toggles when a relevant headline pops up.
                            #Means that we can get the urls for only the
                            #pictures relevant to the news titles.
    toggle_mode = 'DEFAULT'

    imageThenText = False   # = True when the source contains the image
                            #, followed by the text.
                            # = False otherwise.
    h2_text = False
    
    sameData = False    #prevents data to be mistaken for multiple different
                        #entries.
    lastData = ''       #Keeps a record of what the last data entry was for
                        #the title text, so that it can be concatenated.
    storyNumber = 1
    
    def handle_starttag(self, tag, attrs):
        global numStories# Needed to modify global copy of numStories
        global title#######
        global URL#########
        global trail#######

#        print 'START TAG::::::: ' + tag
        GuardianHTMLParser.sameData = False
        GuardianHTMLParser.lastData = ''
        blocking = False

        GuardianHTMLParser.parserToggle = False
        if tag == "a" and attrs[0][0] == 'href':
            if attrs[1][0] == 'class':
                if attrs[1][1] == 'link-text':
                    GuardianHTMLParser.attrsType = 'link-text'
                    GuardianHTMLParser.parserToggle = True
                    for url in blocked_urls:
                        if url == attrs[1][1]:
                            blocking = True
                            GuardianHTMLParser.parserToggle = False
                            break
                elif attrs[1][1] == "media__img trail__img":
                    GuardianHTMLParser.attrsType = 'image'
                    GuardianHTMLParser.showNextImage = True
                    GuardianHTMLParser.parserToggle = True
                    #return
           
            elif str(attrs[1][1])[-4:] == 'text':#For titles, the last 4 chars
                    #of the second subelement of the second element is 'text'

                GuardianHTMLParser.parserToggle = True 
                GuardianHTMLParser.attrsType = 'link-text'#        


        if tag == 'li':
            if len(attrs)>0 and len(attrs[0])>1:
                if attrs[0][1][13:21] == 'featured':
                    GuardianHTMLParser.articleIsFeature = True

                    numStories = numStories + 1
                    title[numStories] = None
                    URL[numStories] = None
                    trail[numStories] = None
                elif attrs[0][1][13:22] == 'thumbnail':
                    GuardianHTMLParser.articleIsFeature = False

                    numStories = numStories + 1
                    title[numStories] = None
                    URL[numStories] = None
                    trail[numStories] = None
            #print attrs
        elif tag == "img":
            #print attrs
            if (attrs[0][1] == 'maxed' or \
            attrs[1][0] == "data-lowsrc"):

                GuardianHTMLParser.attrsType = 'image'
                GuardianHTMLParser.showNextImage = True
                GuardianHTMLParser.parserToggle = True
                URL[numStories] = attrs[1][1]
                #return
        
        elif tag == "div":
            if attrs == [('class', 'trail__text')]:
                if attrs[0][1] == 'trail__text':
                    GuardianHTMLParser.parserToggle = True
                    GuardianHTMLParser.showNextImage = True
                    GuardianHTMLParser.attrsType = 'trail-text'
                    #return

        elif tag == 'h2':
            GuardianHTMLParser.h2_text = True
            GuardianHTMLParser.parserToggle = True

    #        else:
   #           print attrs
            if not blocking:
                return
        return

    def handle_endtag(self, tag):
        
        global numStories# Needed to modify global copy of numStories
        global title#######
        global URL#########
        global trail#######
        
        if tag == 'h2':
            GuardianHTMLParser.h2_text = False
        elif tag == 'img':
            GuardianHTMLParser.showNextImage = False


        if GuardianHTMLParser.sameData == True:
            print GuardianHTMLParser.lastData
        GuardianHTMLParser.sameData = False
        GuardianHTMLParser.lastData = ''
        return

    def handle_data(self, data):
        global numStories# Needed to modify global copy of numStories
        global title#######
        global URL#########
        global trail#######
        
        if str.strip(data):
            if GuardianHTMLParser.parserToggle == True:
                if GuardianHTMLParser.attrsType == 'link-text' or \
                   GuardianHTMLParser.attrsType == 'trail-text' or \
                   GuardianHTMLParser.attrsType == 'image':
                        
                    if data not in BlockedData:
                        if GuardianHTMLParser.attrsType == 'link-text':
                            if unwantedTitleChars in data:
                                data = data.replace(unwantedTitleChars, ' ')

                            if GuardianHTMLParser.sameData == True:
                                data = GuardianHTMLParser.lastData + data
                            else:
                                title[numStories]=data.strip(' \t\n\r').upper()
                                
                        else:
                            trail[numStories] = data.strip(' ')
                else:
                    print 'wat'
            
        
        GuardianHTMLParser.lastData = data   #in case there's any 
                                        #stuffups with the page's layout
        return

# Main Module
title = {}#######
URL = {}#########
trail = {}#######

numStories = 0
                                      
page = urllib.urlopen("http://m.guardian.co.uk/australia")
page = page.read()

parser = GuardianHTMLParser()

toggle_data = False

parser.feed(page)
print('\n \n \n')

newsdict = {}

for story in range(1, numStories):
    newsdict[story]  ={}
    if title[story] != None:
        newsdict[story]['title'] = title[story]
    else:
        newsdict[story]['title'] = None
    if trail[story] != None:
        newsdict[story]['subtitle'] = trail[story]
    else:

        newsdict[story]['subtitle'] = None
    if URL[story] != None:
        newsdict[story]['URL'] = URL[story]
    else:
        newsdict[story]['URL'] = None

####Just to check that it works (Delete afterwards):
for story in range(1, numStories):
    print newsdict[story]['title']
    print newsdict[story]['subtitle']
    print newsdict[story]['URL']
    print '\n'
