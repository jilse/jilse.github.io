import gps
import time
import json
import RPi.GPIO as GPIO
import os
GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.OUT)
GPIO.output(4,False)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
repopath= "/home/pi/gitrepo/jilse.github.io/"

def writemdfile(lat, lon, fileitme):
	targetfile = open(repopath + "_posts/SailTracks/"+time.strftime("%Y-%m-%d-Sailtrack-") + fileitme+".md", 'w')
	targetfile.write("---\n")
	targetfile.write("layout: track\n")
	targetfile.write("title: sail track "+ fileitme +"\n")
	targetfile.write("categories: sailtrack\n")
	targetfile.write("date: " + time.strftime("%Y-%m-%d") + "\n")
	targetfile.write("published: false\n")
	targetfile.write("geo: " + fileitme + ".json\n")
	targetfile.write("geocenterlon: "+ str(lon) +"\n")
	targetfile.write("geocenterlat: "+ str(lat) +"\n")
	targetfile.write("mapzoom: 11\n")
	targetfile.write("---\n\n")
	targetfile.flush()
	targetfile.close()
	return
def blink(wait):
	GPIO.output(4,True)
	time.sleep(wait)
	GPIO.output(4,False)
	time.sleep(wait)
	return

timestr = ""
session = gps.gps("localhost", "2947")
session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)
firstrun = True
lasttime = ""
firsttime = ""
cachefilepath = ""

started = False
pausecount = 0
while True:
	
	start_button_up = GPIO.input(18)
	if started == False and start_button_up == True:
		pausecount+=1
		if(pausecount == 20):
			pausecount = 0
			blink(0.1)
		else:
			time.sleep(0.2)
		continue
	
	if started == False:
		# wait for button release
		start_button_up = GPIO.input(18)
		while start_button_up == False:
			blink(.25)
			start_button_up = GPIO.input(18)
			
		timestr = time.strftime("%Y-%m-%d-%H.%M.%S")
		cachefilepath = repopath + "sailtrack/" + timestr + "-cache.json"
		cachefile = open(cachefilepath, 'w', 1)
		started = True
		firstrun = True
	try:
		report = session.next()
		# Wait for a 'TPV' report and display the current time
		if report['class'] == 'TPV':
			if hasattr(report, 'time') and hasattr(report, 'lat') and  hasattr(report, 'lon'):
				lasttime = report.time
				if firstrun == True:
					firsttime = report.time
					writemdfile(report.lat, report.lon, timestr)
					firstrun = False
					
				cachefile.write(str(round(report.lon, 5)) + ",")
				cachefile.write(str(round(report.lat, 5)) + "\n")
				blink(1)
	except KeyError:
		pass
	except KeyboardInterrupt:
		break
	except StopIteration:
		session = None		

	start_button_up = GPIO.input(18)
	closetrack = start_button_up == False
	
	while start_button_up == False:
			blink(.25)
			start_button_up = GPIO.input(18)
	if closetrack == True:		
		cachefile.flush()
		cachefile.close()
		datafile = open(repopath + "sailtrack/" + timestr + ".json", 'w', 500)
		f = open(repopath + "sailtracktemplate.json", 'r')
		json_data = f.read()
		f.close()
		basetemplate = "{\"type\": \"FeatureCollection\",\"features\": ["+ json_data +"]}"
		jd = json.loads(basetemplate)
		cachereader = open(cachefilepath, 'r').read().splitlines()

		for line in cachereader:
			jd["features"][0]["geometry"]["coordinates"].append([float(line.split(",")[0]),float(line.split(",")[1])])
		jd["features"][0]["properties"]["powertype"] = "sail"
		jd["features"][0]["properties"]["start"] = firsttime
		jd["features"][0]["properties"]["end"] = lasttime

		datafile.write(json.dumps(jd))
		datafile.flush()
		datafile.close()
		os.remove(cachefilepath)
		started = False
GPIO.cleanup()

