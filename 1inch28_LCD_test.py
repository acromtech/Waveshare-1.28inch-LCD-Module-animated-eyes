#!/usr/bin/python
# -*- coding: UTF-8 -*-
#import chardet
import os
import sys 
import time
import logging
import spidev as SPI
sys.path.append("..")
from lib import LCD_1inch28
from PIL import Image,ImageDraw,ImageFont

# Raspberry Pi pin configuration:
bus=0

RST = 27
DC = 25
BL = 18
device = 0

DELAY = 0.2

logging.basicConfig(level=logging.DEBUG)

try:
    # display with hardware SPI:
    ''' Warning!!!Don't  creation of multiple displayer objects!!! '''
    disp = LCD_1inch28.LCD_1inch28()
    
    # Initialize library.
    disp.Init()

    # Clear display.
    disp.clear()

    while(1):
        logging.info("show image")

        image = Image.open('../pic/anim1.png')	
        disp.ShowImage(image)
        time.sleep(DELAY)
        
        image = Image.open('../pic/anim2.png')	
        disp.ShowImage(image)
        time.sleep(DELAY)
        
        image = Image.open('../pic/anim3.png')	
        disp.ShowImage(image)
        time.sleep(DELAY)

        image = Image.open('../pic/anim4.png')	
        disp.ShowImage(image)
        time.sleep(DELAY)

        image = Image.open('../pic/anim5.png')	
        disp.ShowImage(image)
        time.sleep(DELAY)

        image = Image.open('../pic/anim6.png')	
        disp.ShowImage(image)
        time.sleep(DELAY)

        image = Image.open('../pic/anim7.png')	
        disp.ShowImage(image)
        time.sleep(DELAY)
        
        image = Image.open('../pic/CLEAR.png')	
        disp.ShowImage(image)
        time.sleep(DELAY)

        image = Image.open('../pic/anim7.png')	
        disp.ShowImage(image)
        time.sleep(DELAY)

        image = Image.open('../pic/anim6.png')	
        disp.ShowImage(image)
        time.sleep(DELAY)

        image = Image.open('../pic/anim5.png')	
        disp.ShowImage(image)
        time.sleep(DELAY)

        image = Image.open('../pic/anim4.png')	
        disp.ShowImage(image)
        time.sleep(DELAY)

        image = Image.open('../pic/anim3.png')	
        disp.ShowImage(image)
        time.sleep(DELAY)

        image = Image.open('../pic/anim2.png')	
        disp.ShowImage(image)
        time.sleep(DELAY)

        image = Image.open('../pic/anim1.png')	
        disp.ShowImage(image)
        time.sleep(DELAY)

    disp.module_exit()
    logging.info("quit:")
except IOError as e:
    logging.info(e)    
except KeyboardInterrupt:
    disp.module_exit()
    logging.info("quit:")
    exit()
