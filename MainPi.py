#!/usr/bin/python
# Example using a character LCD plate.
import time
import threading
import Adafruit_CharLCD as LCD

def waitForRelease(button):
    while lcd.is_pressed(button):
        time.sleep(.001)

def drawMenu():
    lcd.clear()
    lcd.set_cursor(0,0)
    lcd.message(">" + currentMenu[currentMenuIndex].name)
    lcd.set_cursor(0,1)
    if len(currentMenu) > (currentMenuIndex+1):
        lcd.message(" " + currentMenu[currentMenuIndex + 1].name)    
class AnchorDistance:
    def __init__(self):
        self.refreshRate = 3
        self.counter = 0
        self.action = None
    def show(self):
        self.counter = self.counter +1
        return "reasons " + str(self.counter)

class StatusBase:
    def __init__(self):
        self.refreshRate = 0
        self.trackState = "stopped"
    def show(self):
        return self.trackState
    def action(self):
        if self.trackState == "stopped":
            self.run()
            self.trackState = "running"
        else:
            self.stop()
            self.trackState = "stopped"

class SailTrackStatus(StatusBase):
    def __init__(self):
        self.refreshRate = 0
        self.trackState = "stopped"
    def run(self):
        print "run the gps tracker and log to website"
    def stop(self):
        print "stop the gps tracker"

class AnchorWatchStatus(StatusBase):
    def __init__(self):
        self.refreshRate = 0
        self.trackState = "stopped"
    def run(self):
        print "run the anchor watch"
    def stop(self):
        print "stop the anchor watch"        
        
class NavItem:
    def __init__(self, name, childItems, configure = None):
        self.name = name
        self.childItems = childItems
        self.configure = configure        
    
lcd = LCD.Adafruit_CharLCDPlate()
lcd.clear()

menu = [];
menu.append(NavItem("Anchor", [NavItem("Main Menu", menu),
                               NavItem("Status", [], AnchorWatchStatus()), 
                               NavItem("Distance From Anchor", [], AnchorDistance()),
                               NavItem("Alarm Status", []),
                               NavItem("Upload Status", [])]))
menu.append(NavItem("Track", [NavItem("Main Menu", menu),
                               NavItem("Status", [], SailTrackStatus()),
                               NavItem("Current Speed", []),
                               NavItem("Current Position", []),
                               NavItem("Max Speed", [])]))
menu.append(NavItem("Battery Voltage", [NavItem("Main Menu", menu),
                                        NavItem("Current V.", []),
                                        NavItem("Upload Status", [])]))
            
currentMenuIndex = 0
currentMenu = menu
drawMenu()
while True:
    if lcd.is_pressed(LCD.SELECT):
        if len(currentMenu[currentMenuIndex].childItems) > 0:
            currentMenu = currentMenu[currentMenuIndex].childItems
            currentMenuIndex = 0
            drawMenu()
            waitForRelease(LCD.SELECT)
        elif currentMenu[currentMenuIndex].configure is not None:
            c = currentMenu[currentMenuIndex].configure
            
            lcd.clear()
            lcd.set_cursor(0,0)
            lcd.message("-" + currentMenu[currentMenuIndex].name)
            lcd.set_cursor(0,1)
            lcd.message(c.show())
            waitForRelease(LCD.SELECT)
            if c.refreshRate > 0:
                while not(lcd.is_pressed(LCD.SELECT)):
                    tevent = threading.Event()
                    tevent.wait(timeout = c.refreshRate)
                    lcd.clear()
                    lcd.set_cursor(0,0)
                    lcd.message("-" + currentMenu[currentMenuIndex].name)
                    lcd.set_cursor(0,1)
                    lcd.message(c.show())
            if not c.action is None:
                while True:
                    if lcd.is_pressed(LCD.LEFT):
                        c.action()
                        waitForRelease(LCD.LEFT)
                        lcd.clear()
                        lcd.set_cursor(0,0)
                        lcd.message("-" + currentMenu[currentMenuIndex].name)
                        lcd.set_cursor(0,1)
                        lcd.message(c.show())
                        continue
                    elif lcd.is_pressed(LCD.SELECT):
                        break                    
                
            currentMenu = menu
            currentMenuIndex = 0
            drawMenu()
            
    if lcd.is_pressed(LCD.LEFT):
        waitForRelease(LCD.LEFT)
    if lcd.is_pressed(LCD.RIGHT):
        waitForRelease(LCD.RIGHT)
    if lcd.is_pressed(LCD.UP) and currentMenuIndex > 0:
        currentMenuIndex = currentMenuIndex - 1
        drawMenu()
        waitForRelease(LCD.UP)
    if lcd.is_pressed(LCD.DOWN):
        if currentMenuIndex < len(currentMenu)-1:
            currentMenuIndex+=1
        else:
            currentMenuIndex = 0                
        drawMenu()    
        waitForRelease(LCD.DOWN)
        
