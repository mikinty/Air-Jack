import pygame 
from time import sleep

import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)

pygame.mixer.init() #turn all of pygame on.
pygame.mixer.set_num_channels(10)  # default is 8

currChannel = 0

def playSound(sound):
  pygame.mixer.Channel(currChannel).play(sound)
  currChannel += 1


effect = pygame.mixer.Sound('guitar-electric/A2.ogg')

while True: # Run forever
    if GPIO.input(10) == GPIO.HIGH:
        print("Button was pushed!")
        playSound(effect)