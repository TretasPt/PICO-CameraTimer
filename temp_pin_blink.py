import time
import board
import digitalio

led = digitalio.DigitalInOut(board.GP25)
led.direction = digitalio.Direction.OUTPUT

output = digitalio.DigitalInOut(board.GP17)
output.direction = digitalio.Direction.OUTPUT

while True:
    led.value = True
    output.value = True
    time.sleep(0.05)
    led.value = False
    output.value = False
    time.sleep(0.05)