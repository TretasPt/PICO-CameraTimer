import CameraTimerV5 as CT
import time

def minToSec(min):
    return 60*min

def hourToSec(hour):
    return 3600*hour

def isFloat(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

def toSec(time):

    number = time[0:-1]
    if not isFloat(number):
        raise Exception("Badly formated time. The time should be a number followed by a unit. Units are s(econd), m(inute) and h(hour). Exaple: \"30s\". Argument that generated the error: " + time)
    number= float(number)
    unit = time[-1]

    if unit == "s":
        return number
    elif unit == "m":
        return minToSec(number)
    elif unit == "h":
        return hourToSec(number)
    else:
        raise Exception("Badly formated time. The time should be a number followed by a unit. Units are s(econd), m(inute) and h(hour). Exaple: \"30s\". Argument that generated the error: " + time)
        

def read(lines):

    for line in lines:
        readLine(line)


def readLine(line):
    line = line.strip()

    if line=="" or line.startswith("//"):
        #print("Skip")
        return
    elif line.startswith("photo"):
        duration = toSec(removeParenteses(line[5:]))
        print("picture(%s)" % duration)
        picture(duration)
    elif line.startswith("wait"):
        duration = toSec(removeParenteses(line[4:]))
        print("wait(%s)" % duration)
        wait(duration)
    else:
        print("unrecognized.")


def wait(duration):
    time.sleep(duration)

def picture(duration):
    CT.triggerCamera(True)
    time.sleep(duration)
    CT.triggerCamera(False)

def ledBlink(amount, frequency):
    for i in range(amount):
        CT.triggerLed(True)
        time.sleep(1/frequency)
        CT.triggerLed(False)
        time.sleep(1/frequency)

def removeParenteses(str):
    if(len(str)<3 or str[0]!="(" or str[-1]!=")"):
        raise Exception("Invalid argument format.")
    return str[1:-1]