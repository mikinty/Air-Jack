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

while True: # Run forever
    s = int.from_bytes(ser.read(size=1), byteorder="big")
    if(s != ord('s')):
	    print("Something is wrong")
	    continue
    a = int.from_bytes(ser.read(size=1), byteorder="big")
    b = int.from_bytes(ser.read(size=1), byteorder="big")
    c = int.from_bytes(ser.read(size=1), byteorder="big")

    if (a!=0):
        playSound(sounds[a-1])
    if (b!=0):
        playSound(sounds[b+8-1])
    if (c!=0):
        playSound(sounds[b+16-1])
    #play sound based on a, b, c
    print(a, b, c)
    e = int.from_bytes(ser.read(size=1), byteorder="big")
    if(e != ord('e')):
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
