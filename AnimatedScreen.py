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

class AnimatedScreen:
    def __init__(self, bus, device, rst, dc, bl):
        """
        Initialise un écran Waveshare 1.28".
        :param bus: Bus SPI (0 ou 1)
        :param device: Device SPI (0 ou 1 pour CS)
        :param rst: GPIO pour le reset
        :param dc: GPIO pour DC
        :param bl: GPIO pour le rétroéclairage
        """
        self.spi = SPI.SpiDev(bus, device)
        self.display = LCD_1inch28.LCD_1inch28(spi=self.spi, rst=rst, dc=dc, bl=bl)
        self.display.Init()
        self.display.clear()

    def display_gif(self, gif_path, delay=0.1):
        """
        Affiche un GIF animé sur cet écran.
        :param gif_path: Chemin vers le fichier GIF
        :param delay: Délai entre les frames du GIF (en secondes)
        """
        try:
            gif = Image.open(gif_path)
            for frame in ImageSequence.Iterator(gif):
                frame = frame.resize((240, 240))  # Adapter à la résolution de l'écran
                self.display.ShowImage(frame)
                time.sleep(delay)
        except Exception as e:
            logging.error(f"Erreur lors de l'affichage du GIF : {e}")

    def clear(self):
        """Nettoie l'écran."""
        self.display.clear()

    def close(self):
        """Libère les ressources de l'écran."""
        self.display.module_exit()

