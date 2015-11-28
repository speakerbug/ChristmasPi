# File: debugparser.py
# Henry Saniuk, Jr.
# This script is used for debugging without a Raspberry Pi
# but should act like xmasparser.py
#
# Command Line usage:
#   python debugparser.py <config file> <mp3 file>

import sys
import time

# Defines the mapping of the GPIO pins on the Pi in order of channel
pin_map = [11,12,13,15,16,18,22,7,29,31,32,33,35,36,37,38]

debug = True

try:
    config = str(sys.argv[1])
    mp3 = str(sys.argv[2])
    if debug:
        print 'config file =', config
        print 'mp3 file =', mp3
except IndexError:
    print 'Usage: python debugparser.py <config file> <mp3 file>'

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
        # change the pin state
        if next_step[2] == "1":
            if debug:
                print("Turning on " + next_step[1])
        else:
            if debug:
                print("Turning off " + next_step[1])
        # Increment what step we are on
        step += 1

    # This is used to check for END
    if next_step[1].rstrip() == "END":
        if debug:
            print("Reached END")
        # Reached end - End loop
        break