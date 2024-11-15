#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import sys 
import time
import logging
import spidev as SPI
import threading
from lib import LCD_1inch28
from PIL import Image, ImageDraw, ImageFont

# Raspberry Pi pin configuration
bus = 0
RST = 27
DC = 25
BL = 18

DELAY1 = 0.01
DELAY2 = 2

def setImgToScreen(disp, pathImage):
    disp.ShowImage(Image.open(pathImage))
    time.sleep(DELAY1)

def displayAnimation(disp, images):
    for image in images:
        setImgToScreen(disp, image)

def openEye(disp):
    images = [
        './pic/CLEAR.png',
        './pic/anim7.png',
        './pic/anim6.png',
        './pic/anim5.png',
        './pic/anim4.png',
        './pic/anim3.png',
        './pic/anim2.png',
        './pic/anim1.png'
    ]
    displayAnimation(disp, images)

def closeEye(disp):
    images = [
        './pic/anim1.png',
        './pic/anim2.png',
        './pic/anim3.png',
        './pic/anim4.png',
        './pic/anim5.png',
        './pic/anim6.png',
        './pic/anim7.png',
        './pic/CLEAR.png'
    ]
    displayAnimation(disp, images)

def run_display1():
    disp1 = LCD_1inch28.LCD_1inch28()
    disp1.Init()
    disp1.clear()

    while True:
        openEye(disp1)
        time.sleep(DELAY2)
        closeEye(disp1)

def run_display2():
    disp2 = LCD_1inch28.LCD_1inch28()
    disp2.Init()
    disp2.clear()

    while True:
        openEye(disp2)
        time.sleep(DELAY2)
        closeEye(disp2)

try:
    # Créer les threads pour chaque écran
    thread1 = threading.Thread(target=run_display1)
    thread2 = threading.Thread(target=run_display2)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

except IOError as e:
    logging.info(e)    
except KeyboardInterrupt:
    logging.info("Interrupted by user.")
    exit()

