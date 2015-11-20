import sys
import pygame

try:
    config = str(sys.argv[1])
    mp3 = str(sys.argv[2])
    print 'config file =', config
    print 'mp3 file =', mp3
    pygame.mixer.init()
    pygame.mixer.music.load(mp3)
    pygame.mixer.music.play()
except IndexError:
    print 'Usage: python xmasparser.py <config file> <mp3 file>'