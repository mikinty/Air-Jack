'''
Main file for controlling button logic and registering sounds.
'''

import pygame
from time import sleep
from CONST import *

import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library

import serial

port = "/dev/ttyUSB0" #cu.usbserial-14410" # check if this is right
rate = 9600

#ser = serial.Serial(port, rate)
#ser.flushInput()

# GPIO setup
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering

for pin in GPIO_INPUT_PINS:
  # Pull down resistor for buttons
  GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Pygame sound setup
pygame.mixer.init() #turn all of pygame on.
pygame.mixer.set_num_channels(NUM_CHANNELS)  # default is 8


# Set up multiple event playing channels
currChannel = 0
isGuitar = True

def playSound(sound):
  '''
  A queueing system to play multiple sounds
  '''
  global currChannel
  pygame.mixer.Channel(currChannel).play(sound)
  currChannel = (currChannel + 1) % NUM_CHANNELS

# Load sounds
sounds = []
for s in GUITAR_NOTES:
  sounds.append(pygame.mixer.Sound(GUITAR_SOUNDS_DIR + s))

# Load drum sounds
drumSounds = []
for d in DRUM_SOUNDS:
  drumSounds.append(pygame.mixer.Sound(DRUM_SOUNDS_DIR+ d))

currDrumSetting = 0 #0 = no drums; 1 = metronome; 2 = drum loop
while True: # Run forever
    #sleep(1)
    #pygame.mixer.music.load(DRUM_SOUNDS_DIR + DRUM_SOUNDS[0])
    #pygame.mixer.music.play(loops= -1, start = 0.0)
    sleep (7)

    currDrumSetting = (currDrumSetting+1)%3
    print ("newCurrDrumSetting: ",currDrumSetting)
    pygame.mixer.music.stop()
    if (currDrumSetting == 1):
            pygame.mixer.music.load(DRUM_SOUNDS_DIR + DRUM_SOUNDS[5])
            pygame.mixer.music.play(loops = -1, start = 0.0)
    elif (currDrumSetting==2):
            pygame.mixer.music.load(DRUM_SOUNDS_DIR + DRUM_SOUNDS[13])
            pygame.mixer.music.play(loops = -1, start = 0.0)
