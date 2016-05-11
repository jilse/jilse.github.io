import gps
import time
import json
import RPi.GPIO as GPIO
import os
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)

def writemdfile(lat, lon):
	targetfile = open("_posts/SailTracks/"+time.strftime("%Y-%m-%d-Sailtrack-") + timestr+".md", 'w')
	targetfile.write("---\r")
	targetfile.write("layout: track\r")
	targetfile.write("title: sail track "+ timestr +"\n")
	targetfile.write("categories: sailtrack\n")
	targetfile.write("date: " + time.strftime("%Y-%m-%d") + "\n")
	targetfile.write("published: false\n")
	targetfile.write("geo: " + timestr + ".json\n")
	targetfile.write("geocenterlon:"+ str(lat) +"\n")
	targetfile.write("geocenterlat:"+ str(lon) +"\n")
	targetfile.write("mapzoom: 11\n")
	targetfile.write("---\r\r")
	targetfile.flush()
	targetfile.close()
	return
def blink(wait):
	GPIO.output(7,True)
	time.sleep(wait)
	GPIO.output(7,False)
	time.sleep(wait)
	return

timestr = time.strftime("%Y-%m-%d-%H:%M:%S")
session = gps.gps("localhost", "2947")
session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)
firstrun = True
lasttime = ""
firsttime = ""
cachefilepath = "sailtrack/" + timestr + "-cache.json"
cachefile = open(cachefilepath, 'w', 1)

while True:
	try:
		report = session.next()
		# Wait for a 'TPV' report and display the current time
		if report['class'] == 'TPV':
			if hasattr(report, 'time') and hasattr(report, 'lat') and  hasattr(report, 'lon'):
				lasttime = report.time
				if firstrun == True:
					firsttime = report.time
					writemdfile(report.lat, report.lon)
					firstrun = False
					
				cachefile.write(str(report.lon) + ",")
				cachefile.write(str(report.lat) + "\n")
				blink(1)
	except KeyError:
		pass
	except KeyboardInterrupt:
		break
	except StopIteration:
		session = None		

cachefile.flush()
cachefile.close()
datafile = open("sailtrack/" + timestr + ".json", 'w', 500)
f = open("sailtracktemplate.json", 'r')
json_data = f.read()
f.close()
basetemplate = "{\"type\": \"FeatureCollection\",\"features\": ["+ json_data +"]}"
jd = json.loads(basetemplate)
cachereader = open(cachefilepath, 'r').read().splitlines()

for line in cachereader:
	print "0: " + line.split(",")[0] + "\r"
	print "1: " + line.split(",")[1] + "\r"
	jd["features"][0]["geometry"]["coordinates"].append([line.split(",")[0],line.split(",")[1]])
jd["features"][0]["properties"]["powertype"] = "sail"
jd["features"][0]["properties"]["start"] = firsttime
jd["features"][0]["properties"]["end"] = lasttime

datafile.write(json.dumps(jd, indent=4))
datafile.flush()
datafile.close()
GPIO.cleanup()
os.remove(cachefilepath)
