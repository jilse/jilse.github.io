import gps
import time
import json

print "starting" 
# Listen on port 2947 (gpsd) of localhost
timestr = time.strftime("%Y-%m-%d-%H:%M:%S")

session = gps.gps("localhost", "2947")
session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)
targetfile = open("_posts/SailTracks/"+timestr+".md", 'w')
targetfile.write("---\r")
targetfile.write("layout: track\r")
targetfile.write("title: sail track\n")
targetfile.write("categories: sailtrack\n")
targetfile.write("date: " + timestr + "\n")
targetfile.write("published: false\n")
targetfile.write("geo: " + timestr + ".json\n")
targetfile.write("geocenterlon:\n")
targetfile.write("geocenterlat:\n")
targetfile.write("mapzoom: 11\n")
targetfile.write("---\r\r")
targetfile.close()


firstrun = True
lasttime = ""
firsttime = ""
cachefilepath = "sailtrack/" + timestr + "-cache.json"
cachefile = open(cachefilepath, 'w')

while True:
	try:
		report = session.next()
		# Wait for a 'TPV' report and display the current time
		if report['class'] == 'TPV':
			if hasattr(report, 'time') and hasattr(report, 'lat') and  hasattr(report, 'lon'):
				lasttime = report.time
				if firstrun == True:
					firsttime = report.time
					firstrun = False
				cachefile.write(str(report.lon) + ",")
				cachefile.write(str(report.lat) + "\n")
				print "write"
	except KeyError:
		pass
	except KeyboardInterrupt:
		break
	except StopIteration:
		session = None		


cachefile.close()
datafile = open("sailtrack/" + timestr + ".json", 'w')
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
datafile.close()

