#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time
import logging

# Import the AnimatedScreen class
from lib.AnimatedScreen import AnimatedScreen

# GPIO and SPI pin configuration
# Left and right eyes (sharing SPI0 with different chip selects)
bus_eyes = 0
rst_eye_left = 27
dc_eye_left = 25
bl_eye_left = 23
device_eye_left = 0

rst_eye_right = 22 # To be modified
dc_eye_right = 24 # To be modified
bl_eye_right = 26 # To be modified
device_eye_right = 1 # To be modified

# Mouth (SPI1)
bus_mouth = 1
rst_mouth = 5
dc_mouth = 19
bl_mouth = 6
device_mouth = 0

# Initialize the screens
eye_left = AnimatedScreen(bus_eyes, device_eye_left, rst_eye_left, dc_eye_left, bl_eye_left)
eye_right = AnimatedScreen(bus_eyes, device_eye_right, rst_eye_right, dc_eye_right, bl_eye_right)
mouth = AnimatedScreen(bus_mouth, device_mouth, rst_mouth, dc_mouth, bl_mouth)

# Main loop
try:
    print("GIF for the left eye")
    eye_left.display_gif('./pic/open.gif', delay=0.1)

    print("GIF for the right eye")
    eye_right.display_gif('./pic/close.gif', delay=0.1)

    print("GIF for the mouth")
    mouth.display_gif('./pic/mouth.gif', delay=0.1)

    print("Image for the left eye")
    eye_left.openEye()
        
except KeyboardInterrupt:
    # Clean up the screens before exiting
    eye_left.close()
    eye_right.close()
    mouth.close()
    logging.info("Program stopped.")
    exit()

