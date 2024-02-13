import time
from machine import Pin, Timer, reset
import machine
#import sys

import CameraConfigReader

#Indicative of progress
led = Pin("LED", Pin.OUT)

#Yank out the key in case of problems with the loop.
key = Pin(0,Pin.IN,Pin.PULL_UP)

camera_trigger = Pin(18, Pin.OUT, Pin.PULL_UP)
camera_trigger.value(1)


def getKey():
    return not key.value()

def keyChecker(state):
    while(getKey() and state[0]):
        time.sleep(0.01)
    if(getKey()):
        print("Finished execution.")
    else:
        print("Key removed.")
        machine.soft_reset()

def readConfig():
    try:
        file = open("./run.camera", "r")
        # lines = file.readlines
        return file
    except OSError:  # open failed
        print("No config file found.")
        return False


def run(state):
    lines = readConfig()
    if(lines !=False):
        CameraConfigReader.read(lines)
        
    print("Finished. You may now remove the key.")
    state[0]=False



def triggerCamera(state):
    camera_trigger.value(not state)

def triggerLed(state):
    led.value(state)
    