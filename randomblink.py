# File: randomblink.py
# Henry Saniuk, Jr.
# This script takes in a config file for channels that should blink randomly
#
# Command Line usage:
#   python randomblink.py <config file> <num of blinks>"

import RPi.GPIO as GPIO, time
import sys
import time
import pygame
from random import randint

# Defines the mapping of the GPIO pins on the pi in order of channel
pin_map = [11,12,13,15,16,18,22,7,29,31,32,33,35,36,37,38]

# Defines if program should be in debug mode and 
# print out channels it is turning on and off
debug = True

try:
    config = str(sys.argv[1])
    num_of_blinks = int(sys.argv[2])
    if debug:
        print 'config file =', config
except IndexError:
    print 'Usage: python randomblink.py <config file> <num of blinks>'
    
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

# Start random blink display        
for i in range(0,num_of_blinks):
    next_channel = randint(0,len(seq_data)-1)
    if debug:
    	print("Turning on " + str(seq_data[int(next_channel)]))
    GPIO.output(pin_map[int(seq_data[int(next_channel)])-1],True)
    time.sleep(randint(1,3))
    if debug:
    	print("Turning off " + str(seq_data[int(next_channel)]))
    GPIO.output(pin_map[int(seq_data[int(next_channel)])-1],False)

for i in range(0,16):
        GPIO.output(pin_map[i],False)
GPIO.cleanup()
print("Ending random blink display")
