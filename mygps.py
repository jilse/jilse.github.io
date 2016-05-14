import gps 
from datetime import date, datetime, time, timedelta
import json
import RPi.GPIO as GPIO
import os
import threading
from gpspoll import *


def writemdfile(lat, lon, fileitme):
	targetfile = open(repopath + "_posts/sailtrack/"+time.strftime("%Y-%m-%d-Sailtrack-") + fileitme+".md", 'w')
	targetfile.write("---\n")
	targetfile.write("layout: track\n")
	targetfile.write("title: sail track "+ fileitme +"\n")
	targetfile.write("categories: sailtrack\n")
	targetfile.write("date: " + time.strftime("%Y-%m-%d") + "\n")
	targetfile.write("published: false\n")
	targetfile.write("geo: " + fileitme + ".csv\n")
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

repopath= "/home/pi/gitrepo/jilse.github.io/"
captureinterval = 5
firstrun = True

GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.OUT)
GPIO.output(4,False)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

started = False
pausecount = 0
gpsp = GpsPoller()
gpsp.start()
start_on_run = False
while True:
	
	start_button_up = GPIO.input(18)
	if started == False and start_button_up == True and start_on_run == False:
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
			blink(.1)
			start_button_up = GPIO.input(18)			
		
		started = True
		firstrun = True
	try:
		os.system('clear')
		report = gpsp.get_current_value()
		if report.keys()[0] == 'epx':
			GPIO.output(4,True)
			lasttime = report.time
			if firstrun == True:
				gpstime = time.strptime(report.time, "%Y-%m-%dT%H:%M:%S.%fZ")
				timestr = time.strftime("%Y-%m-%d-%H.%M.%S", gpstime)
				writemdfile(report.lat, report.lon, timestr)
				cachefilepath = repopath + "sailtrack/" + timestr + ".csv"
				cachefile = open(cachefilepath, 'w', 1)
				firstrun = False
				
			cachefile.write(str(round(report['lon'], 5)) + ",")
			cachefile.write(str(round(report['lat'], 5)) + ",")
			cachefile.write(str(report['time']) + ",")
			cachefile.write(str(report['speed']) + "\n")
			start_button_up = GPIO.input(18)
			pausecount = 1
			
			while start_button_up == True and pausecount < captureinterval:
				time.sleep(1)
				start_button_up = GPIO.input(18)
				pausecount+=1
			GPIO.output(4,False)
			time.sleep(1)
		else:
			blink(.25)
			blink(.25)
	except KeyError:
		pass
	except KeyboardInterrupt:
		break
	except StopIteration:
		session = None		

	start_button_up = GPIO.input(18)
	closetrack = start_button_up == False
	
	while start_button_up == False:
			blink(.1)
			start_button_up = GPIO.input(18)
	if closetrack == True:		
		cachefile.flush()
		cachefile.close()
		started = False
GPIO.cleanup()

