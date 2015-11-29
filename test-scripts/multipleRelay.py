# File: multipleRelay.py
# Henry Saniuk, Jr.
# This script takes in a string of channels and num of 
# seconds to keep them on for testing
#
# Command Line usage:
#   python multipleRelay.py <num of seconds> <string of channels>"

import RPi.GPIO as GPIO, time
import sys
import time

pin_map = [11,12,13,15,16,18,22,7,29,31,32,33,35,36,37,38]

num_seconds = int(sys.argv[1])
pins = str(sys.argv[2]).split(',')

GPIO.setmode(GPIO.BOARD)
for i in range(0,16):
    GPIO.setup(pin_map[i], GPIO.OUT)

for x in range(0,len(pins)):
    print("Turning on channel " + pins[x])
    GPIO.output(pin_map[int(pins[x])-1],True)

print("Will turn off after " + str(num_seconds) + " seconds")
time.sleep(num_seconds)

for i in range(0,16):
        GPIO.output(pin_map[i],False)
GPIO.cleanup()
