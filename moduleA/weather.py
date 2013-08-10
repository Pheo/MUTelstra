###############################################################################
# UoM M2M Challenge
# HTML Information Extracter
# For use with http://www.weather.com.au
# Renlord Y.
###############################################################################

# Libraries
import urllib

# Key Variables
site = "http://www.weather.com.au"
info = ["city", "forecast", "max", "min"]

# HTML Tag Keywords
tag = "td class"

wpage = urllib.urlopen(site)
lines = wpage.readlines()

# Useful Functions
def htmltag_stripper(string):
    while("<" in string or ">" in string):
        start = string.index("<")
        end = string.index(">")
        if(start < end):
            if(start != 0):
                new_string = string[:start]
                break
            else:
                string = string[end+1:]
        else:
            string = string[1:]
            
    return new_string

# Main Module
weather_d = {}
for line in lines:
    if tag in line:
        start = line.index("=")
        end = line.index(">")
        line_tag = line[start+2:end-1]
        line1 = line[end:]
        # City Information
        if line_tag == info[0]:
            detail = htmltag_stripper(line1)
            weather_d[detail] = {}
        # Forecast Information
        elif line_tag == info[1]:  
            end = line1.index("<")
            detail1 = line1[1:end]
            weather_d[detail]["Forecast"] = detail1       
        # Max Temp.
        elif line_tag == info[2]:
            detail2 = htmltag_stripper(line1)
            weather_d[detail]["Max Temp"] = detail2 + "C" 
        # Min Temp.
        elif line_tag == info[3]:
            detail3 = htmltag_stripper(line1)
            weather_d[detail]["Min Temp"] = detail3 + "C" 


            

        
