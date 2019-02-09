'''
Main file for controlling button logic and registering sounds.
'''
import pygame
from time import sleep
from CONST import *
"""
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library

# GPIO setup
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering

for pin in GPIO_INPUT_PINS:
  # Pull down resistor for buttons
  GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
"""
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
  sleep(0.1)
  for i in range(len(sounds)):
      playSound(sounds[i]) 
      sleep(1.0)
  """   
  for i in range(len(GPIO_INPUT_PINS)):
    inputPin = GPIO_INPUT_PINS[i]

    if GPIO.input(inputPin) == GPIO.HIGH:
      print('Hit string {0}'.format(i))
      playSound(sounds[i])
  """
