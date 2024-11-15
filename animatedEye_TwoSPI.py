#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import sys 
import time
import logging
import spidev as SPI
sys.path.append("..")
from lib import LCD_1inch28
from PIL import Image, ImageDraw, ImageFont

# Raspberry Pi pin configuration pour le premier écran (SPI0)
bus1 = 0  # SPI0
RST1 = 27  # GPIO pour le reset du premier écran
DC1 = 25   # GPIO pour le DC du premier écran
BL1 = 23   # GPIO pour le rétroéclairage du premier écran
device1 = 0  # Chip Select 0 sur SPI0

# Raspberry Pi pin configuration pour le deuxième écran (SPI1)
bus2 = 1  # SPI1
RST2 = 5  # GPIO pour le reset du deuxième écran
DC2 = 19   # GPIO pour le DC du deuxième écran
BL2 = 6   # GPIO pour le rétroéclairage du deuxième écran
device2 = 0  # Chip Select 0 sur SPI1

"""
- VCC : 5V
- GND : GND
- DIN (MOSI) : Pin 38 (SPI1 MOSI)
- CLK (SCLK) : Pin 40 (SPI1 SCLK)
- CS (Chip Select) : Pin 36 (SPI1 CE0)
- DC : GPIO 35 (choisir un GPIO libre)
- RST : GPIO 33 (choisir un GPIO libre)
- BL : GPIO 31 (Autre GPIO libre pour le rétroéclairage.)
"""

DELAY1 = 0.01
DELAY2 = 2

# Fonction pour afficher une image sur un écran donné
def setImgToScreen(disp, pathImage):
    disp.ShowImage(Image.open(pathImage))
    time.sleep(DELAY1)

# Fonctions pour le premier écran
def openEye1():
    setImgToScreen(disp1, './pic/CLEAR.png')
    setImgToScreen(disp1, './pic/anim7.png')
    setImgToScreen(disp1, './pic/anim6.png')
    setImgToScreen(disp1, './pic/anim5.png')
    setImgToScreen(disp1, './pic/anim4.png')
    setImgToScreen(disp1, './pic/anim3.png')
    setImgToScreen(disp1, './pic/anim2.png')
    setImgToScreen(disp1, './pic/anim1.png')

def closeEye1():
    setImgToScreen(disp1, './pic/anim1.png')
    setImgToScreen(disp1, './pic/anim2.png')
    setImgToScreen(disp1, './pic/anim3.png')
    setImgToScreen(disp1, './pic/anim4.png')
    setImgToScreen(disp1, './pic/anim5.png')
    setImgToScreen(disp1, './pic/anim6.png')
    setImgToScreen(disp1, './pic/anim7.png')
    setImgToScreen(disp1, './pic/CLEAR.png')

# Fonctions pour le deuxième écran
def openEye2():
    setImgToScreen(disp2, './pic/CLEAR.png')
    setImgToScreen(disp2, './pic/anim7.png')
    setImgToScreen(disp2, './pic/anim6.png')
    setImgToScreen(disp2, './pic/anim5.png')
    setImgToScreen(disp2, './pic/anim4.png')
    setImgToScreen(disp2, './pic/anim3.png')
    setImgToScreen(disp2, './pic/anim2.png')
    setImgToScreen(disp2, './pic/anim1.png')

def closeEye2():
    setImgToScreen(disp2, './pic/anim1.png')
    setImgToScreen(disp2, './pic/anim2.png')
    setImgToScreen(disp2, './pic/anim3.png')
    setImgToScreen(disp2, './pic/anim4.png')
    setImgToScreen(disp2, './pic/anim5.png')
    setImgToScreen(disp2, './pic/anim6.png')
    setImgToScreen(disp2, './pic/anim7.png')
    setImgToScreen(disp2, './pic/CLEAR.png')

# Initialisation du premier écran (SPI0)
spi1 = SPI.SpiDev(bus1, device1)  # Créer une instance SPI pour le premier écran
disp1 = LCD_1inch28.LCD_1inch28(spi=spi1, rst=RST1, dc=DC1, bl=BL1)
disp1.Init()  # Initialiser la bibliothèque pour le premier écran.
disp1.clear()  # Nettoyer l'écran.

# Initialisation du deuxième écran (SPI1)
spi2 = SPI.SpiDev(bus2, device2)  # Créer une instance SPI pour le deuxième écran
disp2 = LCD_1inch28.LCD_1inch28(spi=spi2, rst=RST2, dc=DC2, bl=BL2)
disp2.Init()  # Initialiser la bibliothèque pour le deuxième écran.
disp2.clear()  # Nettoyer l'écran.

while True:
    openEye1()  # Animation sur le premier écran
    openEye2()  # Animation sur le deuxième écran
    time.sleep(DELAY2)
    closeEye1()  # Fermer les yeux sur le premier écran
    closeEye2()  # Fermer les yeux sur le deuxième écran
    time.sleep(DELAY2)

disp1.module_exit()
disp2.module_exit()
logging.info("quit:")
exit()

