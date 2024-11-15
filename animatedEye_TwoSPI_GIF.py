#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import sys
import time
import logging
import spidev as SPI
from PIL import Image, ImageSequence

sys.path.append("..")
from lib import LCD_1inch28

# Configuration des broches pour le premier écran (SPI0)
bus1 = 0  # SPI0
RST1 = 27  # GPIO pour le reset du premier écran
DC1 = 25   # GPIO pour le DC du premier écran
BL1 = 23   # GPIO pour le rétroéclairage du premier écran
device1 = 0  # Chip Select 0 sur SPI0

# Configuration des broches pour le deuxième écran (SPI1)
bus2 = 1  # SPI1
RST2 = 5   # GPIO pour le reset du deuxième écran
DC2 = 19   # GPIO pour le DC du deuxième écran
BL2 = 6    # GPIO pour le rétroéclairage du deuxième écran
device2 = 0  # Chip Select 0 sur SPI1

# Initialisation du premier écran (SPI0)
spi1 = SPI.SpiDev(bus1, device1)  # Créer une instance SPI pour le premier écran
disp1 = LCD_1inch28.LCD_1inch28(spi=spi1, rst=RST1, dc=DC1, bl=BL1)
disp1.Init()  # Initialiser la bibliothèque pour le premier écran
disp1.clear()  # Nettoyer l'écran

# Initialisation du deuxième écran (SPI1)
spi2 = SPI.SpiDev(bus2, device2)  # Créer une instance SPI pour le deuxième écran
disp2 = LCD_1inch28.LCD_1inch28(spi=spi2, rst=RST2, dc=DC2, bl=BL2)
disp2.Init()  # Initialiser la bibliothèque pour le deuxième écran
disp2.clear()  # Nettoyer l'écran

# Boucle principale
try:
    while True:
        # Lire un GIF sur le premier écran
        displayGIF(disp1, '../pic/open.gif')
        # Lire un GIF sur le deuxième écran
        displayGIF(disp2, '../pic/close.gif')
except KeyboardInterrupt:
    # Nettoyer les écrans avant de quitter
    disp1.module_exit()
    disp2.module_exit()
    logging.info("Programme arrêté.")
    exit()

