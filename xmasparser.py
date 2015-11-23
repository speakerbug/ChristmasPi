# xmasparser.py
#
# Command Line usage:
#   python xmasparser.py <config file> <mp3 file>

import RPi.GPIO as GPIO, time
import sys
import time
import pygame

# Defines the mapping of the GPIO pins on the Pi in order of channel
pin_map = [11,12,13,15,16,18,22,7,29,31,32,33]

try:
    config = str(sys.argv[1])
    mp3 = str(sys.argv[2])
    print 'config file =', config
    print 'mp3 file =', mp3
except IndexError:
    print 'Usage: python xmasparser.py <config file> <mp3 file>'
    
# Setup the board
GPIO.setmode(GPIO.BOARD)
for i in range(1,12):
    GPIO.setup(pin_map[i], GPIO.OUT)
time.sleep(2.0)

pygame.mixer.init()
pygame.mixer.music.load(mp3)
pygame.mixer.music.play()

# Open the input sequnce file and read/parse it
with open(config,'r') as f:
    seq_data = f.readlines()
    for i in range(len(seq_data)):
        seq_data[i] = seq_data[i].rstrip()

# Start show
start_time = int(round(time.time()*1000))
step = 1 # ignore the header line 
while True :
    next_step = seq_data[step].split(",");
    next_step[1] = next_step[1].rstrip()
    cur_time = int(round(time.time()*1000)) - start_time

    # time to run the command
    if int(next_step[0]) <= cur_time:
        print next_step
        # if the command is Relay 1-12 
        if next_step[1] >= "1" and next_step[1] <= "12":
            # change the pin state
            if next_step[2] == "1":
                GPIO.output(pin_map[int(next_step[1])],True)
            else:
                GPIO.output(pin_map[int(next_step[1])],False)

    # This is used to check for END
    if next_step[1].rstrip() == "END":
        for i in range(1,12):
            GPIO.output(pin_map[i],False)
        #Reached end - End loop
        break
    # Increment what step we are on
    step += 1

GPIO.cleanup()
