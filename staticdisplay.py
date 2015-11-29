# File: staticdisplay.py
# Henry Saniuk, Jr.
# This script takes in a config file for a static display
#
# Command Line usage:
#   python staticdisplay.py <config file> <num of seconds>"

import RPi.GPIO as GPIO, time
import sys
import time
import pygame

# Defines the mapping of the GPIO pins on the pi in order of channel
pin_map = [11,12,13,15,16,18,22,7,29,31,32,33,35,36,37,38]

# Defines if program should be in debug mode and 
# print out channels it is turning on and off
debug = True

try:
    config = str(sys.argv[1])
    num_of_seconds = int(sys.argv[2])
    if debug:
        print 'config file =', config
except IndexError:
    print 'Usage: python staticdisplay.py <config file> <num of seconds>'
    
# Setup the board
GPIO.setmode(GPIO.BOARD)
for i in range(0,16):
    GPIO.setup(pin_map[i], GPIO.OUT)
    GPIO.output(pin_map[i],False)

# Open the input sequnce file and read/parse it
with open(config,'r') as f:
    seq_data = f.readlines()
    for i in range(len(seq_data)):
        seq_data[i] = seq_data[i].rstrip()

# Start static display
i = 1 # ignore the header line 
while True :
    next_channel = seq_data[i]
    if debug:
    	print("Turning on " + str(next_channel))
    GPIO.output(pin_map[int(next_channel)-1],True)
    i += 1

    # This is used to check for END
    if seq_data[i].rstrip() == "END":
        if debug:
            print("Reached END of static display.")
        # Reached end - End loop
        break

print("Will end static display in " + str(num_of_seconds) + " seconds")
time.sleep(num_of_seconds)
for i in range(0,16):
        GPIO.output(pin_map[i],False)
GPIO.cleanup()
print("Ending static display")
