#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time
import logging

# Importer la classe AnimatedScreen
from AnimatedScreen import AnimatedScreen

# Configuration des broches GPIO et SPI
# Yeux gauche et droit (partagent le SPI0 avec des chip selects différents)
bus_eyes = 0
rst_eye_left = 27
dc_eye_left = 25
bl_eye_left = 23
device_eye_left = 0

rst_eye_right = 22 # A modifier
dc_eye_right = 24 # A modifier
bl_eye_right = 26 # A modifier
device_eye_right = 1 # A modifier

# Bouche (SPI1)
bus_mouth = 1
rst_mouth = 5
dc_mouth = 19
bl_mouth = 6
device_mouth = 0

# Initialisation des écrans
eye_left = AnimatedScreen(bus_eyes, device_eye_left, rst_eye_left, dc_eye_left, bl_eye_left)
eye_right = AnimatedScreen(bus_eyes, device_eye_right, rst_eye_right, dc_eye_right, bl_eye_right)
mouth = AnimatedScreen(bus_mouth, device_mouth, rst_mouth, dc_mouth, bl_mouth)

# Boucle principale
try:
    while True:
        # Animation pour l'œil gauche
        eye_left.display_gif('./pic/open.gif', delay=0.1)

        # Animation pour l'œil droit
        eye_right.display_gif('./pic/close.gif', delay=0.1)

        # Animation pour la bouche
        mouth.display_gif('./pic/mouth.gif', delay=0.1)
except KeyboardInterrupt:
    # Nettoyer les écrans avant de quitter
    eye_left.close()
    eye_right.close()
    mouth.close()
    logging.info("Programme arrêté.")
    exit()

