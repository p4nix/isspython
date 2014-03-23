#!/usr/bin/python2.7
import json
import urllib2
import time

print "loading..."
url = "https://api.wheretheiss.at/v1/satellites/25544"
iss = urllib2.urlopen(url)
data = json.load(iss)

# print the result
print('ISS Position:')

print 'Breitengrad:',data["latitude"]

print 'Laengengrad:',data["longitude"]


print 'Hoehe:',int(data["altitude"]),	
if data["units"] == "kilometers":
	print "km"

print 'Sichtbarkeit:',
if data["visibility"]=="daylight":
	print "Ja (Tag)"
else:
	print "Nein (Nacht)"
	print "Geschwindigkeit:",int(data["velocity"]),
if data ["units"] == "kilometers":
	print "km/h"
	lat = str(data["latitude"])
lon = str(data["longitude"])
vel = str(data["velocity"])
maps = str("https://maps.google.com/maps?q="+lat+","+lon+"&z=4")

print maps

url = "http://api.open-notify.org/astros.json"
ppl = urllib2.urlopen(url)
data = json.load(ppl)

list = data["people"]
x = 0
print "Crew:"
while x<len(list):
	craft = str(list[x]["craft"])
	if craft == "ISS": 
		print "	-", list[x]["name"]
	x = x + 1
	
	
