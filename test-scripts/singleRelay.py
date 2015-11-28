import RPi.GPIO as GPIO, time
import sys
import time

pin_map = [11,12,13,15,16,18,22,7,29,31,32,33,35,36,37,38]

pin = int(sys.argv[1]) - 1

print("Getting Started")
GPIO.setmode(GPIO.BOARD)
for i in range(0,16):
    GPIO.setup(pin_map[i], GPIO.OUT)

print("Turning on")
GPIO.output(pin_map[pin], True)
time.sleep(2.0)
print("Turning off")
GPIO.output(pin_map[pin], False)

GPIO.cleanup()

