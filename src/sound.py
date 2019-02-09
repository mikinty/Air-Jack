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

ser = serial.Serial(port, rate)
ser.flushInput()

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
    sleep(1)
    pygame.mixer.music.load(DRUM_SOUNDS_DIR + DRUM_SOUNDS[0])
    pygame.mixer.music.play(loops= -1, start = 0.0)
    sleep (10)
    break;

    s = int.from_bytes(ser.read(size=1), byteorder="big")
    if(s != ord('s') or s != ord('a')):
             print("Something is wrong")
             continue

    if(s == ord('s')):
      a = int.from_bytes(ser.read(size=1), byteorder="big")
      b = int.from_bytes(ser.read(size=1), byteorder="big")
      c = int.from_bytes(ser.read(size=1), byteorder="big")
      print(a, b, c)

      if (isGuitar):
        if (a!=0):
             playSound(sounds[a-1])
        if (b!=0):
             playSound(sounds[b+8-2])
        if (c!=0):
             playSound(sounds[c+16-3])
      else:
         playSound(sounds[(a+1)/2])
         playSound(sounds[(b+1)/2+4])
         playSound(sounds[(c+1)/2+9])
    else:
       d = int.from_bytes(ser.read(size=1), byteorder="big")
       d = d-48
       currDrumSetting = (currDrumSetting+1)%3
       pygame.mixer.music.stop()
       if (currDrumSetting == 1):
            pygame.mixer.music.load(DRUM_SOUNDS_DIR + DRUM_SOUNDS[d-8])
            pygame.mixer.music.play(loops = -1, start = 0.0)
       elif (currDrumSetting==2):
            pygame.mixer.music.load(DRUM_SOUNDS_DIR + DRUM_SOUNDS[d+1])
            pygame.mixer.music.play(loops = -1, start = 0.0)

    #play sound based on a, b, c
    e = int.from_bytes(ser.read(size=1), byteorder="big")
    if(e != ord('e') or e != ord('b')):
           print("Something is wrong")

    """
    sleep(0.1)
    for i in range(len(sounds)):
        print ("played sound: ", i)
        playSound(sounds[i])
        sleep(1.0)

    for i in range(len(GPIO_INPUT_PINS)):
      inputPin = GPIO_INPUT_PINS[i]

      if GPIO.input(inputPin) == GPIO.HIGH:
        print('Hit string {0}'.format(i))
        playSound(sounds[i])
    """
