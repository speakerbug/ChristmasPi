import sys
import os

try:
    config = str(sys.argv[1])
    mp3 = str(sys.argv[2])
    print 'config file =', config
    print 'mp3 file =', mp3
    systemCall = 'omxplayer -o local ', mp3
    os.system(systemCall)
except IndexError:
    print 'Usage: python xmasparser.py <config file> <mp3 file>'