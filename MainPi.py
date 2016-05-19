#!/usr/bin/python
# Example using a character LCD plate.
import time

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
def AnchorDistance():
    return "perfectly placed"
class NavItem:
    def __init__(self, name, childItems, dataReport = None):
        self.name = name
        self.childItems = childItems
        self.dataReport = dataReport
    
lcd = LCD.Adafruit_CharLCDPlate()
lcd.clear()

menu = [];
menu.append(NavItem("Anchor", [NavItem("Main Menu", menu),
                               NavItem("Status", []), 
                               NavItem("Distance From Anchor", [], AnchorDistance),
                               NavItem("Alarm Status", []),
                               NavItem("Upload Status", [])]))
menu.append(NavItem("Track", [NavItem("main menu", menu),
                               NavItem("Status", []),
                               NavItem("current speed", []),
                               NavItem("current position", []),
                               NavItem("max speed", [])]))
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
        elif currentMenu[currentMenuIndex].dataReport is not None:
            lcd.clear()
            lcd.set_cursor(0,0)
            lcd.message("-" + currentMenu[currentMenuIndex].name)
            lcd.set_cursor(0,1)
            lcd.message(currentMenu[currentMenuIndex].dataReport())
        waitForRelease(LCD.SELECT)
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
        
