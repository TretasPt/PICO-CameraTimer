import time
import board
import digitalio
import analogio

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

#output = digitalio.DigitalInOut(board.GP17)
#output.direction = digitalio.Direction.OUTPUT

speed_controller = analogio.AnalogIn(board.GP27)

def get_speed():
    return max(min((speed_controller.value-176)/65344,1),0)


while not key.value:
    
    #print(get_speed())
    
    led.value = True
    camera_trigger.value = False
#    output.value = True
    time.sleep(get_speed())
    camera_trigger.value = True
    led.value = False
#    output.value = False
    time.sleep(get_speed())
