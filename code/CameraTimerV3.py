# import time
import board
import digitalio
import CameraConfigReader


#Indicative of progress
led = digitalio.DigitalInOut(board.GP25)
led.direction = digitalio.Direction.OUTPUT

#Yank out the key in case of problems with the loop.
key = digitalio.DigitalInOut(board.GP0)
key.direction = digitalio.Direction.INPUT
key.pull = digitalio.Pull.UP

camera_trigger = digitalio.DigitalInOut(board.GP18)
camera_trigger.direction=digitalio.Direction.OUTPUT
camera_trigger.value = True

def getKey():
    return key.value

def readConfig():
    try:
        file = open("./run.camera", "r")
        # lines = file.readlines
        return file
    except OSError:  # open failed
        print("No config file found.")
        return False


def run():
    lines = readConfig()
    if(lines ==False):
        return

    CameraConfigReader.read(lines)



def triggerCamera(state):
    camera_trigger.value = not state

def triggerLed(state):
    led.value = state